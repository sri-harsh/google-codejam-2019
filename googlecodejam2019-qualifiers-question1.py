# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def calc(n):
    val=0
    l=len(n)-1
    for i in n:
        val=val+i*(10**l)
        l-=1
    return val
def check(amint,am):
    amintrep=[]
    mul=len(am)-1
    for i in am:
        amintrep.append(int(i))
        mul-=1
    otherintrep=[]
    for i in range(len(amintrep)):
        if amintrep[i]==4:
            otherintrep.append(2)
            amintrep[i]=2
        else:
            otherintrep.append(0)
    return [str(calc(amintrep)),str(calc(otherintrep))]

    
t=int(input())
for i in range(1,t+1):
    am=input()
    amint=int(am)
    print("Case #"+str(i)+": "+" ".join(check(amint,am)))