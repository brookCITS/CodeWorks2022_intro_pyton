import matplotlib.pyplot as plt

x = []
y = []
for i in range(20):
    if i %2 == 0: #if i is even then add to lists
        x.append(i)
        y.append(i**2)

plt.plot(x,y)
plt.xlabel('Even integers')
plt.ylabel('Squares of even integers')
plt.show()
