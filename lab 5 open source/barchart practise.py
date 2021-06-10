import numpy as np 
import matplotlib.pyplot as plt
n = 4
x = np.arange(n)
y1=(1-x/float(n))*np.random.uniform(0.5,1.0,n)
plt.bar(x+y1,facecolor='#9999ff',edgecolor='white',height=20)
plt.show()
y2=(1-x/float(n))*np.random.uniform(0.5,1.0,n)
plt.bar(x,-y2,facecolor='#ff9999',edgecolor='white',height=30)
plt.show()