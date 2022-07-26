import matplotlib.pyplot as plt

year = ['2019', '2020', '2021']
dropout = [15.9, 13.1, 12.5]

plt.subplot(131)
plt.bar(year, dropout, width=2, color='red')

plt.subplot(132)
plt.scatter(year, dropout, s=[159,131,125])

plt.subplot(133)
plt.plot(year, dropout)

plt.suptitle('Baltimore Highschool Dropout rate')
plt.show()
