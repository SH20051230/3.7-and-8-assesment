# Component 2
# making the questions randomly selected by using a random number
import random
class questions:
    def __int__(self, month_in_eng, month_in_maori):
        self.month_in_eng = month_in_eng
        self.month_in_maori = month_in_maori
        questions.append(self)


def random_question():
    random_num = random.randint(1, 12)
    for month in questions:
        if month.numeric_month == random_num:
            current_question.append(month.month_in_eng)
            current_question.append(month.month_in_maori)
            return current_question


questions_answerd = 0
questions_correct = 0
questions = []
current_question = []

questions("January", "Kohi-tātea",)
questions("February", "Hui-tanguru",)
questions("March", "Poutū-te-rangi",)
questions("April", "Paenga-whāwhā",)
questions("May", "Haratua",)
questions("June", "Pipiri",)
questions("July", "Hōngongoi",)
questions("August", "Here-turi-kōkā",)
questions("September", "Mahuru",)
questions("October", "Whiringa-ā-nuku",)
questions("November", "Whiringa-ā-rangi",)
questions("December", "Hakihea",)
# testing
print(random_question())