# The base program of the Maori quiz
# Put in the basic set up of quiz
# From The basic interface design
# Functions from random question generator from component 2 emerged and tested
# Some changes in label position to make it look better
from tkinter import *
import random

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

def get_question():
    global current_question
    current_question = []
    question = random_question()
    display_question = f"What is the month {question[0]} in Te Reo Maori?"
    Start_label = Label(root, bg="orange", fg="red", text=display_question, font=("Times", 15))
    Start_label.grid(column=2, row=4, ipadx=50, ipady=10)





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
# Button labels for mutiple choice
choice_1 = Label(root, bg="purple", fg="blue", text="Hui-tanguru", font=("Times", 20))
choice_1.grid(column=2, row=5, sticky=W)
choice_2 = Label(root, bg="purple", fg="blue", text="Poutū-te-rangi", font=("Times", 20))
choice_2.grid(column=2, row=5, sticky=E)
choice_3 = Label(root, bg="purple", fg="blue", text="Kohitātea", font=("Times", 20))
choice_3.grid(column=2, row=6, sticky=W)
choice_4 = Label(root, bg="purple", fg="blue", text="Pipiri", font=("Times", 20))
choice_4.grid(column=2, row=6, sticky=E)
# Feed back
system_feed_back = Label(root, bg="cyan", fg="black", text="correct!", font=("Times", 15))
system_feed_back.grid(column=2, row=7, sticky=S)

# submit button
submit_answer = Label(root, bg="lime", fg="white", text="submit", )
submit_answer.grid(column=2, row=6, sticky=N, ipady=15, ipadx=15, pady=20)

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
root.mainloop()