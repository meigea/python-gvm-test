```
vim /etc/selinux/config

# 修改参数：
# SELINUX=disabled

# 更新：
# yum -y update

重启：
# reboot

# 安装依赖：
yum install -y wget bzip2 texlive net-tools alien gnutls-utils

# 添加仓库：
wget -q -O - https://www.atomicorp.com/installers/atomic | sh

# 安装：
yum install openvas -y

# 编辑文件：
# vim /etc/redis.conf
# 修改配置：
# unixsocket /tmp/redis.sock
# unixsocketperm 700

# 重启redis：
# systemctl enable redis && systemctl restart redis

# 启动openvas初始环境配置：
openvas-setup

# 防火墙放行端口：
# firewall-cmd --permanent --add-port=9392/tcp
# firewall-cmd --reload
# firewall-cmd --list-port

# 访问登录：
# https://本机IP:9392

# 验证完整性以及运行的可靠性：
openvas-check-setup --v9

# 据部分用户反馈可能出现一些故障，临时解决办法，但我没遇到：
# yum -y install texlive-changepage texlive-titlesec
# mkdir -p /usr/share/texlive/texmf-local/tex/latex/comment
# cd /usr/share/texlive/texmf-local/tex/latex/comment
#wget http://mirrors.ctan.org/macros/latex/contrib/comment/comment.sty
# chmod 644 comment.sty
# texhash​
```

## 也许不用
```
openvas-nvt-sync
openvassd
## https://github.com/greenbone/ospd/blob/master/doc/INSTALL-ospd-scanner.md
openvasmd --rebuild
openvasmd --backup
openvasmd -p 9390 -a 127.0.0.1
# openvasad -a 127.0.0.1 -p 9393
# gsad --http-only --listen=127.0.0.1 -p 9392
gsad  --listen=0.0.0.0 -p 9392
```