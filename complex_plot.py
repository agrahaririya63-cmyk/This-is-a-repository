import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-2*np.pi,np.pi,1000)
y1 = np.sin(z)
y2 = z**2
plt.figure(figsize('z')
plt.plot(z,y1,label = 'sin(z)')
plt.plot(z,y2,label = 'z**2')

plt.xlabel('x')
plt.ylabel('Function value')
plt.title('Plot of sin(z) and z**2')
plt.legend()
plt.grid()
plt.show()


