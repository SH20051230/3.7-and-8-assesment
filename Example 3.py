import tkinter as tk


class QuizQuestion:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def is_correct(self, response):
        return response.lower() == self.answer.lower()


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.question_index = 0
        self.score = 0

    def get_current_question(self):
        if self.question_index < len(self.questions):
            return self.questions[self.question_index]
        else:
            return None

    def answer_question(self, response):
        if self.get_current_question().is_correct(response):
            self.score += 1
        self.question_index += 1


class QuizApp:
    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()
        self.radio_vars = []
        self.radio_buttons = []
        for i in range(4):
            var = tk.StringVar()
            self.radio_vars.append(var)
            button = tk.Radiobutton(self.window, text="", variable=var, value="", command=self.answer_question)
            self.radio_buttons.append(button)
            button.pack()
        self.next_button = tk.Button(self.window, text="Next", command=self.next_question)
        self.next_button.pack()
        self.score_label = tk.Label(self.window, text="Score: 0")
        self.score_label.pack()

    def start