import os
import time
import re

# 自动调节时间脚本，仅仅针对置顶文章，python timerevise.py 即可运行

def func_TimeGet(filename):
    filemt = time.localtime(os.stat(filename).st_mtime)
    return time.strftime("%Y-%m-%d", filemt)

def func_ReMatch(nameextra, filename):
    f1 = open(filename,'r')
    freadline = f1.readlines()
    f1.close()
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        a = re.search(nameextra, eachline, re.I)
        print(a)
        print(eachline)


# =============================================================================== #
# def alter(file, old_str, new_str):
#     with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
#         for line in f1:
#             f2.write(re.sub(old_str, new_str, line))
#     os.remove(file)
#     os.rename("%s.bak" % file, file)
# alter("file1", "admin", "password")
def func_ReviseTest(nameextra, filepath, flags):
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
        a = re.sub(nameextra, flags + func_TimeGet(filepath), eachline)
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


# display by line, you should refine the catch by yourself.
def func_FileReadByLine(filepath):
    f1 = open(filepath,'r')
    freadline = f1.readlines()
    f1.close()
    flag = 0
    for eachline in freadline:
        flag += 1
        if flag <= 5:
            continue
        elif flag > 7:
            break
        else:
            print(eachline)



def func_FileBackupBeforeRevised(filepath):
    f1 = open(filepath,'r')
    freadline = f1.readlines()
    f1.close()
    with open("./new.md.backup","w") as file:
        for eachline in freadline:
            file.write(eachline)

# ---------------------------------- #

# this is an operation to revise time.
def ops_RunTimeRevise():
    filepaths = "./content/posts/new.md"
    print("====================================")
    func_FileReadByLine(filepaths)
    func_FileBackupBeforeRevised(filepaths)
    # func_ReMatch(r"date:\ \d{4}-\d{1,2}-\d{1,2}", filepaths)
    func_ReviseTest(r"date:\ \d{4}-\d{1,2}-\d{1,2}", filepaths, "date: ")
    func_ReviseTest(r"lastmod:\ \d{4}-\d{1,2}-\d{1,2}", filepaths, "lastmod: ")
    print("------------------------------------")
    func_FileReadByLine(filepaths)
    print("====================================")
    # func_TimeGet(filepaths)

# ================================== #
import argparse
import sys

def args_Defination():
    parser = argparse.ArgumentParser()
    parser.add_argument("--use", "-u", help=" -u, -t ", action = "store_true")
    # parser.add_argument('--year', '-y', help='year 属性，非必要参数，但是有默认值', default=2017)
    # parser.add_argument('--body', '-b', help='body 属性，必要参数', required=True)
    parser.add_argument("--time", "-t", help=" Runtime get by auto revision. Version 0.1 ", action = "store_true")
    args = parser.parse_args()
    runtimeflags = False
    if args.use:
        print("====================================\n>> helpsget")
        print("一、图片使用规则：")
        print("\t （1）、{{< figure src=" " title=" " >}}")
        print("\t （1）、![text]() ")
        runtimeflags =True
        return
    if args.time:
        print("====================================\n>> time revised... ")
        runtimeflags =True
        ops_RunTimeRevise()
        return
    if runtimeflags==False:
        print("====================================\n>> nothing done. you'd like to give an agument likes '-u'(known how to use it)")

import datetime

if __name__ == '__main__':
    args_Defination()
    print(">>", datetime.datetime.now() , "all done. ")
    
