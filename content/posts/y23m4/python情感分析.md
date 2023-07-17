---
title: "python情感分析"
description: "使用Python的SnowNLP库进行商品的情感分析情感分析"
image: 'https://cdn.jsdelivr.net/gh/cutecwc/pucpica/y23m4/106374032_p0.avif'
draft: true
date: 2023-04-11
lastmod: 2023-04-11
categories: ["其它"]
tags: ["其它"]
---

# 一、参考目录

Github：

* [一个基于LSTM](https://github.com/xiaogp/sentiment_analysis)，TextCNN，fasttext实现的购物网站评论情感分析，使用tf_serving和flask部署模型

* [基于tensorflow](https://github.com/norybaby/sentiment_analysis_textcnn) 实现的用textcnn方法做情感分析的项目，有数据，可以直接跑。

* [TextCNN Pytorch实现 中文文本分类](https://github.com/PracticingMan/chinese_text_cnn)

* [中文情感分析之TextCNN](https://github.com/kiss90/textcnn-tf)  预训练中文词向量下载链接:https://pan.baidu.com/s/1UHnVN-HEOJ74f44rLqhggQ 密码:g49h

  推荐先安装Anaconda3 python运行环境，然后安装需要的依赖包:
  
  同类推荐阅读：CSDN-[中文情感分析之TextCNN](https://blog.csdn.net/yingyujianmo/article/details/100048416#commentBox)。

CSDN：

* [NLP-自然语言处理-文本分类](https://blog.csdn.net/weixin_47082769/article/details/122393547)-总结-Tensorflow2.0版
* [中文情感分析之TextCNN](https://blog.csdn.net/yingyujianmo/article/details/100048416)
* Textcnn[介绍](https://www.cnblogs.com/zjuhaohaoxuexi/p/15154597.html)

论文：

* 关于[情感分析的文献综述](https://www.cnblogs.com/NLPlunwenjiedu/p/15864581.html)
* 论[文](https://arxiv.org/pdf/1510.03820.pdf)

知乎：

* [文本分类](https://zhuanlan.zhihu.com/p/149491055) [ALBERT+TextCNN] [中文情感分析]（附代码）
* [TextCNN-](https://zhuanlan.zhihu.com/p/401022125)文本情感分析项目实战

其它：

* Chit[GPT。](https://wenku.csdn.net/answer/9bf3f6bf3d7640ea8a699fbbf6ef9941)
* 腾讯自然语言研究中心（[含数据集](https://ai.tencent.com/ailab/nlp/zh/index.html)）
* 中文词向量（[数据集](https://github.com/Embedding/Chinese-Word-Vectors/blob/master/README_zh.md)）
* github数据集（[link](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/weibo_senti_100k/intro.ipynb)）

# 二、分析

## 0、传统模型的缺点

使用词典构建的深度学习有以下缺点：
精度不高。语言是一个高度复杂的东西，采用简单的线性叠加会造成很大的精度损失。词语权重同样不是一成不变的，而且也难以做到准确。
新词发现困难。对于新的情感词，词典不一定能覆盖到。如“陈独秀同学请坐下”，“同九义，何汝秀”等。
词典构建难。情感词典的构建需要有较强的背景知识，需要对语言有较深刻的理解，构建一个适用于自己的应用场景的情感词典是一项复杂的工作。

可以预见SnowNLP并不是作为情感分析的最佳方法。

基于深度学习的情感分析方法是使用神经网络来进行的，典型的神经网络学习方法有：卷积神经网络（Convolutional Neural Network，CNN）、递 归 神 经 网 络 （Recurrent Neural Network，RNN）、长短时记忆（Long Short-Term Memory，LSTM）网络等。

文本情感分析(sentiment analysis)，又称为意见挖掘，是对带有情感色彩的主观性文本进行分析、处理、归纳和推理的过程。其中，主观情感可以是他们的判断或者评价，他们的情绪状态，或者有意传递的情感信息。因此，情感分析的一个主要任务就是情感倾向性的判断，情感倾向分为正面、负面和中性，即褒义、贬义和客观评价。研究初期，大量研究者都致力于针对词语和句子的倾向性判断研究，但随着互联网上大量主观性文本的出现，研究者们逐渐从简单的情感词语的分析研究过渡到更为复杂的情感句研究以及情感篇章的研究。文本情感分析主要可以归纳为3项层层递进的研究任务，即情感信息的抽取、情感信息的分类以及情感信息的检索与归纳]。情感信息抽取就是将无结构的情感文本转化为计算机容易识别和处理的结构化文本。情感信息分类则是利用情感信息抽取的结果将情感文本单元分为若干类别，供用户查看，如分为褒、贬、客观或者其他更细致的情感类别。情感信息检索和归纳可以看作是与用户直接交互的接口，强调检索和归纳的两项应用。 

情感分析是一个新兴的研究课题，具有很大的研究价值和应用价值，正受到国内外众多研究者的青睐。目前实现情感分析的技术主要包括基于机器学习法和基于语义方法两类。本文主要针对这两大方法的研究进展进行比较分析，接着介绍国内外现有的资源建设情况，最后介绍情感分析的几个重要应用和展望它的发展趋势。

## 1  基于统计机器学习法

随着大规模语料库的建设和各种语言知识库的出现，基于语料库的统计机器学习方法进入自然语言处理的视野。多种机器学习方法应用到自然语言处理中并取得了良好的效果，促进了自然语言处理技术的发展。机器学习的本质是基于数据的学习(Learning from Data)。利用机器学习算法对统计语言模型进行训练，最后用训练好的分类器对新文本情感进行识别。 基本的算法有：支持向量机(SVM)、朴素贝叶斯(NB)、K-近邻(KNN)、简单线性分类器(SLC)和最大熵(ME)等。

近年来有关自然语言处理、人工智能、信息检索、数据挖掘以及Web应用等领域的多个国际顶级会议(AAAI、ACL、SIGIR等)都收录了文本情感倾向分析的相关论文。机器学习的方法虽然在目前来讲分类的准确程度比较高，但是它针对每一种产品使用前，训练样本集的建立都需要采用人工方法对大量的评论文章逐一阅读甄别，并进行手工标志，这与利用自动情感分类降低人的阅读负担这一初衷还有着一定的差距。因此，近来许多研究者将情感分析研究的重点集中在对训练样本的需求量较低的语义方法上。

## 2、基于语义的方法

最初学者想到利用词典将手工采集的种子评价词语进行扩展来获取大量的评价词 .这种方法简单易行，但是较依赖于种子评价词语的个数和质量，并且容易由于一些词语的多义性而引入噪声.为了避免词语的多义性，一部分学者使用词典中词语的注释信息来完成评价词语的识别与极性判断.此外，一些学者沿用了Turney等人的点互信息的方法，通过计算WordNet中的所有形容词与种子褒义词代表good和贬义词bad之间的关联度值来识别出评价词语情感倾向。

基于文本语义理解的情感挖掘北京理工大学大数据搜索与挖掘实验室张华平主任研发了NLPIR大数据语义智能情感分析技术。

NLPIR情感分析技术提供两种模式：全文的情感判别(左图)与指定对象的情感判别(右图)。情感分析主要采用了两种技术：1.情感词的自动识别与权重自动计算，利用共现关系，采用Bootstrapping的策略，反复迭代，生成新的情感词及权重;2.情感判别的深度神经网络：基于深度神经网络对情感词进行扩展计算，综合为最终的结果。NLPIR情感分析内容形式包括特定人物的正、负面分析，这样可以从整体看到特定人物对社会观点和事情的态度，从而来判断他的态度是积极的还是消极的 。同时通过喜、怒、哀、乐、惊、惧等几种情感维度分别展现他的性格取向，是稳重型还是冒进型;是积极乐观的还是消极愤世的;这样就可以综合的反应特定人物的情感状态。

情感分析不是单单的对特定人物感情来进行分析，同时还要对特定人物相关事件一起来分析从而得出更加科学、全面的分析报告。NLPIR系统能够实体抽取智能识别文本中出现的人名、地名、机构名、媒体、作者及文章的主题关键词，这是对语言规律的深入理解和预测，并且其所提炼出的词语不需要在词典库中事先存在。NLPIR实体抽取系统采用基于角色标注算法自动识别命名实体，开发者可在此基础上搭建各种多样化的大数据挖掘应用。

# 三、实践

## 1、数据预处理部分


休止符a




## 0、参考

中文常用停用词表（[。](https://github.com/goto456/stopwords)）

# I、附录

## 一、anaconda配置

Python环境anaconda - Linux（[↑](https://blog.csdn.net/qq_38870718/article/details/122796306)）

archlinux中，安装anaconda只需要使用命令：

```bash
yay -S anaconda
```

如何使用（图形界面等功能）？

```bash
# 可以通过(激活和取消环境)
source /opt/anaconda/bin/activate root
source /opt/anaconda/bin/deactivate root # conda deactivate

# 使用来启动图形界面
anaconda-navigator
```

参考文件（[↑](https://blog.csdn.net/qq_42663663/article/details/125227099)）
