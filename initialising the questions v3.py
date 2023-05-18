import random
from tkinter import *
# This version have make another function to get the question displayed
# each time randomly on the GUI
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
    Start_label.grid(column=2, row=5, pady=175, ipadx=20, sticky="S")

current_question = []
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

next_question_button = Button(root, bg="red", fg="black", text="Next question", font=("Times", 15), command=get_question)
next_question_button.grid(column=1, row=5, pady=175, ipadx=20, sticky="S")

root.mainloop()
