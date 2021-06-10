import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi,np.pi,256,endpoint=True)
c = 1/np.tan(x)
plt.plot(x,c)
plt.show()