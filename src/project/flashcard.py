#define the class
class Flashcard:
    #define the class variables
    cards = []

    #define the init function
    def __init__(self, q, ans):
        self.q = q
        self.ans = ans
        Flashcard.cards.append(self)

    #define the methods
    def __str__(self):
        msg = "Question: "+self.q+" | Answer: "+self.ans
        return msg

    def flash(self):
        user_ans = input("Question: "+self.q+"\nAnswer: ")
        if user_ans == self.ans:
            print("That is Correct!\n\n\n")
        else:
            print("That is not correct.\nThe correct answer is "+self.ans+"\n\n\n")

    def get_all(self):
        return Flashcard.cards


#create 4 instance of this class and test all the methods
print(Flashcard('1 + 1 =', '2'))
print(Flashcard('1 - 1 =', '0'))
print(Flashcard('1 * 1 =', '1'))
print(Flashcard('1 / 1 =', '1'))

for card in Flashcard.cards:
    card.flash()
