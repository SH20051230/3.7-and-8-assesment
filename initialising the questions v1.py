# Component 2
# Setting up classes for the quiz question and its english, maori attribute
# keep track of how many questions being answered and how many of them is correct
# Putting these in a list to keep track of the questions
class questions:
    def __int__(self, month_in_eng, month_in_maori):
        self.month_in_eng = month_in_eng
        self.month_in_maori = month_in_maori
        questions.append(self)


questions_answerd = 0
questions_correct = 0
questions = []

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