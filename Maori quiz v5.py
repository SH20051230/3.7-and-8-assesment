# The base program of the Maori quiz
# all components merged and tested
# final version of the quiz
# imports
from tkinter import *
import random


# define questions as a class and given it attributes
class Questions:
    def __init__(self, english_month, maori_month, num):
        self.english_month = english_month  # english name attribute
        self.maori_month = maori_month  # maori name attribute
        self.num_month = num  # number attribute
        questions.append(self)  # append details to the question list


# randomly select a question
def random_question():
    # an empty english month choice list that will hold the english month name
    month_choices = []
    for month in questions:
        # add the english month into the month choice list
        month_choices.append(month.english_month)
    random_month = random.choice(month_choices)   # make the random_month by randomly selecting it from the list
    for month in questions:
        if month.english_month == random_month:
            current_question.append(month.english_month)  # add the english name to current question
            current_question.append(month.maori_month)  # add the maori name to current question
            current_question.append(month.num_month)  # add the number name to current question
            # setting the incorrect answers
            incorrect_answers = [m.maori_month for m in questions if m.english_month != current_question[0]]
            randomized_answers = random.sample(incorrect_answers, 3)
            # get all answer choices including the incorrect ones
            answer_choices = [current_question[1]] + randomized_answers
            random.shuffle(answer_choices)
            return current_question + answer_choices


# get the question displayed on the GUI using global variables
def get_question():
    # global variables
    global current_question
    global selected_choice
    # the summary is printed after user have answered all 12 questions
    if num_questions == 12:
        summary = f"You answered {num_correct} out of {num_questions} questions correctly."
        feedback_label.configure(text=summary)
        # disable all the choice buttons and next question button
        next_question_button.configure(state="disabled")
        choice_1.configure(state="disabled")
        choice_2.configure(state="disabled")
        choice_3.configure(state="disabled")
        choice_4.configure(state="disabled")
        # destroy the root which close the window after 5000 milliseconds = 5 seconds
        root.after(5000, root.destroy)
        return
    current_question = []
    # call the random question function to get a random question
    question = random_question()
    # display it on the screen
    display_question = f"What is the month {question[0]} in Te Reo Maori?"
    feedback_label.configure(text=display_question)
    # the choice buttons that's only activated once each time user click the next question button
    choice_1.configure(text=question[3], command=lambda: set_choice(choice_1, question[3], question[1]), state="normal")
    choice_2.configure(text=question[4], command=lambda: set_choice(choice_2, question[4], question[1]), state="normal")
    choice_3.configure(text=question[5], command=lambda: set_choice(choice_3, question[5], question[1]), state="normal")
    choice_4.configure(text=question[6], command=lambda: set_choice(choice_4, question[6], question[1]), state="normal")
    next_question_button.configure(state="disabled")
    selected_choice = None


def check_answer(user_answer, correct_answer):
    # it checks if the answer user selected matches with the correct answer or not
    # define the global variables
    global num_questions
    global num_correct
    global high_score
    num_questions += 1  # increase the number of questions answered
    # if the selected answer is the correct answer
    if user_answer == correct_answer:
        num_correct += 1  # the number of correct + 1
        system_feed_back.configure(text="Correct!")  # provide this feedback to user
    else:
        # otherwise print the wrong message and display what the correct answer was
        system_feed_back.configure(text="Incorrect.")
        # then updating these changes to the score board
        feedback_label.configure(text=f"The correct answer was {correct_answer}.")
    score.configure(text=f"Score: {num_correct}/{num_questions}")
    correct_que.configure(text=f"Correct: {num_correct}")
    incorrect_que.configure(text=f"Incorrect: {num_questions - num_correct}")
    # if the number of correct beats the high score it updates in the text file
    if num_correct > high_score:
        high_score = num_correct
        high_score_label.configure(text=f"Highest score: {high_score}")
        with open('high_score.txt', 'w') as f:
            f.write(str(high_score))


def set_choice(button, choice, correct_answer):
    # a simple function that sets the choice button temporally disable
    global selected_choice
    selected_choice = button
    check_answer(choice, correct_answer)
    # disabling all choice button
    choice_1.configure(state="disabled")
    choice_2.configure(state="disabled")
    choice_3.configure(state="disabled")
    choice_4.configure(state="disabled")
    # enable the next question button
    next_question_button.configure(state="normal")


def start_quiz():
    ready_button.destroy()   # remove the ready button
    get_question()   # start the quiz


# tk window
root = Tk()
root.title("Te Reo Maori Quiz")
root.geometry("600x400")
root.maxsize(800, 600)
root.minsize(400, 200)
root.configure(bg="#FF7200")

# stats of questions keeping on track
num_questions = 0
num_correct = 0
high_score = 0

# instruction labels and choice buttons
# feedback labels and score system labels
# with their position
instructions_label = Label(root, bg="red", fg="pink", text="Answering the 12 month question below"
                                                           "to help with practice your Maori language",
                           font=("Times", 16))
instructions_label.grid(column=2, row=2)
# score
score = Label(root, fg="white", bg="black", text=f"Score: {num_correct}/{num_questions}", font=("Arial", 10))
score.grid(column=1, row=5, pady=20, ipadx=10, sticky=N)
# correct number label
correct_que = Label(root, fg="white", bg="black", text=f"Correct: {num_correct}", font=("Arial", 10))
correct_que.grid(column=1, row=3, pady=20, ipadx=10, sticky=N)
# incorrect number label
incorrect_que = Label(root, fg="white", bg="black", text=f"Incorrect:"
                      f" {num_questions - num_correct}", font=("Arial", 10))
incorrect_que.grid(column=1, row=4, pady=20, ipadx=10, sticky=N)
# high score label
high_score_label = Label(root, fg="white", bg="black", text=f"Highest score: {high_score}", font=("Arial", 10))
high_score_label.grid(column=1, row=6, pady=20, ipadx=10, sticky=N)
# feedback label
system_feed_back = Label(root, bg="cyan", fg="black", text="", font=("Times", 15))
system_feed_back.grid(column=2, row=6, sticky=S)
# multiple choice buttons
choice_1 = Button(root, bg="purple", fg="white", text="", font=("Times", 20))
choice_1.grid(column=2, row=5, sticky=W, padx=(30, 0), pady=(10, 30))

choice_2 = Button(root, bg="purple", fg="white", text="", font=("Times", 20))
choice_2.grid(column=2, row=5, sticky=E, padx=(0, 30), pady=(10, 30))

choice_3 = Button(root, bg="purple", fg="white", text="", font=("Times", 20))
choice_3.grid(column=2, row=6, sticky=W, padx=(30, 0), pady=(0, 50))

choice_4 = Button(root, bg="purple", fg="white", text="", font=("Times", 20))
choice_4.grid(column=2, row=6, sticky=E, padx=(0, 30), pady=(0, 50))
# ready button
ready_button = Button(root, bg="red", fg="black", text="Ready to start", font=("Times", 15), command=start_quiz)
ready_button.grid(column=2, row=8, pady=20)
# next question button
next_question_button = Button(root, bg="red", fg="black", text="Next question",
                              font=("Times", 15), command=get_question, state="disabled")
next_question_button.grid(column=2, row=9, ipadx=40, ipady=10)


# Question label
current_question = []
# initially is none
selected_choice = None
questions = []
# questions calling the class which is what will could be selected as a question
# to quiz the user
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
# feedback labels and their position (this one is the correct answer one, if the user answer the question wrong)
feedback_label = Label(root, bg="orange", fg="red", text="", font=("Times", 15))
feedback_label.grid(column=2, row=4, ipadx=50, ipady=10)
# the main loop to start the whole quiz program
root.mainloop()
