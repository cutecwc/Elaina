import os
import time
import re


# to print time the file last revised.
# TODO: done.
# func_TimeGet("file://filepath/filename")
def func_TimeGet(filename):
    filemt = time.localtime(os.stat(filename).st_mtime)
    return time.strftime("%Y-%m-%d", filemt)


# to match (by testing), 输出符合正则的字符串
# TODO: done.
# func_ReMatch("re-description", "file://filepath/filename")
def func_ReMatch(nameextra, filename):
    f1 = open(filename, 'r')
    freadline = f1.readlines()
    f1.close()
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        a = re.search(nameextra, eachline, re.I)
        print(a)
        # print(eachline)


# =============================================================================== #
# def alter(file, old_str, new_str):
#     with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
#         for line in f1:
#             f2.write(re.sub(old_str, new_str, line))
#     os.remove(file)
#     os.rename("%s.bak" % file, file)
# alter("file1", "admin", "password")
# func_ReviseTest("re-description", "file://filepath/filename",
def func_ReviseTest(nameextra, filepath, flags):
    # TODO: to give a path, to open a file, and the file looks like (/path/**/example.txt)
    # with open(filepath, "r+", encoding='UTF-8') as f1:
    #     for line in f1:
    #         f1.writelines(re.sub(r"(https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/)","]]]]]]]]]]]",line))
    f1 = open(filepath, 'r')
    freadline = f1.readlines()
    f1.close()
    f2 = open(filepath, "w+")
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        a = re.sub(nameextra, flags + func_TimeGet(filepath), eachline)
        f2.writelines(a)
    f2.close()


# to match (by testing), 输出符合正则的字符串
# TODO: done.
# func_ReMatch("re-description", "file://filepath/filename")
def func_ReMatchEntry(nameextra, filename):
    f1 = open(filename, 'r')
    freadline = f1.readlines()
    f1.close()
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        return re.search(nameextra, eachline, re.I)
        # print(eachline)


# TODO: single file by walker.
def func_ReviseLinkByWalker(filepath, nameextra, substr):
    # TODO: to give a path, to open a file, and the file looks like (/path/**/example.txt)
    # with open(filepath, "r+", encoding='UTF-8') as f1:
    #     for line in f1:
    #         f1.writelines(re.sub(r"(https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/)","]]]]]]]]]]]",line))
    f1 = open(filepath, 'r')
    freadline = f1.readlines()
    f1.close()
    f2 = open(filepath, "w+")
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        a = re.sub(nameextra, substr, eachline)
        f2.writelines(a)
    f2.close()


def func_ReMatchFileSystemPaser(filepath, nameextra, substr):
    for filepathe, dirs, fs in os.walk(filepath):
        for f in fs:
            # print(os.path.join(filepathe, f))
            # print(func_ReMatch(nameextra,os.path.join(filepathe, f)))
            if func_ReMatchEntry(nameextra, os.path.join(filepathe, f)) == None:
                print(os.path.join(filepathe, f))
                # func_FileOpen(os.path.join(filepathe, f))
                func_ReviseLinkByWalker(os.path.join(filepathe, f), nameextra, substr)

# TODO: done
# func_FileReadByLine("file://filepath/filename")
# display by line, you should refine the catch by yourself.
def func_FileReadByLine(filepath):
    f1 = open(filepath, 'r')
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
            print(eachline, end='')


# TODO: 文件备份:
# func_FileBackupBeforeRevise("file://filepath/filename")
def func_FileBackupBeforeRevised(filepath):
    f1 = open(filepath, 'r')
    freadline = f1.readlines()
    f1.close()
    with open("./new.md.backup", "w") as file:
        for eachline in freadline:
            file.write(eachline)


# ---------------------------------- #

# TODO: 修改制定文件的匹配行。
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

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# TODO: 文件的标签管理工具。
# to match (by testing), 输出符合正则的字符串
# TODO: done.
# func_ReMatch("re-description", "file://filepath/filename")
def func_NewRematcher_list(nameextra, filename):
    f1 = open(filename, 'r')
    freadline = f1.readlines()
    f1.close()
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        a = re.search(nameextra, eachline, re.I)
        if a != None:
            print(a)
        # print(eachline)
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

# TODO: 文件的选择初始化工具（具有时间自动化能力）


# ================================== #
import argparse


# TODO: 参数主体
def args_Defination():
    parser = argparse.ArgumentParser()
    parser.add_argument("--use", "-u", help=" -u, -t ", action="store_true")
    # parser.add_argument('--year', '-y', help='year 属性，非必要参数，但是有默认值', default=2017)
    # parser.add_argument('--body', '-b', help='body 属性，必要参数', required=True)
    parser.add_argument("--time", "-t", help="自动修改时间", action="store_true")
    parser.add_argument("--cdn", "-c", help="更改cdn链接", action="store_true")
    args = parser.parse_args()
    runtimeflags = False
    if args.use and runtimeflags == False:
        print("====================================\n>> 这是一些帮助：")
        print("一、图片使用规则：")
        print("\t （1）、{{< figure src=" " title=" " >}}")
        print("\t （1）、![text]() ")
        runtimeflags = True
        return
    if args.time and runtimeflags == False:
        print("====================================\n>> 已修改... ")
        runtimeflags = True
        ops_RunTimeRevise()
        return
    if args.cdn and runtimeflags == False:
        print("====================================\n>> ")
        # nameextra = r"(jsdelivr.net/gh/cutecwc/pucpica/)"
        # substr = "staticaly.com/gh/cutecwc/pucpica/main/"

        # nameextra = r"(staticaly.com/gh/cutecwc/pucpica/main/)"
        # substr = "jsdelivr.net/gh/cutecwc/pucpica/"

        # https://mugit.eelaina.cc/cutecwc/pucpica/blob/main/y23m3/
        # https://cdn.jsdelivr.net/gh/cutecwc/pucpica/blgold/
        # https://mugit.eelaina.cc/cutecwc/pucpica/blob/main/?
        # append = ?raw=true
        # nameextra = r"(cdn.jsdelivr.net/gh/cutecwc/pucpica/)"
        # substr = "mugit.eelaina.cc/cutecwc/pucpica/blob/main/"

        nameextra = r"mugit\.eelaina\.cc/cutecwc/pucpica/blob/main/"
        substr = "cdn.jsdelivr.net/gh/cutecwc/pucpica/"
        print(" 请确认这个操作：y/n-yes/not")
        argument = input()
        if (argument=='y') or (argument=='yes'):
            func_ReMatchFileSystemPaser("content", nameextra, substr)
            runtimeflags = True
        elif (argument=='n') or (argument=='not'):
            print("cancel..")
        else:
            print("不正确的输入，请重试。")
        return
    if runtimeflags == False:
        print("====================================\n>> 缺少的命令：使用'-u'了解方法。")


import datetime

if __name__ == '__main__':
    args_Defination() #运行主体
    # func_NewRematcher_list(r"\$tags(<@>).*\1\$", "./content/posts/new.md")
    print("\n >>", datetime.datetime.now(), "all done. ")
