---
title: "SearXNG搭建"
description: "nothing else"
image: 'https://cdn.staticaly.com/gh/cutecwc/pucpica/main/y23m3/z63z6s-2.webp'
draft: false
date: 2023-03-17
lastmod: 2023-03-17
categories: ["教程/搭建"]
tags: ["教程/搭建"]
---

应该使用的标记：

```api
https://cdn.staticaly.com/gh/cutecwc/pucpica/main/y23m3/
```

## 一、SearXNG

```markdown
系统：Debian 10（DD脚本 非必需DD用原来的系统也OK，之后教程都是用Debian或者Ubuntu搭建～）
安装好Docker、Docker-compose（相关脚本）
【非必需但建议】域名一枚，并做好解析到服务器上（域名购买、域名解析 视频教程）
【非必需】提前安装好宝塔面板海外版本aapanel，并安装好Nginx（安装地址）
【非必需本教程选用】安装好Nginx Proxy Manager（相关教程）
```

```markdown
服务器要求：不是非常高，能搭建Docker即可，建议1G以上。
```

```bash
# 选择一个目录：（这里选择/usr/local），在此处克隆文件。
cd /usr/local
git clone https://github.com/searxng/searxng-docker.git
# Enter the directory of the file you just cloned。
cd searxng-docker

# ======================
# Edit the '.env' file, which is usually hidden, change the 
# '<email>' and '<host>' to the required values（需要包括'<>' 
# <host> => yoursite.com  <email> => you@mail.com）。
vim .env

# ======================
# 在当前目录（/usr/local/searxng-docker），修改searxng目录下的settings.yml中的一个配置，直接运行这个命令即可。
sed -i "s|ultrasecretkey|$(openssl rand -hex 32)|g" searxng/settings.yml
# 也可以进入这个文件自行填写ultrasecretkey的值（不推荐）
# nano searxng/settings.yml
```

```bash
# ======================
# 在当前目录（/usr/local/searxng-docker）编辑这个文件（docker-compose.yaml）
vim docker-compose.yaml
# Delete all the 'Caddy' parts. (You can optionally comment 
# it out using '#')
# 修改searxgn:选项下的'posts:'
` posts: 
` 		"127.0.0.1:8080:8080" #(before)
`		"127.0.0.1:7890:8080" #(after, while '7890' can revise to anyone port as you like.)

# ======================
# Your server usually has a BT panel. 使用宝塔面板Nginx反代。
# Then use BT-Penal to add anti-generation configuration, 
# the target URL is 'http://127.0.0.1:7890' , if the port is 
# modified above, replace 7890 with the modified port, and 
# finally submit.
# as the picture shows：
```

![](https://cdn.staticaly.com/gh/cutecwc/pucpica/main/y23m3/f63ecc05ea494a0e83c8cf55f40df6f8.png)

在下图所示出编辑配置：

![](https://cdn.staticaly.com/gh/cutecwc/pucpica/main/y23m3/41bc38b517deeab4566797958b4664e0.png)

```nginx
# Comment or delete all the content of the original 
# 'location / {}', fill in the content here, here 7890 needs to 
# be modified to the port value you set.
location / {
    proxy_pass http://127.0.0.1:7890;
    proxy_set_header Host $host;
    proxy_set_header Connection       $http_connection;
    proxy_set_header X-Forwarded-For  $proxy_add_x_forwarded_for;
    proxy_set_header X-Scheme         $scheme;
    proxy_buffering                   off;
}
```

最后点击保存。

```bash
# ======================
# 在当前目录（/usr/local/searxng-docker）运行docker脚本
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
# 设置开机启动，并且立即运行
systemctl enable docker
systemctl start docker

# ======================
# 在当前目录（/usr/local/searxng-docker）拉取docker-compose，并将其放置在/usr/local/bin/docker-compose。
curl -SL "https://github.com/docker/compose/releases/download/v2.6.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# 为docker-compose赋予运行条件，并加入系统环境（root）
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# ======================
# 防火墙允许（ufw自行放通目标端口-7890-'the port you set before'）
firewall-cmd --zone=public --add-port=7890/tcp --permanent
firewall-cmd --reload

# ======================
# 在当前目录（/usr/local/searxng-docker）执行
sudo docker-compose up
# 试试是否可以访问了（broswer-> host）(Before this, you should 
# have set up the DNS resolution service. If not, go back to 
# your domain name service provider and modify this)

# 如果没有问题（正常访问），就可以Ctrl-C服务，并启动这个程序的守护进程。
sudo docker-compose up -d
# --关闭终端
```

```markdown
更多：
是否会自动启动？
是否可以定制这个网站？
```

