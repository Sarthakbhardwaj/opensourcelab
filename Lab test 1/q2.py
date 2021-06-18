import numpy as np
import matplotlib.pyplot as plt

array1 = np.array(['Python', 'MONGODB', 'NodeJS', 'LISP', 'ruby'])
print("Array1: ",array1)
array2 = ['Python','mongods','java','LISP','ruby']
print("Array2: ",array2)
print("Comparison: ")
a = np.in1d(array1, array2)
print(a)
b = []
for i in a:
    if(a[i]=='True'):
        b.append(array1[i])

count = []
for i in b:
    for j in len(b[i]):
        if(j=='P'):
            count.append(1)
        else:
            count.append(0);

print(count)
count= [1,1,0]
plt.hist(count)
plt.show()
