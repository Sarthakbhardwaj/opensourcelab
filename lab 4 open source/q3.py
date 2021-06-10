import numpy as np
s = input("enter the string:")
n = len(s)
index = int(input("enter the index: "))
print(s)
print(s[0:index]+s[index+1:n])