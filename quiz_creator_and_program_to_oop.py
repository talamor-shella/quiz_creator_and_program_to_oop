# Assignment 11: Convert Assignment 9 and 10 to OOP

# random module
import random

# define class question
class Question:
    # constructor to initialize question text, choices, and correct answer
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    #  displays the questions and choices
    def display(self):
        print(f"\nQuestionL: {self.text}")
        for key,value in self.choices.items():
            print(f"{key}) {value}")
# define class quiz manager
# define class quiz taker that inherits from quiz manager
# define main function