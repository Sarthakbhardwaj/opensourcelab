#creating a simple tan x graph using matplotlib
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi,np.pi,256,endpoint=True)
t =np.tan(x)
plt.plot(x,t)
plt.show()