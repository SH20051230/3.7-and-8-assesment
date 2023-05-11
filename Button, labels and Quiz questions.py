# Component 2
# A question named what is 4 in Maori with edited fonts, bg, fg, colour added


from tkinter import *
root = Tk()
root.title("Te Reo Maori Quiz")
root.geometry("600x400")
root.maxsize(800, 600)
root.minsize(400, 200)


Quiz_question = Label(root, bg="black", fg="white", text="what is 4 in Maoti?",
                      font=("Times", 20, "bold"))
Quiz_question.pack()
root.mainloop()