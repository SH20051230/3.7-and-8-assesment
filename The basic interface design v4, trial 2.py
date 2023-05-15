# Component 1
# Added background colour and texts as labels with trialing ethier using pack or grid methid
# This version using grid method
from tkinter import *
root = Tk()
root.title("Te Reo Maori Quiz")
root.geometry("600x400")
# Size of the quiz app
root.maxsize(800, 600)
root.minsize(400, 200)
root.configure(bg="green")
# Lables
Welcome = Label(root, bg="Black", fg="Yellow", text="Welcome to the Maori language quiz",
                font=("Times", 20, "bold")).grid(column=2, row=2)

Start_lable = Label(root, bg="orange", fg="red", text="Ready?",
                      font=("Times", 15,)).grid(column=2, row=5, pady=175, ipadx=20,)
root.mainloop()