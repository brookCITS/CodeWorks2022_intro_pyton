#Import Modules
from matplotlib import pyplot as plt

#create empty lists
months = []
income = []
expense = []
profit = []

#open the file
file = open('files/expense_report.csv','r')

#loop through the file line by line and populate the lists apropriately
for line in file:
    row = line.split(',')
    months.append(row[0])
    income.append(int(row[1]))
    expense.append(int(row[2]))
    profit.append(int(row[1])-int(row[2]))

#create the plot
plt.plot(months,income, 'g', months, expense, 'r', months, profit)
plt.show()
