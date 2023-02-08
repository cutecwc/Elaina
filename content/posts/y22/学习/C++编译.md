---
title: "C++编译"
description: "C/C++"
image: '/images/post/y22_trans/40011042_p0.jpg'
date: 2022-01-01
categories:
- 学习笔记
tags:
- C语言学习
- 学与思
---

## Compiling the files:

The first step in building a C++ program is to compile the source code files into object files. Object files contain the machine code equivalent of the source code, but they are not yet executable. To compile a C++ source file, such as main.cpp or act.cpp, you will use a C++ compiler. The most common C++ compilers are GCC and Clang.

For example, on Windows, you can use the following command to compile main.cpp using the GCC compiler:

```bash
g++ -c main.cpp
```

This will create an object file named "main.o".

Similarly, you can use the following command to compile act.cpp using the GCC compiler:

```bash
g++ -c act.cpp
```

This will create an object file named "act.o".

Linking the files:

Once you have compiled the source files, you need to link the object files together to create the final executable. Linking combines the object files and resolves any external references between them.

For example, on Windows, you can use the following command to link the object files and create an executable named "main.exe" using the GCC compiler:

```bash
g++ main.o act.o -o main.exe
```

This command tells the linker to link main.o and act.o together to create an executable named main.exe

On some systems, you may need to specify additional libraries or options when linking. For example, if you are using a library, such as the standard library, you will need to include it in the linker command.

```bash
g++ main.o act.o -o main.exe -std=c++11
```

This command tells the linker to link main.o and act.o together to create an executable named main.exe, and also specify the standard library to be used during the linking process.

Please note that the above commands are for GCC on Windows, if you are using different operating systems or compilers, the commands might be slightly different, but the overall process should be similar.



## Git commands and their usage

> 1. `git init`: This command is used to initialize a new Git repository. It creates a new directory named .git that contains all the necessary files for the repository.
> 2. `git clone`: This command is used to create a copy of an existing repository. The clone command creates a new directory and copies all the files from the remote repository to the new directory.
> 3. `git add`: This command is used to stage changes in a local repository. It adds changes to the index, which is a staging area for the repository.
> 4. `git commit`: This command is used to save changes to the local repository. It creates a new commit object that includes a reference to the index and a message describing the changes.
> 5. `git push`: This command is used to upload changes to a remote repository. It sends commits from the local repository to the remote repository.
> 6. `git pull`: This command is used to download changes from a remote repository. It fetches commits from the remote repository and merges them into the local repository.
> 7. `git diff`: This command is used to compare changes between commits, commits and the working tree, commits and index. It shows the differences between two commits or between the working tree and index.
> 8. `git status`: This command is used to check the current status of the repository. It shows the files that have been modified, added, or deleted and also shows the current branch.
> 9. `git log`: This command is used to show the commit history of the repository. It shows the list of commits in reverse chronological order.
> 10. `git branch`: This command is used to create, list, and manage branches in a Git repository. Branches are used to create multiple development lines in a repository.

常见的 Git 命令组如下:

1. 在本地创建一个新的 Git 仓库：`$ git init`
2. 克隆一个远程仓库到本地：`$ git clone <url>`
3. 添加本地修改到暂存区：`$ git add <file>`
4. 提交本地修改到本地仓库：`$ git add <file>`
5. 推送本地仓库的修改到远程仓库：`$ git push origin <branch>`
6. 从远程仓库拉取最新修改到本地仓库：`$ git pull origin <branch>`
7. 查看当前仓库状态:`$ git status`
8. 查看提交历史:`$ git log`
9. 创建、查看、切换分支：`$ git branch`

这些命令是常用的git命令组，在不同的场景下可能会有不同的使用方法。喵~

## Make编译脚本

在 Linux 环境下，可以使用 make 工具来实现自动编译。

Make 是一种自动化编译系统，它可以根据依赖关系来自动编译项目。Make 使用一个名为 Makefile 的文件来描述项目的结构和编译规则。

为了使用 Make 工具编译项目，需要创建一个 Makefile 文件。 Makefile 包含了编译项目所需的所有命令和规则。

下面是一个简单的 Makefile 示例：

```makefile
CC = g++
CFLAGS = -c -Wall

all: main
main: main.o act.o
    $(CC) main.o act.o -o main
main.o: main.cpp
    $(CC) $(CFLAGS) main.cpp
act.o: act.cpp
    $(CC) $(CFLAGS) act.cpp
clean:
    rm -rf *o main
```

这个 Makefile 包含了编译和链接 main.cpp 和 act.cpp 文件所需的命令。

- CC 变量设置编译器为 g++。
- CFLAGS 变量设置编译选项。
- all: main 告诉 make 当执行 make 命令时默认执行 main 目标。
- main: main.o act.o 告诉 make main 目标依赖于 main.o 和 act.o。
- $(CC) main.o act.o -o main 告诉 make 使用 $(CC) 编译器链接 main.o 和 act.o 并生成 main 可执行文件。
- main.o: main.cpp 告诉 make main.o 依赖于 main.cpp。
- $(CC) $(CFLAGS) main.cpp 告诉 make 使用 $(CC) 编译器和 $(CFLAGS) 选项编译 main.cpp。
- clean: 告诉 make 当执行 make clean 时删除所有目标文件和可执行文件。

通过运行 make 命令，就可以根据 Makefile 中的规则自动编译项目。

运行 make clean 命令，会删除所有目标文件和可执行文件。

这样就可以自动编译项目，避免了手动输入命令的繁琐了。

希望这对您有帮助，如果有其他问题请随时问我。喵~

```markdown
问：我在运行上面你给的代码时，它给出了错误：makefile:7: *** 缺失分隔符，停止。这是怎么回事呢
答：这是因为在 Makefile 中缺少了一些必需的分隔符，导致 make 命令无法正确识别规则。
	在 Makefile 中，每一条规则都需要使用冒号（:）来分隔目标和依赖。
	例如，上面给出的示例中的规则 main: main.o act.o 就是正确的规则。
	如果你把冒号漏了，就会出现这样的错误信息。
	请检查你的 Makefile 文件，确保所有规则都使用了冒号分隔目标和依赖。
	请检查你的 makefile 文件，确保每一条规则都是正确的。
	
问：上面你给的的Makefile示例代码中，似乎不定义CC = g++之类的规则，而在下文中直接使用g++也不会影响make结果，那么添加这一步有什么特别含义吗？
答：在 Makefile 中定义变量可以让我们更灵活地管理编译命令。
	例如，通过定义 CC = g++ 变量，我们可以方便地更换编译器。如果要使用其他编译器，只需要更改 CC 变量的值即可。
	同样的，定义 CFLAGS 变量可以让我们更灵活地管理编译选项。如果要更改编译选项，只需要更改 CFLAGS 变量的值即可。
	定义变量可以使 Makefile 更灵活和易于维护。在 Linux 系统中，g++ 默认是安装的，所以我们可以直接使用 g++ 作为编译器。
	但是如果你想要使用其他编译器，或者你的系统中没有安装 g++，那么定义 CC 变量就非常有用了。
	所以 定义变量可以使 Makefile 更灵活和易于维护，增加了程序的可移植性。
	
希望这对你有帮助，如果有其他问题请随时问我。喵~
```



