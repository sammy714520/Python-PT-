#!/usr/bin/python
#coding:utf-8

import socket
target_host = "www.google.com.tw"
target_port = 80

#建立socket物件
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#AF_INET 欲使用IPV4位址或主機名稱
#SOCK_STREAM 代表會是個TCP client

#client連線
client.connect((target_host,target_port))

#傳送資料
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#接收資料
response = client.recv(4096)

print response