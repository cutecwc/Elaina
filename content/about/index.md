---
title: "About"
description: "A few years ago, while visiting or, rather, rummaging about Notre-Dame, the author of this book found, in an obscure nook of one of the towers, the following word, engraved by hand upon the wall: —ANANKE."
image: '/images/post/23年2月/Screenshot_20230208_154626.png'
---




** (9) **
{{< figure src="/images/post/23年2月/80468767_p0.jpg" title="(9)" >}}

这是wxymywill的个人博客(先行版)-cc.elaina.cc(https://cc.eelaina.cc/ )。
网页使用的静态网站，由github保存，由netlify构建并发布。其中图床使用的是github，在国内大概率加载不出来。由于是先行版本，本博客可能很少维护或者修改特别频繁，其中错误的地方难免较多，欢迎前往x.x的评论区提出。x_x的维护亦具有不稳定性，通常情况下记载了本网站较为成熟的知识点以供复习使用。

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
