# The base program of the Maori quiz
# Put in the basic set up of quiz
# From The basic interface design
from tkinter import *
# Main routine
root = Tk()
root.title("Te Reo Maori Quiz")
root.geometry("600x400")
# Size of the quiz app
root.maxsize(800, 600)
root.minsize(400, 200)
root.configure(bg="green")
# Ready button
Start_lable = Label(root, bg="orange", fg="red", text="Ready?",
                      font=("Times", 15,))
Start_lable.grid(column=2, row=5, pady=175, ipadx=20, sticky="S")
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
# question label
question_label = Label(root, bg="black", fg="red", text="what's the Maori langauge word of Januray?"
                       ,font=("Times", 20))
question_label.grid(column=2, row=4, ipadx=50, ipady=10)
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
system_feed_back.grid(column=2, row=6, sticky=S)

# submit button
submit_answer = Label(root, bg="lime", fg="white", text="submit", )
submit_answer.grid(column=2, row=5, sticky=N, ipady=15, ipadx=15, pady=20)
root.mainloop()