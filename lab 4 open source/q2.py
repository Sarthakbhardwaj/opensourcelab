import numpy as np
a = []
n = int(input("enter the length:"))
for i in range(0,n):
    ele = int(input());
    a.append(ele)

count =0
for i in range(0,n):
    if(a[i]==0):
        count = count + 1

for i in range(0,n):
    while(i<n-count):
        a[i]=1
        i= i+1
    a[i]=0


print(a)
