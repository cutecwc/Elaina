---
title: "C++学习笔记（一）：编译器"
description: "nothing else"
image: ''
draft: false
date: 2023-02-23
lastmod: 2023-02-23
series: ["Cplusplus学习笔记"]
categories: ["学习笔记"]
tags: ["语言学习"]
---

# 如何编写makefile文件

makefile示例：

```makefile
cc = g++
co = -c -Wall
target = main.o mkt.o
file_cpp = ./cpp/


all: main

main:main.o mkt.o
	$(cc) $(target) -o main


main.o: main.cpp
	$(cc) $(co) main.cpp
mkt.o: $(file_cpp)mkt.cpp
	$(cc) $(co) $(file_cpp)mkt.cpp


clean:
	rm -f *.o main
```

# clang编译cpp

```markdown
clang是什么?

Clang是一个C、C++和Objective-C编译器，是LLVM编译器工具链的一部分。它是一个开源项目，由苹果公司开发和维护。与传统的GCC编译器相比，Clang编译器具有更快的编译速度和更好的错误诊断能力，并且支持C++11、C++14、C++17等新的C++标准。
Clang的设计目标是提供更好的代码质量和更好的用户体验。它提供了丰富的静态分析功能，包括语法分析、类型检查、控制流分析、数据流分析等，这些功能可以帮助开发者更快地发现代码中的问题并进行修复。此外，Clang还提供了一些有用的工具，如代码重构、静态分析器等，可以帮助开发者提高代码的质量和效率。
Clang被广泛应用于各种开发场景，包括编译器开发、操作系统开发、游戏开发、嵌入式开发等。在Apple公司的Xcode集成开发环境中，Clang是默认的编译器。此外，Clang还被许多其他的集成开发环境和开发工具所采用。
```

```markdown
那clang应该如何使用呢？
```

使用Clang编译器可以分为以下步骤：

1. 安装Clang编译器，可以从官方网站（https://clang.llvm.org/）下载源代码编译安装，也可以从操作系统的软件源中安装。

2. 编写C/C++/Objective-C源代码文件，例如可以使用任何文本编辑器创建一个名为"hello.c"的C源代码文件。

3. 打开终端或命令行工具，进入到存放源代码文件的目录下。

4. 运行Clang编译器进行编译，例如运行以下命令进行C源代码的编译：

   ```bash
   Copy code
   clang hello.c -o hello
   ```

   上面的命令将会生成一个名为"hello"的可执行文件，可以通过运行以下命令来执行它：

   ```bash
   bashCopy code
   ./hello
   ```

   如果想要进行C++或Objective-C的编译，可以将源代码文件的扩展名改为".cpp"或".m"，并使用"clang++"或"clang -ObjC"进行编译。

Clang编译器还支持许多命令行选项，可以通过运行"clang --help"命令来查看所有可用的选项。此外，许多集成开发环境和编辑器也提供了对Clang编译器的集成支持，可以在编辑器中直接使用Clang进行编译和调试。

```markdown
clang与gcc有什么区别呢？
```

Clang和GCC是两种常用的C/C++编译器，它们在许多方面都有不同的特点，包括以下几个方面：

1. 架构：Clang是基于LLVM架构的编译器，而GCC则是自己的编译器框架。相比于GCC，Clang更加模块化、可扩展和易于维护。
2. 编译速度：Clang通常比GCC更快，特别是在大型代码库上进行增量编译时。这是因为Clang采用了一种更加智能的编译策略，能够更好地利用现代计算机的多核处理能力。
3. 代码质量：Clang在语法分析和诊断方面有更强的能力，能够提供更准确和更详细的错误信息和警告信息。这有助于提高代码质量，并且可以更快地发现和修复潜在的问题。
4. 标准支持：Clang和GCC都支持C和C++标准，但是Clang通常更早地支持新的标准，并且在实现新的标准时更加严格和一致。
5. 库支持：GCC的库支持更加完善，可以提供更多的功能和更好的性能。但是Clang的库也在不断发展，并且很多库可以直接在Clang上使用。

总体而言，Clang和GCC都是优秀的编译器，选择哪一个取决于具体的情况和需求。例如，对于需要快速编译和具有更好代码质量的项目，Clang可能更合适；而对于需要更广泛的库支持和更高的性能的项目，则可能更适合使用GCC。

# 使用cmake构建（旧）

```bash
curl https://github.com/Kitware/CMake/tree/master/Help/guide/tutorial
git clone https://github.com/Kitware/CMake.git
```

```bash
文件tree(yay -S tree)
.
├── build(此处内容未展示)
├── CMakeLists.txt(需要编写的内容1)
├── cmake_studyConfig.h.in
├── cpp
│   ├── CMakeLists.txt(需要编写的内容2)
│   └── mkt.cpp
├── h(如果只是.h文件不需要添加subdirectory，仅cpp文件需要添加，此处的cmake文件便可以删除)
│   ├── CMakeLists.txt
│   └── mkt.h
├── main.cpp(可执行文件)

```

```cmake
# 需要编写的内容1
cmake_minimum_required(VERSION 3.15)

# set the project name and version
project(cmake_study VERSION 1.0)
# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# add the executable(no label with.)
set(SRC_LIST main.cpp)
add_executable(${PROJECT_NAME} ${SRC_LIST})

# configure a header file to pass some of the CMake settings to the source code
configure_file(cmake_studyConfig.h.in cmake_studyConfig.h)

# add the binary tree to the search path for include files so that we will find xxxConfig.h
add_subdirectory(cpp)
target_link_libraries(${PROJECT_NAME} PUBLIC cpp)

target_include_directories(${PROJECT_NAME} PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           "${PROJECT_SOURCE_DIR}/cpp"
                           )

```

```cmake
# 需要编写的内容2
add_library(cpp mkt.cpp)
```

```C++
//mkt.cpp中需要引入mkt.h
#include"../h/mkt.h"
```

```c
// 在main.cpp中需要引入mkt.h
#include"./h/mkt.h"
```

```c++
//mkt.h的定义
#ifndef MKT_H
#define MKT_H

namespace mkt_Solution{
class Solution{
public:
	Solution();
	void opse();
};
#endif
```

# 如何编写CMakeLists.txt（新）

一个项目的文件树如下：

```bash
.
├── CMakeLists.txt
├── hdtest
│   ├── CMakeLists.txt
│   ├── hdtest.cc
│   └── hdtest.h
└── main.cpp
```

应该如何编写这两个CMakeLists.txt文件呢？

对于你的问题，这两个CMakeLists.txt文件应该这样编写：

在项目根目录下的CMakeLists.txt文件中，你可以添加以下内容：

```cmake
cmake_minimum_required(VERSION 3.10)
project(project_name)
add_subdirectory(hdtest)
add_executable(executable_name main.cpp)
target_link_libraries(executable_name hdtest)
```

在hdtest目录下的CMakeLists.txt文件中，你可以添加以下内容：

```cmake
add_library(hdtest hdtest.cc)
```

这样，在根目录下运行cmake .和make命令就可以生成可执行文件了。

CMake是一个跨平台的构建工具，它可以帮助你管理项目的构建过程。CMakeLists.txt文件是CMake的配置文件，它定义了项目的构建规则。

* 在根目录下的CMakeLists.txt文件中，我们首先指定了CMake的最低版本要求，然后定义了项目名称。

* 接着，我们使用add_subdirectory命令将hdtest目录添加到构建过程中。这意味着CMake会在hdtest目录下寻找CMakeLists.txt文件并执行其中的命令。

* 然后，我们使用add_executable命令定义了一个可执行文件，并指定了它所依赖的源文件。最后，我们使用target_link_libraries命令指定了可执行文件需要链接的库。

* 在hdtest目录下的CMakeLists.txt文件中，我们使用add_library命令定义了一个库，并指定了它所依赖的源文件。

这样，在根目录下运行cmake .命令时，CMake会根据这些配置生成构建脚本。然后运行make命令就可以根据这些脚本构建项目并生成可执行文件了。

```cmake
cmake_minimum_required(VERSION 3.15)
project(tasksuu VERSION 1.0)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED on)

set(SRC_LIST main.cpp)
add_executable(${PROJECT_NAME} ${SRC_LIST})


add_subdirectory(hdtest)
# target_link_libraries(${PROJECT_NAME} PUBLIC hdtest)
target_link_libraries(${PROJECT_NAME} hdtestlib)

# target_include_directories(${PROJECT_NAME} PUBLIC
#                             "${PROJECT_BINARY_DIR}"
#                             "${PROJECT_SOURCE_DIR}/hdtest"
# )
```
```cmake
add_library(hdtestlib hdtest.cc hdtest.h)
target_include_directories(hdtestlib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
```
# make提示重定义？

上面的项目中，hdtest.h被定义如下：

```c++
#ifndef HDTEST_H
#define HDTEST_H
namespace std_hdtest{
    class Solutions{
    public:
        Solutions();
        void print();
        ~Solutions();
    public:
        static void prints();
    };
}
#include"hdtest.cc"
#endif
```

* 在使用cmake和make之后，得到了错误：“错误：‘std_hdtest::Solutions::~Solutions()’ 重定义”。但是如果使用vscode的g++则可以运行，这是为什么呢？

这个错误的原因是在hdtest.h文件中包含了hdtest.cc文件。通常情况下，头文件（.h）中只包含类、函数和变量的声明，而不包含它们的定义。定义应该放在源文件（.cc）中。

当你在hdtest.h文件中包含hdtest.cc文件时，每当hdtest.h被其他文件包含时，hdtest.cc中的内容也会被包含进来。这就导致了重复定义的问题。

你可以尝试删除hdtest.h文件中的#include"hdtest.cc"这一行，然后再次运行cmake和make命令，看看是否能够解决问题。

至于为什么使用vscode的g++可以运行，我无法确定具体原因。可能是你使用g++编译时只编译了main.cpp文件，而没有编译hdtest.cc文件。

之前的回答中提到的“使用vscode的g++可以运行”是一个猜测，我无法确定你实际使用vscode时的具体情况。如果你只编译了main.cpp文件，那么程序应该是无法正常运行的。

通常情况下，当你使用g++编译C++程序时，需要指定所有源文件，例如：

g++ main.cpp hdtest/hdtest.cc -o executable_name
这样，g++会编译所有指定的源文件，并将它们链接在一起生成可执行文件。

而当你使用CMake和Make工具构建项目时，CMake会根据CMakeLists.txt文件中的配置生成构建脚本。这些脚本会指定哪些源文件需要编译和链接。当你运行make命令时，Make工具会根据这些脚本构建项目并生成可执行文件。

总之，不管是使用g++直接编译还是使用CMake和Make工具构建项目，都需要编译所有源文件才能生成可执行文件。

# 如何在vscode中执行C++文件？

需要安装C++扩展套件，系统需要有g++等相关环境，（调试则是gdb）。

```json
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: g++ 生成活动文件", //会输出这个提示，表示正在构建
            "command": "/usr/bin/g++", //环境目录
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "调试器生成的任务。"
        }
    ],
    "version": "2.0.0"
}
```



