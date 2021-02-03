#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:47:07 2021

@author: alireza
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import ctypes


class System:
    def __init__(self):
        self.initial_state = [-5.76,  2.27,  32.82]
        self.time = np.arange(0.0, 40.0, 0.01)
        self.rho = 28.0
        self.sigma = 10.0
        self.beta = 8.0 / 3.0
        self.states = None

    def model(self, state, t):
        x, y, z = state
        return self.sigma * (y - x), x * (self.rho - z) - y, x * y - self.beta * z

    def solve(self):
        self.states = odeint(self.model, self.initial_state, self.time)
        return self.states

    def plot(self):
        fig = plt.figure()
        ax = fig.gca(projection="3d")
        ax.plot(self.states[:, 0], self.states[:, 1], self.states[:, 2])
        plt.draw()
        plt.show()

    def get_lya_exp(self):
        epsilon = 0.00001
        lya_exp = []

        for i in range(6):    
            model1 = System()
            for j in range(3):
                model1.initial_state[j] = self.initial_state[j] if i != j else (self.initial_state[j] + epsilon) 
            model1.beta = self.beta if i != 3 else (self.beta+epsilon)
            model1.rho = self.rho if i != 4 else (self.rho+epsilon)
            model1.sigma = self.sigma if i != 5 else (self.sigma+epsilon)
            response = self.solve()
            response1 = model1.solve()
            abs_delta_X = abs(response[-1]-response1[-1])
            lambda_matrix = 1/40*(np.log(abs_delta_X/epsilon))
            lya_exp.append(np.amax(lambda_matrix))

        return lya_exp


class PRNG:
    def __init__(self):
        self.model = System()

    def SetKey(self, initialValue, beta, rho, sigma):
        self.model.beta = beta
        self.model.rho = rho
        self.model.sigma = sigma
        self.model.initial_state = initialValue

    def check_params(self):
        lya_exp = self.model.get_lya_exp()
        for i in lya_exp:
            if(i <= 0):
                msg = 'INVALID PARAMS'
                print(msg)
                return
        print('OK')

    def generate(self):
        response = self.model.solve()
        self.check_params()                   ##########################################3
        response = response[range(50, len(response), 62)]
        code = ''
        for data in response:
            num = 0.0
            for vec in data:
                num += vec
            binaryForm = bin(ctypes.c_uint.from_buffer(
                ctypes.c_float(num)).value)[2:]
            bit1 = binaryForm[-5]  # 11
            bit2 = binaryForm[-4]  # 17
            bit3 = binaryForm[-1]
            bit4 = binaryForm[-2]
            code += (bit1)
            code += (bit2)
            code += (bit3)
            code += (bit4)
        return code

