import numpy as np
list =[]
n = int(input("number of values?"))
for i in range(0,n):
    ele = int(input())
    list.append(ele);
print(list)

freq = [None]*100
for i in range(0,n):
    freq[i]=1
    for j in range(i+1,n):
        if(list[i]==list[j]):
            freq[i] = freq[i]+1
            list[j]=0
            

for i in range(0,100):
    if(freq[i]!=0):
        print(str(list[i]) + " " + str(freq[i]))          

