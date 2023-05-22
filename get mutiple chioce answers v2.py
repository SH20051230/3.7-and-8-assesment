import random
from tkinter import *
# The code below come from component 2 v3
# Link the labels with the fucntions created previously
# to randomly generated a correct answer label and other 3 incorrect labels
root = Tk()
root.title("Te Reo Maori Quiz")
root.geometry("600x400")
# Size of the quiz app
root.maxsize(800, 600)
root.minsize(400, 200)
root.configure(bg="green")


class Questions:
    def __init__(self, english_month, maori_month, num):
        self.english_month = english_month
        self.maori_month = maori_month
        self.num_month = num
        questions.append(self)
# modified random question function using .sample method to get the randomized answers
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
            incorrect_answers = [m.maori_month for m in questions if m.english_month != current_question[0]]
            randomized_answers = random.sample(incorrect_answers, 3)
            answer_choices = [current_question[1]] + randomized_answers
            random.shuffle(answer_choices)
            return current_question + answer_choices
# from initialising questions component but modified with lambda to call the check answer function
# which will be developed in next component
def get_question():
    global current_question
    current_question = []
    question = random_question()
    display_question = f"What is the month {question[0]} in Te Reo Maori?"
    start_label.configure(text=display_question)
    choice_1.configure(text=question[3], command=lambda: check_answer(question[3], question[1]))
    choice_2.configure(text=question[4], command=lambda: check_answer(question[4], question[1]))
    choice_3.configure(text=question[5], command=lambda: check_answer(question[5], question[1]))
    choice_4.configure(text=question[6], command=lambda: check_answer(question[6], question[1]))

# main routine
questions = []

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
# Choices button and other labels
choice_1 =Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_1.grid(column=2, row=5, sticky=W, padx=(30, 0), pady=(10, 30))

choice_2 = Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_2.grid(column=2, row=5, sticky=E, padx=(0, 30), pady=(10, 30))

choice_3 = Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_3.grid(column=2, row=6, sticky=W, padx=(30, 0), pady=(0, 50))

choice_4 = Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_4.grid(column=2, row=6, sticky=E, padx=(0, 30), pady=(0, 50))
next_question_button = Button(root, bg="red", fg="black", text="Next question",
                              font=("Times", 15), command=get_question)
next_question_button.grid(column=1, row=5, pady=175, ipadx=20, sticky="S")
start_label = Label(root, bg="orange", fg="red", text="", font=("Times", 15))
start_label.grid(column=2, row=4, ipadx=50, ipady=10)
root.mainloop()
