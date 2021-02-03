#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:07:57 2021

@author: alireza
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('ggplot')

class System:
    def __init__(self, init_values=[0.001, 0.0, 0.0]):
        self.initial_state = init_values
        self.time = np.arange(0.0, 100.0, 0.01)
        self.rho = 28
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
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        
        
sys = System()
sys.solve()
sys1 = System([0.0011, 0.0, 0.0])
sys1.solve()
states = sys.states
states1 = sys1.states
fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot(states[:, 0], states[:, 1], states[:, 2])
ax.plot(states1[:, 0], states1[:, 1], states1[:, 2])
plt.draw()
plt.xlabel('x')
plt.ylabel('y')
plt.show()