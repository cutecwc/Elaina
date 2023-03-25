---
title: "在服务器搭建个人应用"
description: "nothing else"
image: ''
draft: true
date: 2023-02-13
lastmod: 2023-02-14
categories: ["发现"]
tags: ["教程/搭建"]
---



写在前面：本内容仅个人学习搭建和测试使用服务器中的应用..。

# 一、第一部分

## 1、介绍

V2Ray由两个部分组成，一个是**V2Ray服务器**，或称**节点**，一个是**V2Ray客户端应用**（app）。V2Ray服务器是远程的位于那些互联网自由开放的国家的服务器，服务器上安装和运行有V2Ray的程序，可供客户端连接使用；V2Ray客户端是安装在手机或电脑等设备上的软件，使用这个软件可以将设备连接到V2Ray服务器。两者的工作原理是，在用户上网的同时，客户端会在后台发送网站访问请求给服务器处理，由于服务器所在的国家没有互联网限制，它可以正常获取那些在用户所在地被屏蔽的网络内容，获取之后将这些信息传到用户的设备上，从而用户自己的手机或电脑就能够突破限制正常访问那些网站。

## 2、平台选择

在搭建V2Ray服务器前先要有一个远程服务器，这个服务器通常是租用，比如国内的阿里云、腾讯云、华为云等（20元/月左右-极低配），国外的美国的[Vultr](https://www.vultr.com/?ref=9086219)、[DigitalOcean](https://thetowerinfo.com/go/digitalocean)和加拿大的[搬瓦工](https://bwh81.net/aff.php?aff=68661)，每月5美元（约35元-比较符合）。Vultr和搬瓦工都支持支付宝；DigitalOcean的最低价格的服务器是6美元/月，而Vultr同样配置的服务器是5美元/月。搬瓦工价格更低，差不多是4美元/月，但只能按年付。

## 3、套餐选择

由于这个服务器还需要测试其它应用，则选择$5的套餐(1vCPU+1GBMemory+1TBBandwidth ps：0.5TB其实也差不多了)，如果仅仅为搭建这个应用，可选$3.5套餐。

## 4、主要设置

Image可以选择很多系统，可以选一款熟悉的（如`archlinux`(bushi)）。

也可以通过选择应用来初始化一个系统，这个系统会自动预装这些个软件（如wordpress）。

如果不需要安装其他应用，选择`centos` `ubuntu` `debian`都可以。

`Add auto backups`：如果没有重要数据，可以不开启（开启要加钱）。

`Additional features`：可以启用IPv6支持，其它默认即可。

`Server hostname & label`：为主机赋予名字和标签。

然后接下去就可以点击页面右下角的蓝色的“Deploy Now”按钮创建服务器了。然后等待十几秒种到几分钟时间让服务器完成创建。
等服务器创建完成后，屏幕会跳转到一个新的页面，显示已创建的服务器。

## 5、连接服务器

可以不用ssh（控制面板中有终端可以打开，不过有点卡），如果需要可以使用：

```bash
ssh root@your_server_ip #后面是服务器IP
```

密码有关信息都可以在控制面板中看到。

安装必要程序(root)：

```bash
apt-get update -y && apt-get install curl -y #ubuntu或Debian
yum update -y && yum install curl -y #CentOS系统
```

## 6、安装服务

```bash
bash <(curl -L -s https://install.direct/go.sh) #使用脚本自动化安装
bash <(curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh)#这两个命令二选一，官网给的是第一个，但是第二个也执行成功了QAQ
#将上面命令输入后按回车，V2Ray就开始安装了，然后等待十几秒至几十秒时间后，V2Ray就安装完成了。一般不会出现问题，因为本来就是国外环境的主机，无所谓无法访问的问题。
```

--==以下是一些文件的内容，不是需要执行的命令。==--

```bash
#!/usr/bin/env bash

# This file is accessible as https://install.direct/go.sh
# Original source is located at github.com/v2fly/v2ray-core/release/install-release.sh

# If not specify, default meaning of return value:
# 0: Success
# 1: System error
# 2: Application error
# 3: Network error

#######color code########
RED="31m"      # Error message
YELLOW="33m"   # Warning message
colorEcho(){
    echo -e "\033[${1}${@:2}\033[0m" 1>& 2
}

colorEcho ${RED} "ERROR: This script has been DISCARDED, please switch to fhs-install-v2ray project."
colorEcho ${YELLOW} "HOW TO USE: https://github.com/v2fly/fhs-install-v2ray"
colorEcho ${YELLOW} "TO MIGRATE: https://github.com/v2fly/fhs-install-v2ray/wiki/Migrate-from-the-old-script-to-this"
exit 255
```

此脚本会自动安装以下文件：

- `/usr/bin/v2ray/v2ray`：V2Ray 程序；
- `/usr/bin/v2ray/v2ctl`：V2Ray 工具；
- `/etc/v2ray/config.json`：配置文件；
- `/usr/bin/v2ray/geoip.dat`：IP 数据文件
- `/usr/bin/v2ray/geosite.dat`：域名数据文件

此脚本会配置自动运行脚本。自动运行脚本会在系统重启之后，自动运行 V2Ray。目前自动运行脚本只支持带有 Systemd 的系统，以及 Debian / Ubuntu 全系列。

运行脚本位于系统的以下位置：

- `/etc/systemd/system/v2ray.service`: Systemd
- `/etc/init.d/v2ray`: SysV

脚本运行完成后，你需要：

1. 编辑 /etc/v2ray/config.json 文件来配置你需要的代理方式；
2. 运行 service v2ray start 来启动 V2Ray 进程；
3. 之后可以使用 service v2ray start|stop|status|reload|restart|force-reload 控制 V2Ray 的运行。

--==以上是一些文件的内容，不是需要执行的命令。==--

## 7、配置服务

首先，配置文件里需要用户ID，所以在创建配置文件前我们需要先获取一个用户ID，用户ID需要符合特定的UUID 格式，可以去一些UUID号生成网站生成一个使用，可搜索online UUID generator找这样的网站。另外更方便的方法是在命令行界面里使用指令生成，使用下面的命令就会生成一个用户ID。

```bash
cat /proc/sys/kernel/random/uuid
```

生成id后要记下来，在下一步和使用客户端时都要用到。可以选中id后按Ctrl+Shift+C复制，然后粘贴到记事本或其他地方。

然后我们用Vi编辑器创建和编辑V2Ray的配置文件，使用如下命令：

```bash
vi /usr/local/etc/v2ray/config.json
```

回车后界面会切换到文件里去，里面几乎是空白的，只有两个大括号。然后按键盘上的“i”键进入编辑模式开始编辑。先用“delete”键把两个大括号删掉，再复制以下文本到文件里：

```json
{
  "inbounds": [
    {
      "port": 16832, // 服务器端口，不需要变更，除非有已知的冲突
      "protocol": "vmess", //使用软件时选择的类型
      "settings": {
        "clients": [
          {
            "id": "b831381d-6324-4d53-ad4f-8cda68b30851",  // 用户 ID刚刚记下来的那串数字，不记得可以再次执行 cat /proc/sys/kernel/random/uuid，
            "alterId": 0
          }
        ]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",  
      "settings": {}
    }
  ]
}
```

配置文件里值得注意和需要记下来的几个参数是**用户ID**，**服务器端口**，**alterID**，这些都要在使用V2Ray客户端时输入。你可以自行修改设置一个port（服务器端口）。alterID不必更改。

然后按esc退出编辑，输入`:wq`保存退出。

接下去就可以启动V2Ray使用了，启动V2Ray的方法是使用以下指令。

```bash
systemctl start v2ray #启动服务
systemctl restart v2ray # 以后如果你修改了配置文件，在修改完退出配置文件后需要运行以下命令重启V2Ray，这样才能使做的修改生效。
```

## 8、附加操作

```markdown
系统支持：CentOS 6+，Debian 8+，Ubuntu 16+
虚拟技术：OpenVZ 以外的，比如 KVM、Xen、VMware
内存要求：≥128M
日期　　：2022 年 5 月 11 日
1、本脚本已在 Vultr 上的 VPS 全部测试通过。
2、当脚本检测到 VPS 的虚拟方式为 OpenVZ 时，会提示错误，并自动退出安装。
3、脚本运行完重启发现开不了机的，打开 VPS 后台控制面板的 VNC, 开机卡在 grub 引导, 手动选择内核即可。
4、由于是使用最新版系统内核，最好请勿在生产环境安装，以免产生不可预测之后果。
```

Google 开源了其 TCP BBR 拥塞控制算法，并提交到了 Linux 内核，从 4.9 开始，Linux 内核已经用上了该算法。根据以往的传统，Google 总是先在自家的生产环境上线运用后，才会将代码开源，此次也不例外。
根据实地测试，在部署了最新版内核并开启了 TCP BBR 的机器上，网速甚至可以提升好几个数量级。
于是我根据目前三大发行版的最新内核，开发了一键安装最新内核并开启 TCP BBR 脚本。

我们通过安装Google BBR拥堵控制算法来为V2Ray服务器加速，Google BBR是谷歌开发的一个TCP拥堵控制算法，它可以大大提升V2Ray服务器的速度。我们可以采用[Github用户Teddysun的脚本](https://teddysun.com/489.html)来安装Google BBR，方法是运行以下指令。

```bash
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && ./bbr.sh
```

运行该指令后，要按任意键（如回车）才能开始脚本的安装。安装只要几秒钟时间就能完成。完成后再次用以下命令重启V2Ray。

```bash
systemctl restart v2ray
```

到此V2Ray的安装、设置和优化就全部完成了，接下来的一步就是在手机或电脑上下载安装V2Ray客户端。

## 9、使用服务

到此V2Ray的安装、设置和优化就全部完成了，接下来的一步就是在手机或电脑上下载安装V2Ray客户端。

### 安卓：

安卓用户需要安装的V2Ray客户端名为**V2RayNG**，可以在Github上下载（[点击此处](https://github.com/2dust/v2rayNG/releases/)前往下载页面），当然如果手机安装有Google Play服务也可以在Google Play商店上下载。

### 苹果：

苹果用户可以安装的客户端应用是**Shadowrocket**、**ShadowRay**、**Kitsunebi**或**Pepi**，都是原本专为影梭设计的应用，但现在也支持V2Ray。Shadowrocket是付费应用，但性能更好。注意你需要用海外iTunes账号才可以在App Store上搜索到这些应用，因为中国版的App Store上所有VPN和类似应用都已经下架。

### Windows：

以下是电脑上使用的V2Ray客户端，都是在Github上下载：
Windows系统：[**V2RayN**](https://github.com/2dust/v2rayN/releases) （进入下载页面后，选择“v2rayN-Core.zip”下载，解压后打开里面的“v2rayN.exe”即可运行客户端）

### Mac：

Mac系统：[**V2RayX**](https://github.com/Cenmrev/V2RayX/releases/)

### Linux：

略，看Github。



这里简单介绍一下**V2Ray安卓客户端应用程序V2RayNG**的使用方法。打开客户端点击右上方的加号，在出现的下拉列表中选择“手动输入[Vmess]”，然后找到相应区域输入别名（remark，任意名称均可）、服务器IP地址（address）和之前记下的显示在V2Ray配置文件中的几项参数（Port，ID，alterID），还有一项是Security，是选择加密方式，可以自己在下拉列表中选择，和配置文件中的设置无关，建议选择“Chacha20-poly1305”。输入完成后点击右上方的勾号确定，再点击右下方的连接按钮就可以连接到服务器了。

使用**Windows的V2RayN**时只要添加服务器（选择Vmess服务器），输入各项信息确定后就会自动连接。注意还要设置系统代理，方法是在Windows的任务栏找到V2RayN的小图标，鼠标右击，在出现的菜单中找到“系统代理”，然后选择“自动配置系统代理”。

其他操作系统的客户端的用法也类似，都是输入服务器IP和配置文件里的几项信息然后连接。连接之后就可以离开应用让它在后台运行，去访问那些正常情况下因为互联网限制不能访问的网站。

V2Ray有两种代理模式，有**全局模式**，和**PAC模式**，如果平时多用中国以外的网站，那么可以选用全局模式，如果平时会经常用到中国网站，如优酷，QQ音乐等，这些网站的服务只针对中国内的用户开放，这时应该采用PAC模式，让这些没被限制的网站不受V2Ray影响。



clash for windows（三个平台都可用）--以下是未经实践的理论修改：

CFW 启动的过程会使用到两个配置文件，分别是：

- `Home Directory/config.yaml`
- `Home Directory/profiles/xxxx.yaml`

`config.yaml`是由软件自动维护的，不需要更改什么。

`profiles/xxxx.yaml`可以自行建立（名字自取），参考以下设置键值：

```yaml
# Port of HTTP(S) proxy server on the local end
port: 7890

# Port of SOCKS5 proxy server on the local end
socks-port: 7891

# Transparent proxy server port for Linux and macOS (Redirect TCP and TProxy UDP)
# redir-port: 7892

# Transparent proxy server port for Linux (TProxy TCP and TProxy UDP)
# tproxy-port: 7893

# HTTP(S) and SOCKS4(A)/SOCKS5 server on the same port
# mixed-port: 7890

# authentication of local SOCKS5/HTTP(S) server
# authentication:
#  - "user1:pass1"
#  - "user2:pass2"

# Set to true to allow connections to the local-end server from
# other LAN IP addresses
# allow-lan: false

# This is only applicable when `allow-lan` is `true`
# '*': bind all IP addresses
# 192.168.122.11: bind a single IPv4 address
# "[aaaa::a8aa:ff:fe09:57d8]": bind a single IPv6 address
# bind-address: '*'

# Clash router working mode
# rule: rule-based packet routing
# global: all packets will be forwarded to a single endpoint
# direct: directly forward the packets to the Internet
mode: rule

# Clash by default prints logs to STDOUT
# info / warning / error / debug / silent
# log-level: info

# When set to false, resolver won't translate hostnames to IPv6 addresses
# ipv6: false

# RESTful web API listening address
external-controller: 127.0.0.1:9090

# A relative path to the configuration directory or an absolute path to a
# directory in which you put some static web resource. Clash core will then
# serve it at `http://{{external-controller}}/ui`.
# external-ui: folder

# Secret for the RESTful API (optional)
# Authenticate by spedifying HTTP header `Authorization: Bearer ${secret}`
# ALWAYS set a secret if RESTful API is listening on 0.0.0.0
# secret: ""

# Outbound interface name
# interface-name: en0

# fwmark on Linux only
# routing-mark: 6666

# Static hosts for DNS server and connection establishment (like /etc/hosts)
#
# Wildcard hostnames are supported (e.g. *.clash.dev, *.foo.*.example.com)
# Non-wildcard domain names have a higher priority than wildcard domain names
# e.g. foo.example.com > *.example.com > .example.com
# P.S. +.foo.com equals to .foo.com and foo.com
hosts:
  # '*.clash.dev': 127.0.0.1
  # '.dev': 127.0.0.1
  # 'alpha.clash.dev': '::1'

profile:
  # Store the `select` results in $HOME/.config/clash/.cache
  # set false If you don't want this behavior
  # when two different configurations have groups with the same name, the selected values are shared
  store-selected: false

  # persistence fakeip
  store-fake-ip: true

# DNS server settings
# This section is optional. When not present, the DNS server will be disabled.
dns:
  enable: false
  listen: 0.0.0.0:53
  # ipv6: false # when the false, response to AAAA questions will be empty

  # These nameservers are used to resolve the DNS nameserver hostnames below.
  # Specify IP addresses only
  default-nameserver:
    - 114.114.114.114
    - 8.8.8.8
  enhanced-mode: fake-ip # or redir-host (not recommended)
  fake-ip-range: 198.18.0.1/16 # Fake IP addresses pool CIDR
  # use-hosts: true # lookup hosts and return IP record
  
  # Hostnames in this list will not be resolved with fake IPs
  # i.e. questions to these domain names will always be answered with their
  # real IP addresses
  # fake-ip-filter:
  #   - '*.lan'
  #   - localhost.ptlogin2.qq.com
  
  # Supports UDP, TCP, DoT, DoH. You can specify the port to connect to.
  # All DNS questions are sent directly to the nameserver, without proxies
  # involved. Clash answers the DNS question with the first result gathered.
  nameserver:
    - 114.114.114.114 # default value
    - 8.8.8.8 # default value
    - tls://dns.rubyfish.cn:853 # DNS over TLS
    - https://1.1.1.1/dns-query # DNS over HTTPS
    - dhcp://en0 # dns from dhcp
    # - '8.8.8.8#en0'

  # When `fallback` is present, the DNS server will send concurrent requests
  # to the servers in this section along with servers in `nameservers`.
  # The answers from fallback servers are used when the GEOIP country
  # is not `CN`.
  # fallback:
  #   - tcp://1.1.1.1
  #   - 'tcp://1.1.1.1#en0'

  # If IP addresses resolved with servers in `nameservers` are in the specified
  # subnets below, they are considered invalid and results from `fallback`
  # servers are used instead.
  #
  # IP address resolved with servers in `nameserver` is used when
  # `fallback-filter.geoip` is true and when GEOIP of the IP address is `CN`.
  #
  # If `fallback-filter.geoip` is false, results from `nameserver` nameservers
  # are always used if not match `fallback-filter.ipcidr`.
  #
  # This is a countermeasure against DNS pollution attacks.
  # fallback-filter:
  #   geoip: true
  #   geoip-code: CN
  #   ipcidr:
  #     - 240.0.0.0/4
  #   domain:
  #     - '+.google.com'
  #     - '+.facebook.com'
  #     - '+.youtube.com'
  
  # Lookup domains via specific nameservers
  # nameserver-policy:
  #   'www.baidu.com': '114.114.114.114'
  #   '+.internal.crop.com': '10.0.0.1'

proxies:
  # Shadowsocks
  # The supported ciphers (encryption methods):
  #   aes-128-gcm aes-192-gcm aes-256-gcm
  #   aes-128-cfb aes-192-cfb aes-256-cfb
  #   aes-128-ctr aes-192-ctr aes-256-ctr
  #   rc4-md5 chacha20-ietf xchacha20
  #   chacha20-ietf-poly1305 xchacha20-ietf-poly1305
  - name: "ss1"
    type: ss
    server: server
    port: 443
    cipher: chacha20-ietf-poly1305
    password: "password"
    # udp: true

  - name: "ss2"
    type: ss
    server: server
    port: 443
    cipher: chacha20-ietf-poly1305
    password: "password"
    plugin: obfs
    plugin-opts:
      mode: tls # or http
      # host: bing.com

  - name: "ss3"
    type: ss
    server: server
    port: 443
    cipher: chacha20-ietf-poly1305
    password: "password"
    plugin: v2ray-plugin
    plugin-opts:
      mode: websocket # no QUIC now
      # tls: true # wss
      # skip-cert-verify: true
      # host: bing.com
      # path: "/"
      # mux: true
      # headers:
      #   custom: value

  # vmess
  # cipher support auto/aes-128-gcm/chacha20-poly1305/none
  - name: "vmess"
    type: vmess
    server: server
    port: 443
    uuid: uuid
    alterId: 32
    cipher: auto
    # udp: true
    # tls: true
    # skip-cert-verify: true
    # servername: example.com # priority over wss host
    # network: ws
    # ws-opts:
    #   path: /path
    #   headers:
    #     Host: v2ray.com
    #   max-early-data: 2048
    #   early-data-header-name: Sec-WebSocket-Protocol

  - name: "vmess-h2"
    type: vmess
    server: server
    port: 443
    uuid: uuid
    alterId: 32
    cipher: auto
    network: h2
    tls: true
    h2-opts:
      host:
        - http.example.com
        - http-alt.example.com
      path: /
  
  - name: "vmess-http"
    type: vmess
    server: server
    port: 443
    uuid: uuid
    alterId: 32
    cipher: auto
    # udp: true
    # network: http
    # http-opts:
    #   # method: "GET"
    #   # path:
    #   #   - '/'
    #   #   - '/video'
    #   # headers:
    #   #   Connection:
    #   #     - keep-alive

  - name: vmess-grpc
    server: server
    port: 443
    type: vmess
    uuid: uuid
    alterId: 32
    cipher: auto
    network: grpc
    tls: true
    servername: example.com
    # skip-cert-verify: true
    grpc-opts:
      grpc-service-name: "example"

  # socks5
  - name: "socks"
    type: socks5
    server: server
    port: 443
    # username: username
    # password: password
    # tls: true
    # skip-cert-verify: true
    # udp: true

  # http
  - name: "http"
    type: http
    server: server
    port: 443
    # username: username
    # password: password
    # tls: true # https
    # skip-cert-verify: true
    # sni: custom.com

  # Snell
  # Beware that there's currently no UDP support yet
  - name: "snell"
    type: snell
    server: server
    port: 44046
    psk: yourpsk
    # version: 2
    # obfs-opts:
      # mode: http # or tls
      # host: bing.com

  # Trojan
  - name: "trojan"
    type: trojan
    server: server
    port: 443
    password: yourpsk
    # udp: true
    # sni: example.com # aka server name
    # alpn:
    #   - h2
    #   - http/1.1
    # skip-cert-verify: true

  - name: trojan-grpc
    server: server
    port: 443
    type: trojan
    password: "example"
    network: grpc
    sni: example.com
    # skip-cert-verify: true
    udp: true
    grpc-opts:
      grpc-service-name: "example"

  - name: trojan-ws
    server: server
    port: 443
    type: trojan
    password: "example"
    network: ws
    sni: example.com
    # skip-cert-verify: true
    udp: true
    # ws-opts:
      # path: /path
      # headers:
      #   Host: example.com

  # ShadowsocksR
  # The supported ciphers (encryption methods): all stream ciphers in ss
  # The supported obfses:
  #   plain http_simple http_post
  #   random_head tls1.2_ticket_auth tls1.2_ticket_fastauth
  # The supported supported protocols:
  #   origin auth_sha1_v4 auth_aes128_md5
  #   auth_aes128_sha1 auth_chain_a auth_chain_b  
  - name: "ssr"
    type: ssr
    server: server
    port: 443
    cipher: chacha20-ietf
    password: "password"
    obfs: tls1.2_ticket_auth
    protocol: auth_sha1_v4
    # obfs-param: domain.tld
    # protocol-param: "#"
    # udp: true

proxy-groups:
  # relay chains the proxies. proxies shall not contain a relay. No UDP support.
  # Traffic: clash <-> http <-> vmess <-> ss1 <-> ss2 <-> Internet
  - name: "relay"
    type: relay
    proxies:
      - http
      - vmess
      - ss1
      - ss2

  # url-test select which proxy will be used by benchmarking speed to a URL.
  - name: "auto"
    type: url-test
    proxies:
      - ss1
      - ss2
      - vmess1
    # tolerance: 150
    # lazy: true
    url: 'http://www.gstatic.com/generate_204'
    interval: 300

  # fallback selects an available policy by priority. The availability is tested by accessing an URL, just like an auto url-test group.
  - name: "fallback-auto"
    type: fallback
    proxies:
      - ss1
      - ss2
      - vmess1
    url: 'http://www.gstatic.com/generate_204'
    interval: 300

  # load-balance: The request of the same eTLD+1 will be dial to the same proxy.
  - name: "load-balance"
    type: load-balance
    proxies:
      - ss1
      - ss2
      - vmess1
    url: 'http://www.gstatic.com/generate_204'
    interval: 300
    # strategy: consistent-hashing # or round-robin

  # select is used for selecting proxy or proxy group
  # you can use RESTful API to switch proxy is recommended for use in GUI.
  - name: Proxy
    type: select
    # disable-udp: true
    proxies:
      - ss1
      - ss2
      - vmess1
      - auto
 
  # direct to another infacename or fwmark, also supported on proxy
  - name: en1
    type: select
    interface-name: en1
    routing-mark: 6667
    proxies:
      - DIRECT 

  - name: UseProvider
    type: select
    use:
      - provider1
    proxies:
      - Proxy
      - DIRECT

proxy-providers:
  provider1:
    type: http
    url: "url"
    interval: 3600
    path: ./provider1.yaml
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
  test:
    type: file
    path: /test.yaml
    health-check:
      enable: true
      interval: 36000
      url: http://www.gstatic.com/generate_204

tunnels:
  # one line config
  - tcp/udp,127.0.0.1:6553,114.114.114.114:53,proxy
  - tcp,127.0.0.1:6666,rds.mysql.com:3306,vpn
  # full yaml config
  - network: [tcp, udp]
    address: 127.0.0.1:7777
    target: target.com
    proxy: proxy

rules:
  - DOMAIN-SUFFIX,google.com,auto
  - DOMAIN-KEYWORD,google,auto
  - DOMAIN,google.com,auto
  - DOMAIN-SUFFIX,ad.com,REJECT
  - SRC-IP-CIDR,192.168.1.201/32,DIRECT
  # optional param "no-resolve" for IP rules (GEOIP, IP-CIDR, IP-CIDR6)
  - IP-CIDR,127.0.0.0/8,DIRECT
  - GEOIP,CN,DIRECT
  - DST-PORT,80,DIRECT
  - SRC-PORT,7777,DIRECT
  - RULE-SET,apple,REJECT # Premium only
  - MATCH,auto
```

此处给出了示例文件：

```yaml
mixed-port: 7890
allow-lan: true
bind-address: '*'
mode: global
ipv6: true
log-level: info
external-controller: '127.0.0.1:9090'
dns:
    enable: true
    ipv6: true
    nameserver: [223.5.5.5, 119.29.29.29, 8.8.8.8]
    enhanced-mode: redir-host
    fake-ip-range: 198.18.0.1/16
    use-hosts: true
    fallback-filter: { geoip: true, ipcidr: [240.0.0.0/4, 0.0.0.0/32] }
proxies:
    - { name: 'my proxy (括号删除，server为自己的服务器IP)', type: vmess, server: 1.1.1.1, port: 16832, uuid: b831381d-6324-4d53-ad4f-8cda68b30851, alterId: 0, cipher: auto, udp: true }
```

## 0、维护

V2Ray服务器可能会在某一天被屏蔽，如果你发现你的V2Ray连不上了，很可能就是服务器被屏蔽导致的。通常情况下受影响的只是端口，只需要像搭建V2Ray服务器的时候一样编辑配置文件，将文件里的端口号换掉，如你原来的端口是16832，那改成16833即可，修改完成后要记得重启V2Ray。

更糟糕的：IP被屏蔽了，需要重新搭建这样一个服务器，以此来刷新IP。（或许有其它办法，暂时未知...）

如何确定是否被和谐？

直接输入IP看是否可以访问？是否可以ping通？

--排查：

```bash
#进入服务器终端，查看防火墙状态（如果有，一般有-firewalld or ufw-以ufw为例）：
# apt-get install ufw #安装防火墙（不需要执行这条）
# sudo apt remove ufw -y #卸载防火墙
# ufw enable|disable #开启|关闭防火墙
# ufw default deny #配置访问控制列表
# ufw allow proto udp 192.168.0.1 port 53 to 192.168.0.2 port 53 #样式
# ufw allow from 192.168.1.1 #仅允许来自**的访问
# ufw deny 端口号 
# ufw allow 端口号 
# ufw delete 端口号 
# systemctl stop ufw #临时停用防火墙
ufw status
ufw allow 9080
ufw allow 16832
ufw status #再次检查是否开启，等一会看看是否可以访问
#取消允许：

```

## -1、参考文件

```bash
#主要
curl https://thetowerinfo.com/zh/v2ray-tutorial/  #搭建部分
curl https://teddysun.com/489.html #加速服务部分
#参考资料
curl https://www.v2ray.com/chapter_00/install.html #v2ray官网安装说明
curl https://www.v2ray.com/chapter_02/01_overview.html #v2ray官网配置文件说明
curl https://docs.cfw.lbyczf.com/contents/configfile.html#%E6%A0%BC%E5%BC%8F #cfw的官网配置文件说明
curl https://github.com/Dreamacro/clash/wiki/configuration #cfw的官网配置文件说明
#推荐阅读
curl https://thetowerinfo.com/zh/create-minecraft-server-tutorial/ #我的世界服务器
curl https://thetowerinfo.com/zh/bandwagonhost-deploy-server-tutorial/ #搬瓦工的服务器如何配置？
curl https://thetowerinfo.com/zh/digitalocean-deploy-server-tutorial/ #DigitalOcean服务器
#自动安装脚本-1-来自https://vmessnode.xyz/centos-one-click-install-v2ray/
bash <(curl -sL https://s.hijk.art/v2ray.sh)
#
```

