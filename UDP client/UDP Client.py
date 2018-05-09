#!/usr/bin/python
#coding:utf-8

import socket
target_host = "127.0.0.1"
target_port = 80

#建立socket物件
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#AF_INET 欲使用IPV4位址或主機名稱
#SOCK_STREAM 代表會是個UDP socket通信

#绑定地址和端口
client.bind((target_host, target_port))

#傳送資料
client.sendto("AABBCC",(target_host,target_port))


#接收資料
data, addr = client.recvfrom(4096) 
#返回一个格式為(client,address)的位元组
#client 客戶端資料
#address是格式為(host,port)的位元组
print data