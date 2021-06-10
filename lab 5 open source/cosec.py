import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi,np.pi,256,endpoint=True)
s = 1/np.sin(x)
plt.plot(x,s)
plt.show()