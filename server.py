#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:45:08 2021

@author: alireza
"""
from LorenzSystem import PRNG


def xor(text, key):
    step = len(key)
    num_steps = int(len(text) / len(key))
    encoded = ''
    for i in range(num_steps + 1):
        elapsed = len(text[i*step:])
        if (elapsed < step):
            n1 = int(text[i*step:], 2)
            n2 = int(key[:elapsed], 2)
            encoded += (bin(n1^n2)[2:]).zfill(elapsed)
        else:
            n1 = int(text[i*step:(i+1)*step], 2)
            n2 = int(key, 2) 
            encoded += (bin(n1^n2)[2:]).zfill(step)
    return encoded

import socket
import binascii
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 10008        # Port to listen on (non-privileged ports are > 1023)

prng = PRNG()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break

            prng.SetKey([-5.7589,  2.265,  32.82], 8.0/3.0, 28.0001, 10.0)
            c = prng.generate()
            data = xor(data, c)
            n = int(data, 2)
            print(binascii.unhexlify('%x' % n))