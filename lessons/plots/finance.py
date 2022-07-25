# importing the module
import csv
import matplotlib.pyplot as plt
import datetime as dt
# open the file in read mode
filename = open('spy500.csv')

# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists
days = []
open = []
close = []

# iterating over each row and append
# values to empty list
for col in file:
    days.append(dt.datetime.strptime(col['Date'],'%m/%d/%y').date())
    open.append(float(col['Open'].replace(',','')))
    close.append(float(col['Close*'].replace(',','')))



# Draw As plot

plt.plot(days, open, label="Open")
plt.plot(days, close, label="Close")
plt.ylabel('Price in US Dollars')
plt.legend()
plt.show()
