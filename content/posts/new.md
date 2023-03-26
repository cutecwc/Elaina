---
title: "笔记停泊站"
description: "nothing else"
image: 'https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/89893271_p0.jpg'
draft: false
date: 2023-03-24
lastmod: 2023-03-24
categories: ["其它"]
tags: ["其它"]
---

# 应该使用的标记：

```api
https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/

{{< figure src="" title="" >}}

end:
```

已经使用的标签：

1. 学习笔记
2. 发现
3. algo-c++
4. linux使用日志
5. 教程
6. 趣闻
7. 其它

已经使用的标签：

1. 教程/搭建
2. 语言学习
3. algo-c++
4. 趣闻
5. 其它

已经使用的系列：

1. C++学习笔记
2. leetcode笔记

![dd](https://cdn.jsdelivr.net/gh/cutecwc/pucpica/y23m3/Screenshot_20230317_205607.png)

------------------

# tip

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

如何读取文件

```python
import os
# fileopen reference from: https://www.cnblogs.com/jiaoran/p/14546413.html
# want to get more information from that site above.
# read only the function is, you'd like to copy and workon it.
def func_FilePaser_V1(filepath):
    # TODO edit to open md file from filesystem.
    files = os.listdir(filepath)
    print(files)
    categories_txt = []
    for iterator_file in files:
        position = filepath + "/" + iterator_file
        print(position)
        file_next = os.path.join(filepath, iterator_file)
        if os.path.isdir(file_next):
            func_FilePaser_V1(file_next)
        else:
            print(os.path.join(filepath, file_next))


# fileopen reference from: https://www.cnblogs.com/jiaoran/p/14546413.html
# want to get more information from that site above.
# read only the function is, you'd like to copy and workon it.
def func_FilePaser_V2(filepath):
    # TODO: edit to open md? files from file system.
    for filepathe, dirs, fs in os.walk(filepath):
        for f in fs:
            print(os.path.join(filepathe, f))
```

如何正则匹配？

```python
import re


def func_ReMatch(nameextra, filename):
    # TODO: filename like "***.txt", to give "(.txt)" as nameextra. filename can give by path.
    # you'd like to know "re.match" and "re.search", what differences can be found there.
    # the start string will be matched by "match", while "search" oppose to all things.
    return re.search(nameextra, filename, re.I)


def func_FileOpen(str_filepath):
    f = open(str_filepath, "r+", encoding='UTF-8')
    print(f.read())
    f.close()


def func_FileOpen_SaftyVer(str_filepath):
    with open(str_filepath, "r", encoding='UTF-8') as f:
        print(f.read())
```

```python
# def alter(file, old_str, new_str):
#     with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
#         for line in f1:
#             f2.write(re.sub(old_str, new_str, line))
#     os.remove(file)
#     os.rename("%s.bak" % file, file)
# alter("file1", "admin", "password")
def func_ReviseTest(filepath):
    # TODO: to give a path, to open a file, and the file looks like (/path/**/example.txt)
    # with open(filepath, "r+", encoding='UTF-8') as f1:
    #     for line in f1:
    #         f1.writelines(re.sub(r"(https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/)","]]]]]]]]]]]",line))
    f1 = open(filepath,'r')
    freadline = f1.readlines()
    f1.close()
    f2 = open(filepath, "w+")
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        a = re.sub(r"(https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/)",
                   "https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/", eachline)
        f2.writelines(a)
    f2.close()

def func_MyReMatch(filepath, nameextra):
    for filepathe, dirs, fs in os.walk(filepath):
        for f in fs:
            # print(os.path.join(filepathe, f))
            # print(func_ReMatch(nameextra,os.path.join(filepathe, f)))
            if func_ReMatch(nameextra, os.path.join(filepathe, f)):
                # print(os.path.join(filepathe, f))
                # func_FileOpen(os.path.join(filepathe, f))
                func_ReviseTest(os.path.join(filepathe, f))
```

参考文件[；](https://c.runoob.com/front-end/854/?optionGlobl=global)









