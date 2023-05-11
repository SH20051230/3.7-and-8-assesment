# Component 2
# A question named what is 4 in Maori with edited fonts, bg, fg, colour added
# A button correlated with the question have added to answer it
# function to make an answer:
def quiz_answer():
    Label(root, bg="yellow", fg="red", text="wha",
          font=("Times", "50", "bold")).pack

# import tkinter
from tkinter import *
root = Tk()
root.title("Te Reo Maori Quiz")
# set up geometry
root.geometry("600x400")
# resizeable
root.maxsize(800, 600)
root.minsize(400, 200)

# question label
Quiz_question = Label(root, bg="black", fg="white", text="what is 4 in Maoti?",
                      font=("Times", 20, "bold"))
Quiz_question.pack()
# button for answers
Button_quiz_answer = Button(root)
root.mainloop()