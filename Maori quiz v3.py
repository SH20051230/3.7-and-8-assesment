# The base program of the Maori quiz
# put in get multiple choice answer function
# to make the answers randomly generated with one correct to that question
# and other 3 incorrect answers randomly arranged in the four buttons
from tkinter import *
import random

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





# Main routine

root = Tk()
root.title("Te Reo Maori Quiz")
root.geometry("600x400")
# Size of the quiz app
root.maxsize(800, 600)
root.minsize(400, 200)
root.configure(bg="green")

# Ready button

# Instruction label
instructions_label = Label(root, bg="red", fg="pink", text="Answering the 12 month question below"
                                                           "to help with practice your Maori language",
                           font=("Times", 14))
instructions_label.grid(column=2, row=2)
# record the scores
score = Label(root, fg="white", bg="black", text="Score:", font=("Arial", 10))
score.grid(column=1, row=5, pady=20, ipadx=10,sticky=N)
# record of correct and incorrect numbers
correct_que = Label(root, fg="white", bg="black", text="correct:", font=("Arial", 10))
correct_que.grid(column=1, row=3, pady=20, ipadx=10, sticky=N)
incorrect_que = Label(root, fg="white", bg="black", text="incorrect:", font=("Arial", 10))
incorrect_que.grid(column=1, row=4, pady=20, ipadx=10, sticky=N)
# Button labels for multiple choice
choice_1 =Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_1.grid(column=2, row=5, sticky=W, padx=(30, 0), pady=(10, 30))

choice_2 = Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_2.grid(column=2, row=5, sticky=E, padx=(0, 30), pady=(10, 30))

choice_3 = Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_3.grid(column=2, row=6, sticky=W, padx=(30, 0), pady=(0, 50))

choice_4 = Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_4.grid(column=2, row=6, sticky=E, padx=(0, 30), pady=(0, 50))
# Feed back
system_feed_back = Label(root, bg="cyan", fg="black", text="correct!", font=("Times", 15))
system_feed_back.grid(column=2, row=7, sticky=S)

# submit button is deleted as the answer will be automatically submitted
# when clicking on the chosen button


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

next_question_button = Button(root, bg="red", fg="black", text="Next question", font=("Times", 15), command=get_question)
next_question_button.grid(column=2, row=5, ipadx=50, ipady=10)
start_label = Label(root, bg="orange", fg="red", text="", font=("Times", 15))
start_label.grid(column=2, row=4, ipadx=50, ipady=10)
root.mainloop()