import tkinter as tk

class QuizQuestion:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.answers = []
        self.current_question = 0
        self.score = 0

        self.question_text = tk.Label(master, text=self.questions[0].question)
        self.question_text.pack()

        self.option_vars = []
        for i in range(len(self.questions[0].options)):
            option_var = tk.StringVar(value=self.questions[0].options[i])
            self.option_vars.append(option_var)
            option_button = tk.Radiobutton(master, text=self.questions[0].options[i], variable=option_var, value=self.questions[0].options[i])
            option_button.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

        self.message_text = tk.Label(master, text="")
        self.message_text.pack()

    def submit_answer(self):
        selected_option = self.option_vars.index(tk.StringVar().set("1"))
        if self.questions[self.current_question].options[selected_option] == self.questions[self.current_question].answer:
            self.score += 1
            self.answers.append(True)
            self.message_text.configure(text="Correct!")
        else:
            self.answers.append(False)
            self.message_text.configure(text="Wrong!")
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question(self.current_question)
        else:
            self.show_results()

    def display_question(self, question_num):
        self.question_text.configure(text=self.questions[question_num].question)
        for i in range(len(self.option_vars)):
            self.option_vars[i].set(self.questions[question_num].options[i])
        self.message_text.configure(text="")
        self.submit_button.configure(text="Submit")

    def show_results(self):
        self.question_text.configure(text="")
        self.submit_button.pack_forget()
        self.message_text.configure(text="You scored " + str(self.score) + " out of " + str(len(self.questions)))
        for i in range(len(self.answers)):
            text = "Question " + str(i+1) + ": " + ("Correct" if self.answers[i] else "Incorrect")
            question_label = tk.Label(self.master, text=text)
            question_label.pack()

questions = [
    QuizQuestion("What is the capital of France?", ["Paris", "Madrid", "Berlin", "Rome"], "Paris"),
    QuizQuestion("What is the largest ocean?", ["Pacific", "Atlantic", "Indian", "Arctic"], "Pacific"),
    QuizQuestion("Who wrote the Harry Potter series?", ["J.K. Rowling", "Stephenie Meyer", "Suzanne Collins", "George R.R. Martin"], "J.K. Rowling"),
]

root = tk.Tk()
app = QuizApp(root, questions)
root.mainloop()