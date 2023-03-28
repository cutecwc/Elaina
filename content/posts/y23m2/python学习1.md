---
title: "python学习（一）"
description: "python .."
image: ''
draft: false
date: 2023-03-26
lastmod: 2023-03-26
categories: ["其它"]
tags: ["其它"]
---




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
    #         f1.writelines(re.sub(r"(https://mugit.eelaina.cc/cutecwc/pucpica/blob/main/blgold/)","]]]]]]]]]]]",line))
    f1 = open(filepath,'r')
    freadline = f1.readlines()
    f1.close()
    f2 = open(filepath, "w+")
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        a = re.sub(r"(https://mugit.eelaina.cc/cutecwc/pucpica/blob/main/blgold/)",
                   "https://mugit.eelaina.cc/cutecwc/pucpica/blob/main/blgold/", eachline)
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
