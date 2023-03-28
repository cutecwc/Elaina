---
title: "笔记停泊站"
description: "nothing else"
image: 'https://mugit.eelaina.cc/cutecwc/pucpica/blob/main/blgold/89893271_p0.jpg?raw=true'
draft: false
date: 2023-03-26
lastmod: 2023-03-26
categories: ["其它"]
tags: ["其它"]
---

# 应该使用的标记：

```markdown
https://mugit.eelaina.cc/cutecwc/pucpica/blob/main/blgold/

{{< figure src="" title="" >}}

end:
```

已经使用的标签：

1. $tags<@>学习笔记<@>$
2. $tags<@>发现<@>$
3. $tags<@>algo-c++<@>$
4. $tags<@>linux使用日志<@>$
5. $tags<@>教程<@>$
6. $tags<@>趣闻<@>$
7. $tags<@>其它<@>$

已经使用的标签：

1. $categories<@>教程/搭建<@>$
2. $categories<@>语言学习<@>$
3. $categories<@>algo-c++<@>$
4. $categories<@>趣闻<@>$
5. $categories<@>其它<@>$

已经使用的系列：

1. $series<@>C++学习笔记<@>$
2. $series<@>leetcode笔记<@>$

![dd](https://mugit.eelaina.cc/cutecwc/pucpica/blob/main/y23m3/Screenshot_20230317_205607.png?raw=true)

------------------

# tip


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






