# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def check(mappy):
    myrep=""
    for i in mappy:
        if i=="S":
            myrep+="E"
        elif i=="E":
            myrep+="S"
    return myrep
t=int(input())
for i in range(1,t+1):
    steps=int(input())
    mappy=input()
    print("Case #"+str(i)+": "+check(mappy))