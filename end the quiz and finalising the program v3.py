# all other code come from Maori quiz v4
# The end quiz function is developed and will end the program when the user have answered all 12 questions
# but another function must be developed first before the end quiz function in order to corectly
# run the program
# add a once clicked button "ready to start button" to make sure the first set of question is displayed
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
            incorrect_answers = [m.maori_month for m in questions if m.english_month != current_question[0]]
            randomized_answers = random.sample(incorrect_answers, 3)
            answer_choices = [current_question[1]] + randomized_answers
            random.shuffle(answer_choices)
            return current_question + answer_choices

def get_question():
    global current_question
    global selected_choice
    if num_questions == 12:
        summary = f"You answered {num_correct} out of {num_questions} questions correctly"
        feedback_label.configure(text=summary)
        next_question_button.configure(state="disabled")
        choice_1.configure(state="disabled")
        choice_2.configure(state="disabled")
        choice_3.configure(state="disabled")
        choice_4.configure(state="disabled")
        # destroy the root which close the window after 5000 milliseconds = 5 seconds
        root.after(5000, root.destroy)
        return
    current_question = []
    question = random_question()
    display_question = f"What is the month {question[0]} in Te Reo Maori?"
    feedback_label.configure(text=display_question)
    choice_1.configure(text=question[3], command=lambda: set_choice(choice_1, question[3], question[1]), state="normal")
    choice_2.configure(text=question[4], command=lambda: set_choice(choice_2, question[4], question[1]), state="normal")
    choice_3.configure(text=question[5], command=lambda: set_choice(choice_3, question[5], question[1]), state="normal")
    choice_4.configure(text=question[6], command=lambda: set_choice(choice_4, question[6], question[1]), state="normal")
    next_question_button.configure(state="disabled")
    selected_choice = None

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
    if num_correct > high_score:
        high_score = num_correct
        high_score_label.configure(text=f"Highest score: {high_score}")
        with open('high_score.txt', 'w') as f:
            f.write(str(high_score))

def set_choice(button, choice, correct_answer):
    global selected_choice
    selected_choice = button
    check_answer(choice, correct_answer)
    choice_1.configure(state="disabled")
    choice_2.configure(state="disabled")
    choice_3.configure(state="disabled")
    choice_4.configure(state="disabled")
    next_question_button.configure(state="normal")

def start_quiz():
    ready_button.destroy() # remove the ready button
    get_question() # start the quiz

root = Tk()
root.title("Te Reo Maori Quiz")
root.geometry("600x400")
root.maxsize(800, 600)
root.minsize(400, 200)
root.configure(bg="#FF7200")

num_questions = 0
num_correct = 0
high_score = 0

instructions_label = Label(root, bg="red", fg="pink", text="Answering the 12 month question below"
                                                           "to help with practice your Maori language",
                           font=("Times", 14))
instructions_label.grid(column=2, row=2)

score = Label(root, fg="white", bg="black", text=f"Score: {num_correct}/{num_questions}", font=("Arial", 10))
score.grid(column=1, row=5, pady=20, ipadx=10, sticky=N)

correct_que = Label(root, fg="white", bg="black", text=f"Correct: {num_correct}", font=("Arial", 10))
correct_que.grid(column=1, row=3, pady=20, ipadx=10, sticky=N)

incorrect_que = Label(root, fg="white", bg="black", text=f"Incorrect: {num_questions - num_correct}", font=("Arial", 10))
incorrect_que.grid(column=1, row=4, pady=20, ipadx=10, sticky=N)

high_score_label = Label(root, fg="white", bg="black", text=f"Highest score: {high_score}", font=("Arial", 10))
high_score_label.grid(column=1, row=6, pady=20, ipadx=10, sticky=N)

system_feed_back = Label(root, bg="cyan", fg="black", text="", font=("Times", 15))
system_feed_back.grid(column=2, row=6, sticky=S)

choice_1 = Button(root, bg="purple", fg="white", text="", font=("Times", 20))
choice_1.grid(column=2, row=5, sticky=W, padx=(30, 0), pady=(10, 30))

choice_2 = Button(root, bg="purple", fg="white", text="", font=("Times", 20))
choice_2.grid(column=2, row=5, sticky=E, padx=(0, 30), pady=(10, 30))

choice_3 = Button(root, bg="purple", fg="white", text="", font=("Times", 20))
choice_3.grid(column=2, row=6, sticky=W, padx=(30, 0), pady=(0, 50))

choice_4 = Button(root, bg="purple", fg="white", text="", font=("Times", 20))
choice_4.grid(column=2, row=6, sticky=E, padx=(0, 30), pady=(0, 50))

ready_button = Button(root, bg="red", fg="black", text="Ready to start", font=("Times", 15), command=start_quiz)
ready_button.grid(column=2, row=8, pady=20)

next_question_button = Button(root, bg="red", fg="black", text="Next question", font=("Times", 15), command=get_question, state="disabled")
next_question_button.grid(column=2, row=9, ipadx=40, ipady=10)


# Question label
current_question = []
selected_choice = None
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