import matplotlib.pyplot as plt
import numpy as np

t = np.array([0,1,2,3,4,5])
x = t*t
y = t**3
z = t**4
plt.plot(t, x, 'g', t, y, 'r', t, z)
plt.ylabel('some numbers')
plt.show()
