---
title: Cookie与Session的区别
date: 2019-03-30 14:05:56
tags: 
- Cookie
- Session
categories: 
- 网络编程
---

[本文转自此处](https://baijiahao.baidu.com/s?id=1619095369231494766&wfr=spider&for=pc)

## Cookie ##

位于用户的计算机上，用来维护用户计算机中的信息，直到用户删除。

比如我们在网页上登录某个软件时输入用户名及密码时如果保存为cookie，则每次我们访问的时候就不需要登录网站了。

我们可以在浏览器上保存任何文本，而且我们还可以随时随地的去阻止它或者删除。

我们同样也可以禁用或者编辑cookie，但是有一点需要注意不要使用cookie来存储一些隐私数据，以防隐私泄露。

Cookie可能被用户禁用。

替代方案：URL参数，form表单的隐藏与，localStorage或sessionStorage

## Session ##

session称为会话信息，位于web服务器上，主要负责访问者与网站之间的交互，当访问浏览器请求http地址时，将传递到web服务器上并与访问信息进行匹配， 当关闭网站时就表示会话已经结束，网站无法访问该信息了

## Session与Cookie的区别 ##

1. Cookie以文本文件格式存储在浏览器中，而session存储在服务端，数据量由服务器限制。它只允许4kb它没有在cookie中保存多个变量。

2. Cookie的存储限制了数据量，只允许4KB，而session是无限量的

3. 我们可以轻松访问cookie值但是我们无法轻松访问会话值，因此它更安全

4. 设置Cookie时间可以使cookie过期。但是使用session-destory()，我们将会销毁会话。

## 小结 ##

如果我们需要经常登录一个站点时，最好用cookie来保存信息，要不然每次登陆都特别麻烦，如果对于需要安全性高的站点以及控制数据的能力时需要用会话效果更佳，当然我们也可以结合两者，使网站按照我们的想法进行运行

