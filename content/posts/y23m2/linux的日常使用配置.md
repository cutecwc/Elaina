---
title: "linux的日常使用"
description: "nothing else"
image: 'https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/111da.png'
draft: false
date: 2023-02-14
lastmod: 2023-02-23
categories: ["发现"]
tags: ["教程/搭建"]
---


推荐阅读：[代理搭建测试](https://github.com/cutecwc/Elaina/blob/main/content/posts/y23m2/V2Ray%3F.md)

### 1、WPS报告dpi不对称问题

KDE下dpi不对称导致的字体模糊

wps office默认设置dpi为96。但是当kde DPI非96时，会强制修改wps的dpi导致字体模糊

此时只需要在wps（包括wps,wps文字，wps表格，wps演示，wpsPDF）的desktop文件中第四行的Exec添加QT_SCREEN_SCALE_FACTORS=1 即可。如：

```bash
Exec= env QT_SCREEN_SCALE_FACTORS=1 /usr/bin/wps %U
Exec= env QT_SCREEN_SCALE_FACTORS=1 /usr/bin/wpp %F
```

另外，在kde环境(wayland)下，报告的dpi不对称问题，可以将wayland改为x11（默认）。

==------==

改为X11（并使用100%缩放）可以使搜狗输入法在某些情况下不能输入中文的情况得到解决，可以使菜单栏在非全屏时有黑边闪动的情况解决。

### 2、WPS无法打开pdf文件wpspdf 无法打开 PDF 文件

wpspdf 依赖于 libtiff5.so.5 以支撑其 PDF 功能。而系统更新后，Arch Linux 提供的是 libtiff.so.6 或更新版本，导致其无法正常工作。以下为几种可选的解决方案：

1. 安装 [libtiff5](https://aur.archlinux.org/packages/libtiff5/)AUR。
2. 使用 

   ```bash
   sudo ln /usr/lib/libtiff.so.6 /usr/lib/libtiff.so.5
   ```

    创建其硬链接，让 WPS 将 libtiff.so.6 当作 libtiff.so.5 使用。

### 3、endeavouros与archlinux

作为arch的代替，endeavouros可以以图形化的方式使用户很方便地体验到arch。

```markdown
archlinux：自由定制，原教旨主义。
endeavouros：方便、继承archlinux的主义，在安装时为用户部署了一定量的软件（可选），支持图形化安装
manjaro：基于arch思想，但拥有自己特色的发行版，拥有内核管理等有用的小工具，支持图形化安装
```

### 4、某些软件启动报错'appmenu...'

```bash
yay -S appmenu-gtk-module
```

