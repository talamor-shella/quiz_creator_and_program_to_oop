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

    # Format the question and choices into a string suitable for saving to a file
    def format_for_file(self):
        content = f"\nQuestion: {self.text}\n"
        for key, value in self.choices.items():
            content += f"{key}) {value}\n"
        content += f"The correct answer is: {self.correct_answer}\n"
        return content
    
    # ask the user the question and check if their answer is correct
    def ask_user(self):
        self.display()
        user_answer = input("Enter your answer (a/b/c/d): ").lower()
        return user_answer == self.correct_answer

# define class quiz manager
class QuizManager: 
    # constructor to initialize category
    def __init__(self, category):
        self.category = category.lower()
        self.filename = self.category + ".txt"
        self.questioms = []
        
    # load questions from a file for the selected category
    def load_questions_from_file(self):
        try: 
            with open(self.filename, "r") as file:
                lines = file.readlines()
            for i in range (0, len(lines), 7): # Process every 7 lines (1 question block)
                try:
                    text = lines[i + 1].strip()  # Get the question text
                    choices = { 
                        'a': lines[i + 2].strip().split(') ', 1)[1],  # Get text after "a) "
                        'b': lines[i + 3].strip().split(') ', 1)[1],  # Get text after "b) "
                        'c': lines[i + 4].strip().split(') ', 1)[1],  # Get text after "c) "
                        'd': lines[i + 5].strip().split(') ', 1)[1],  # Get text after "d) "
                    }
                    correct = lines[i + 6].strip().replace("The correct answer is: ", "")  # Get correct answer
                    self.questions.append(Question(text, choices, correct))  # Add to the question list
                except IndexError:
                    continue 
        except FileNotFoundError:


# define class quiz taker that inherits from quiz manager
# define main function