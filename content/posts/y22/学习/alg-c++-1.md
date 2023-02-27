---
title: algo-二分查找
description: "C/C++"
image: '/images/post/y22_trans/104354054_p0.jpg'
date: 2022-12-15
categories:
- algo-c++
tags:
- algo-c++
---



### 一、数组特性

* 地址从零开始计数

* 数组中全是相同类型的元素

* 元素只能覆盖不能删除

* 地址是连续的（逻辑）

### 二、二分查找

#### 1、理论提出

**适用情况**：对于已经有序数组，采用二分查找寻找组内元素。

> **闭区间**：设置left为头right为尾（`left=0`,`right=size-1`），`while(left<=right)`，设置`mid`为`(1/2)*(left+right)`，更新为`left=mid+1`或`right=mid-1`。

> **开区间**：设置left为头right为尾（`left=0`,`right=size`）,`while(left<right)`，设置`mid`为`left+((left+right)>>1)`，更新为`left=mid+1`或`right=mid`。

```markdown
问：C++中(b - a) >> 1是什么意思？
答：In C++, the expression (b - a) >> 1 is a bit shift operation. The operator ">>" shifts the bits of the value on its left side to the right by the number of positions specified on its right side. In this case, the value being shifted is (b - a), which calculates the difference between b and a.

The meaning of this expression is that it divides the difference between b and a by 2. By shifting the bits of (b - a) to the right by 1 position, the result is the same as dividing the value by 2. This is because shifting the bits to the right by 1 position is equivalent to dividing the value by 2^1 (which is 2). This is a faster way to divide a number by 2 than doing a division operation.

So, (b - a) >> 1 will return the middle value of range [a, b] if b>a, otherwise it will return 0.
QAQ：摘要，>>是一个更快捷的除以二的方式，是逻辑右移。
```

```markdown
时间复杂度：logn
空间复杂度：1
```

```markdown
推荐：704，35，69，367
```

#### 2、详细代码

二分查找，又称折半查找，是一种在有序数组中查找某一特定元素的搜索算法。它的基本思想是将数组分成三部分，其中一部分的元素都比要查找的元素小，另一部分的元素都比要查找的元素大，剩下部分则是要查找的元素。

C++代码实现二分查找的示例如下：

```c++
#include <iostream>
#include <vector>

int binarySearch(std::vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int main() {
    std::vector<int> nums = {1, 3, 5, 7, 9};
    int target = 5;
    int result = binarySearch(nums, target);
    if (result != -1) {
        std::cout << "Target " << target << " found at index " << result << std::endl;
    } else {
        std::cout << "Target " << target << " not found in the array" << std::endl;
    }
    return 0
}

```

这里附上教程里的代码（两个版本以提供比较分析）

```c++
#include<iostream>
#include<vector>
using namespace std;

// 版本一
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1; // 定义target在左闭右闭的区间里，[left, right]
        while (left <= right) { // 当left==right，区间[left, right]依然有效，所以用 <=
            int middle = left + ((right - left) / 2);// 防止溢出 等同于(left + right)/2
            if (nums[middle] > target) {
                right = middle - 1; // target 在左区间，所以[left, middle - 1]
            } else if (nums[middle] < target) {
                left = middle + 1; // target 在右区间，所以[middle + 1, right]
            } else { // nums[middle] == target
                return middle; // 数组中找到目标值，直接返回下标
            }
        }
        // 未找到目标值
        return -1;
    }
};

```

```c++
#include<iostream>
#include<vector>
using namespace std;

// 版本二
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size(); // 定义target在左闭右开的区间里，即：[left, right)
        while (left < right) { // 因为left == right的时候，在[left, right)是无效的空间，所以使用 <
            int middle = left + ((right - left) >> 1);
            if (nums[middle] > target) {
                right = middle; // target 在左区间，在[left, middle)中
            } else if (nums[middle] < target) {
                left = middle + 1; // target 在右区间，在[middle + 1, right)中
            } else { // nums[middle] == target
                return middle; // 数组中找到目标值，直接返回下标
            }
        }
        // 未找到目标值
        return -1;
    }
};

```



#### 3、相似题目

> 在第29题中，函数被如下定义，可以发现采用的是第二种方式。

```c++
#include<iostream>
#include<vector>
using namespace std;

int Solution::mySqrt(int x){
    if(0 == x){
        return 0;
    }else if(1==x){
        return 1;
    }else{
        int tail = x/2;
        int head = 1;
        int mid = 0;
        while(head < tail){
            mid = head + ((tail - head + 1)/2);
            if(mid>x/mid){
                tail = mid -1;
            }
            else{
                head = mid;
            }
        }
        return tail;
    }
}

```

```C++
int a =3,b=7;
int c1 = (1/2)* (a+b);
int c2 = a + ((b - a)>>1);
其中c1与c2所表示的含义有什么区别？
```

