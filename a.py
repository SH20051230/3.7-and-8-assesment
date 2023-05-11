import tkinter as tk
import random


class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0
        self.results = []

    def get_question(self):
        if self.question_number < len(self.questions):
            return self.questions[self.question_number]
        else:
            return None

    def answer_question(self, response):
        is_correct = self.get_question().answer == response
        self.results.append((self.get_question().prompt, response, is_correct))
        if is_correct:
            self.score += 1
        self.question_number += 1

    def get_statistics(self):
        total = len(self.questions)
        correct = self.score
        incorrect = total - correct
        return f"Total questions: {total}, Correct answers: {correct}, Incorrect answers: {incorrect}"

    def export_results(self):
        with open("quiz_results.txt", "w") as f:
            for result in self.results:
                f.write(f"Question:
