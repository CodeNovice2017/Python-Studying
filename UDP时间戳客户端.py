#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21567
BUFIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFIZ)
    if not data:
        break
    print data

udpCliSock.close()
