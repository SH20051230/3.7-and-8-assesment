import random
# component 2 developing the random question function
# Trailed by using either make a list of month choice
# and randomly choosing from the list

class Questions:
    def __init__(self, english_month, maori_month, num):
        self.english_month = english_month
        self.maori_month = maori_month
        self.num_month = num
        questions.append(self)


def random_question():
    month_choices = []
    for month in questions:
        month_choices.append(month.english_month)
    random_month = random.choice(month_choices)
    for month in questions:
        if month.english_month == random_month:
            current_question.append(month.english_month)
            current_question.append(month.maori_month)
            current_question.append(month.num_month)
            return current_question


current_question = []
questions = []
num_questions = 0
num_correct = 0

Questions("January", "Kohi-tātea", 1)
Questions("February", "Hui-tanguru", 2)
Questions("March", "Poutū-te-rangi", 3)
Questions("April", "Paenga-whāwhā", 4)
Questions("May", "Haratua", 5)
Questions("June", "Pipiri", 6)
Questions("July", "Hōngongoi", 7)
Questions("August", "Here-turi-kōkā", 8)
Questions("September", "Mahuru", 9)
Questions("October", "Whiringa-ā-nuku", 10)
Questions("November", "Whiringa-ā-rangi", 11)
Questions("December", "Hakihea", 12)

# testing purposes
print(random_question())