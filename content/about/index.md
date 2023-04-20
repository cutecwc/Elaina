---
title: "About"
description: "A few years ago, while visiting or, rather, rummaging about Notre-Dame, the author of this book found, in an obscure nook of one of the towers, the following word, engraved by hand upon the wall: —ANANKE."
image: '/images/post/23年2月/Screenshot_20230208_154626.avif'
---




** (9) **
{{< figure src="/images/post/23年2月/80468767_p0.avif" title="(9)" >}}

这是wxymywill的个人博客(先行版)-cc.elaina.cc(https://cc.eelaina.cc/ )。
网页使用的静态网站，由Github保存，由Netlify(Netlify->Vercel)构建并发布。其中图床使用的是xx，在国内大概率加载不出来。由于是学习记录，文章的内容可能修改特别频繁，其中错误难免较多，欢迎前往xx(不维护)的评论区提出。

```markdown
**TODO: **
[待解决] 文章将对图片格式进行修改（常规图片-->avif），届时将会有部分图片无法访问；在不收支持的浏览器中加载avif亦将无法访问。
```

以下是部分的参数记录：

```markdown
# MD文件头：
> title: "{{ replace .Name "-" " " | title }}" 标题
> date: {{ .Date }} 日期
> lastmod: "2022-10-01" 最后修改日期

** set false when you want the post publish **
> draft: true/false

** 用逗号隔开多个string,任有其它形式可以支持。**
* one category: ["category-1"] 
* more categories: ["category-1", "category-2", ...]
> categories: []

** refer to categories **
tags: []
** seires **
series: []
** Top image for the post **
image: "" 在静态中放置需要的文件。


博客主题来自 [Here](https://github.com/xioyito/NewBee)。
```

[测试文件](/files/clash.tar.gz)下载(文件已删除)。
