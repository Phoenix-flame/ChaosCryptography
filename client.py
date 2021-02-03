#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:45:56 2021

@author: alireza
"""


from LorenzSystem import PRNG
import time


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


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 10008        # The port used by the server


prng = PRNG()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    text = "Control Engineering, University of Tehran"
    start = time.time_ns()
    prng.SetKey([-5.7589,  2.265,  32.82], 8.0/3.0, 28.0, 10.0)
    c = prng.generate()
    end = time.time_ns()
    print("Elapsed Time: ", (end - start)/1000000, "ms")
    data_a = ''.join(format(ord(x), 'b').zfill(8) for x in text)
    data = xor(data_a, c)
    
    
    s.sendall(data.encode())

