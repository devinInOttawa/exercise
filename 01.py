# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Xin Shen)s
"""
import numpy as np
import scipy as sc

list=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                a=[i, j, k]
                list.append(a)            
print(list)