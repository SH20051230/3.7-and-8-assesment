# all other code come from Maori quiz v4
# The end quiz function is developed and will end the program when the user have answered all 12 questions
# but another function must be developed first before the end quiz function in order to corectly
# run the program
# This version now can display the correct answer after the user have answer the question wrong.
from tkinter import *
import random

class Questions:
    def __init__(self, english_month, maori_month, num):
        self.english_month = english_month
        self.maori_month = maori_month
        self.num_month = num
        questions.append(self)

# functions are all from get mutiple choice answers comonent
# except for check answer function

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
    if num_questions == 12:  # check if user has answered 12 questions
        # show summary and exit
        summary = f"You answered {num_correct} out of {num_questions} questions correctly."
        feedback_label.configure(text=summary)
        root.destroy()
        return
    current_question = []
    question = random_question()
    display_question = f"What is the month {question[0]} in Te Reo Maori?"
    feedback_label.configure(text=display_question)
    choice_1.configure(text=question[3], command=lambda: check_answer(question[3], question[1]))
    choice_2.configure(text=question[4], command=lambda: check_answer(question[4], question[1]))
    choice_3.configure(text=question[5], command=lambda: check_answer(question[5], question[1]))
    choice_4.configure(text=question[6], command=lambda: check_answer(question[6], question[1]))

def check_answer(user_answer, correct_answer):
    global num_questions
    global num_correct
    global high_score
    num_questions += 1
    if user_answer == correct_answer:
        num_correct += 1
        system_feed_back.configure(text="Correct!")
    else:
        system_feed_back.configure(text="Incorrect.")
        feedback_label.configure(text=f"The correct answer was {correct_answer}.")
    score.configure(text=f"Score: {num_correct}/{num_questions}")
    correct_que.configure(text=f"Correct: {num_correct}")
    incorrect_que.configure(text=f"Incorrect: {num_questions - num_correct}")
    # Update high scores
    if num_correct > high_score:
        high_score = num_correct
        high_score_label.configure(text=f"Highest score: {high_score}")
        # Write high score to file
        with open('high_score.txt', 'w') as f:
            f.write(str(high_score))


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

# record the scores and questions user have answered
num_questions = 0
num_correct = 0
high_score = 0
score = Label(root, fg="white", bg="black", text=f"Score: {num_correct}/{num_questions}", font=("Arial", 10))
score.grid(column=1, row=5, pady=20, ipadx=10, sticky=N)
# record of correct and incorrect numbers
correct_que = Label(root, fg="white", bg="black", text=f"Correct: {num_correct}", font=("Arial", 10))
correct_que.grid(column=1, row=3, pady=20, ipadx=10, sticky=N)
incorrect_que = Label(root, fg="white", bg="black", text=f"Incorrect: {num_questions - num_correct}", font=("Arial", 10))
incorrect_que.grid(column=1, row=4, pady=20, ipadx=10, sticky=N)
# High score label
high_score_label = Label(root, fg="white", bg="black", text=f"Highest score: {high_score}", font=("Arial", 10))
high_score_label.grid(column=1, row=6, pady=20, ipadx=10, sticky=N)

# Feedback label
system_feed_back = Label(root, bg="cyan", fg="black", text="", font=("Times", 15))
system_feed_back.grid(column=2, row=7, sticky=S)

# Button labels for multiple choice
choice_1 =Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_1.grid(column=2, row=5, sticky=W, padx=(30, 0), pady=(10, 30))

choice_2 = Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_2.grid(column=2, row=5, sticky=E, padx=(0, 30), pady=(10, 30))

choice_3 = Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_3.grid(column=2, row=6, sticky=W, padx=(30, 0), pady=(0, 50))

choice_4 = Button(root, bg="purple", fg="blue", text="", font=("Times", 20))
choice_4.grid(column=2, row=6, sticky=E, padx=(0, 30), pady=(0, 50))

# Next question button
next_question_button = Button(root, bg="red", fg="black", text="Next question", font=("Times", 15), command=get_question)
next_question_button.grid(column=2, row=5, ipadx=50, ipady=10)

# Question label
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

feedback_label = Label(root, bg="orange", fg="red", text="", font=("Times", 15))
feedback_label.grid(column=2, row=4, ipadx=50, ipady=10)

root.mainloop()