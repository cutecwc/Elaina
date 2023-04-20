---
title: "linux的日常使用"
description: "nothing else"
image: 'https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/111da.avif?raw=true'
draft: false
date: 2023-02-14
lastmod: 2023-02-23
categories: ["发现"]
tags: ["教程/搭建"]
---


推荐阅读：[代理搭建测试](https://github.com/cutecwc/Elaina/blob/main/content/posts/y23m2/V2Ray%3F.md)

# Linux方法

## 1、zip相关的使用方式


```bash
tar -cvf log.tar log2012.log            # 仅打包，不压缩
tar -zcvf log.tar.gz log2012.log        # 打包后，以 gzip 压缩
tar -jcvf log.tar.bz2 log2012.log       # 打包后，以 bzip2 压缩

tar -ztvf log.tar.gz                    # 查阅上述 tar 包内有哪些文件
tar -zxvf log.tar.gz                    # 将 tar 包解压缩
tar -zxvf log30.tar.gz log2013.log      # 只将 tar 内的部分文件解压出来
```

```bash
gzip * # 将所有文件压缩成 .gz 文件
gzip -l * # 详细显示压缩文件的信息，并不解压
gzip -dv * # 解压上例中的所有压缩文件，并列出详细的信息
gzip -r log.tar     # 压缩一个 tar 备份文件，此时压缩文件的扩展名为.tar.gz
gzip -rv test/      # 递归的压缩目录
gzip -dr test/      # 递归地解压目录
```

```bash
unzip test.zip              # 解压 zip 文件
unzip -n test.zip -d /tmp/  # 在指定目录下解压缩
unzip -o test.zip -d /tmp/  # 在指定目录下解压缩，如果有相同文件存在则覆盖
unzip -v test.zip           # 查看压缩文件目录，但不解压
```

# Arch日志

## 1、WPS报告dpi不对称问题

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

## 2、WPS无法打开pdf文件wpspdf 无法打开 PDF 文件

wpspdf 依赖于 libtiff5.so.5 以支撑其 PDF 功能。而系统更新后，Arch Linux 提供的是 libtiff.so.6 或更新版本，导致其无法正常工作。以下为几种可选的解决方案：

1. 安装 [libtiff5](https://aur.archlinux.org/packages/libtiff5/)AUR。
2. 使用 

   ```bash
   sudo ln /usr/lib/libtiff.so.6 /usr/lib/libtiff.so.5
   ```

    创建其硬链接，让 WPS 将 libtiff.so.6 当作 libtiff.so.5 使用。

## 3、endeavouros与archlinux

作为arch的代替，endeavouros可以以图形化的方式使用户很方便地体验到arch。

```markdown
archlinux：自由定制，原教旨主义。
endeavouros：方便、继承archlinux的主义，在安装时为用户部署了一定量的软件（可选），支持图形化安装
manjaro：基于arch思想，但拥有自己特色的发行版，拥有内核管理等有用的小工具，支持图形化安装
```

## 4、某些软件启动报错'appmenu...'

```bash
yay -S appmenu-gtk-module
```

## 5、archlinux管理助手

```bash
# 使用paru替代yay ?, 日常使用不太会使用到新的特性，就像使用yay一样使用paru吧。
用法:
    paru
    paru <操作> [...]
    paru <软件包>

Pacman 操作:
    paru {-h --help}
    paru {-V --version}
    paru {-D --database}    <选项> <软件包>
    paru {-F --files}       [选项] [文件]
    paru {-Q --query}       [选项] [软件包]
    paru {-R --remove}      [选项] <软件包>
    paru {-S --sync}        [选项] [软件包]
    paru {-T --deptest}     [选项] [软件包]
    paru {-U --upgrade}     [选项] <文件>

新操作:
    paru {-P --show}        [选项]
    paru {-G --getpkgbuild} [软件包]

如果未提供任何参数，则将执行 'paru -Syu'

无操作选项:
    -c --clean              删除不需要的依赖关系
       --gendb              生成用于更新的开发包数据库

新选项:
       --repo               假设目标来自存储库
    -a --aur                假设目标来自AUR
    --aururl    <url>       设置备用 AUR 地址
    --clonedir  <dir>       用于下载和运行 PKGBUILD 的目录

    --makepkg   <file>      使用 makepkg 命令
    --mflags    <flags>     传递参数给 makepkg
    --pacman    <file>      使用 pacman 命令
    --git       <file>      使用 git 命令
    --gitflags  <flags>     传递参数给 git
    --sudo      <file>      使用 sudo 命令
    --sudoflags <flags>     传递参数给 sudo
    --asp       <file>      使用 asp 命令
    --bat       <file>      使用 bat 命令
    --batflags  <flags>     传递参数给 bat
    --gpg       <file>      使用 gpg 命令
    --gpgflags  <flags>     传递参数给 gpg
    --fm        <file>      使用文件管理器审阅 PKGBUILD
    --fmflags   <flags>     传递参数给文件管理器

    --completioninterval    <n>  刷新完成缓存的天数
    --sortby    <field>     在搜索过程中按特定字段对 AUR 结果进行排序
    --searchby  <field>     使用指定字段搜索包
    --limit     <limit>     限制搜索中返回的项目数
    -x --regex              为 aur 搜索启用正则表达式

    --skipreview            跳过审阅流程
    --review                不跳过审阅流程
    --[no]upgrademenu       显示交互式菜单以跳过升级
    --[no]removemake        在安装后删除生成依赖
    --[no]cleanafter        安装后删除软件包源
    --[no]rebuild           始终构建目标软件包
    --[no]redownload        始终下载目标 PKGBUILD

    --[no]pgpfetch          提示从 PKGBUILD 导入 PGP 密钥
    --[no]useask            使用 pacman 询问标志自动解决冲突
    --[no]savechanges       审阅时提交 PKGBUILD 修改
    --[no]newsonupgrade     系统升级时打印新消息
    --[no]combinedupgrade   刷新，然后一起执行存储库和 AUR 升级
    --[no]batchinstall      构建多个AUR包，然后安装
    --[no]provides          在搜索时查找匹配的提供者
    --[no]devel             系统升级时检查开发包
    --[no]installdebug      当软件包提供调试包时，同时安装调试包
    --[no]sudoloop          在后台循环 sudo 调用以避免超时
    --[no]chroot            在 chroot 中构建
    --[no]failfast          构建 AUR 软件包失败后立即退出
    --[no]keepsrc           构建完软件包后保留 src/ 和 pkg/ 目录
    --[no]sign              使用 gpg 签名软件包
    --[no]signdb            使用 gpg 签名数据库
    --localrepo             构建软件包到本地存储库中
    --nocheck               不解决依赖项或运行检查功能
    --develsuffixes         用于确定包是否为开发包的后缀
    --bottomup              首先显示 AUR 包，然后显示存储库的包
    --topdown               首先显示存储库的包，然后显示 AUR 的包

显示特定选项:
    -c --complete           用于完成
    -s --stats              显示系统软件见包统计信息
    -w --news               打印 arch 新闻

获取 PKGBUILD 特定选项：
    -p --print              打印 PKGBUILD 到 stdout
    -c --comments           打印 PKGBUILD 的 AUR 评论
    -s --ssh                使用 SSH 克隆软件包

升级特定选项:
    -i --install            安装软件包以及构建

```

## 文件目录维护

[目录维护](https://cdn.jsdelivr.net/gh/cutecwc/pucpica/y23m4/filePather.py)（待完善，标记已经显示变化的文件，以此完成系统清理）

