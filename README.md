# Project 9 - Object Oriented Programing

## Vehicle
create a class Vehicle with instance variables 'name', 'color' and a method 'max_speed' which print's out 'max speed'.
then create two other classes called Car and Bus which inherit Vehicle class and override the 'max_speed' function so that it print's out 150 for the bus and 250 for the car


## Game
Create a class called Characters with instance variables 'name', 'position', and a method called move() which does nothing (pass)
create two other classes called Hero and Villain which inherit form Character class. For the hero class, override the move() function so that it changes the position in the positive direction (position + speed) and for the Villain class the move() function changes the position in the negative direction (position - speed)

## Payroll
Create a class called payroll which has two instance variable, company name and employee_list.
- initialize the name by passing the value to the init method but for the employee_list, just make it an empty employee_list

- create a method called add_employee() which takes an Employee object and adds it to the employee_list

- create a method called get_payroll() which has no input but will loop through the employee_list and print out the name and salary of the employee (call the payment method on the employee object to get the salary)
