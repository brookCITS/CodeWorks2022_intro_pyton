# project 8 -- Python Class

## game character

create a character class with instance variables name, level, position, and lives. The name should be initialized when the instance of the class is created but the rest should be initialized with default values (level = 0, lives = 3, and position = 0). It should also have a class variable characters (empty list)

- create a method called move() which takes a value speed and changes the position
- create a method called level_up() which adds 1 to the level
- create a method called kill() which subtracts 1 from lives
- create a method called bonus() which adds 1 to lives
- create 4 instance of this class and test all the methods twice

## Car
create a class called "Car" with instance variables "make" and "model" which get initialized when the instance of the class is created.
- Add to-string method that will return the make and model as a concatenated string
- create 4 instance of this class and test all the methods twice

## flashcard
create a class called flashcard which will initialize a word and it's meaning as instance variables when it is first created
- create a class variable called flashcards (empty list) and add the flashcard instances to it inside the init method

- create a to-string method that returns the word and the meaning as a concatenated string
- create a method called "flash" which will pick out a flash card and ask the user for the answer and give a response message based on the correctness of the answer
- create a method called "get_all" which will return the flashcards list
- create 4 instance of this class and test all the methods twice
