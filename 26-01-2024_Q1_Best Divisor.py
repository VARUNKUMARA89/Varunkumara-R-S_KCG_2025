#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    l = []
    for i in range (1,n):
        if n%i == 0:
            l.append(i)
    b = l[0]
    for i in range(1,len(l)):
        l[i] = str(l[i])
        sum = 0
        for j in l[i]:
            sum += int(j)
        if sum>b:
            b = sum
            num = l[i]
        elif sum == b:
            if l[i] < l[i-1]:
                num = l[i]
            else:
                num = l[i-1]
    print(num)
            
        
        
        
