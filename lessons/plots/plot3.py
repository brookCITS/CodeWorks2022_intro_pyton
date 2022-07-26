import matplotlib.pyplot as plt
import numpy as np

#data
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
z = np.array([10, 20, 30, 40])

#plot 1:
plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
plt.subplot(2, 2, 4)
plt.plot(x,z)
plt.title("INCOME")

plt.show()
