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

# define class quiz manager
# define class quiz taker that inherits from quiz manager
# define main function