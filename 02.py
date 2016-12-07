# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Xin Shen)s
"""
import numpy as np
import scipy as sc

str = int(input("请输入："));
print ("你输入的内容是: ", str)
percent=[0.1,0.075,0.05,0.03,0.015,0.01]
limit=[0,100000,200000,400000,600000,1000000]
bonus=0.0
for i in range(5,-1,-1):
    if str>limit[i]:
        bonus+=(str-limit[i])*percent[i]
        str=limit[i]
print(round(bonus,3))
    