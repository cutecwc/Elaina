---
title: "Git使用实例"
description: "C/C++"
image: '/images/post/23年2月/Screenshot_20230208_210752.jpg'
date: 2022-12-16
categories:
- 学习笔记
tags:
- 语言学习
---



{{< figure src="https://mugit.eelaina.cc/cutecwc/pucpica/blob/main/blgold/104270153_p0.jpg?raw=true" title="zhen" >}}

# Git的使用

```bash
git config --global user.name 'name'
git config --global user.email 'mail address'
```

```bash
#日常使用的git流程
git clone <url> #克隆一个仓库到本地
git add . #添加文件暂存
git commit -m "string to discribe" #提交已暂存的文件
git pull #拉取代码，先同步再推送
git push origin master #推送当前已提交代码到master分支
```

```bash
#本地初始化一个git后，想要推送到远程已有分支，需要先add 这个目标仓库
#err:源引用表达式 main 没有匹配
git init #默认生成master
git remote add <url.gitG>
#以github为例，github默认main为主分支，git创建的默认为master
git branch #查看当前分支名称
git branch -m <branch name> #更改分支名称，使其与远程仓库分支相同

git add .
git commit -m "string"
git push -f origin main #提交更改到远程仓库
```

```bash
git status #查看文件状态
git status -s
```

```bash
git add <specific> #指定某一个文件暂存
```

```bash
git add . 与 git commit -m 'string' 可以合并为:
git commit -am "string"
```

# .git文件过大

可以新初始化一个仓库，将远程仓库除git相关的以外的文件复制到里面，然后强制推送。（可以减少一点点，如果对项目熟悉，可以定期清理git文件；主要还是得把大文件找出来，尽量不上传）

另： github单个文件限制为100M，单个仓库大小限制为1G。

