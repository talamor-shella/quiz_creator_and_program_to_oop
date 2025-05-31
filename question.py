# Assignment 11: Convert Assignment 9 and 10 to OOP

# define class question
class Question:
    # constructor to initialize question text, choices, and correct answer
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    #  displays the questions and choices
    def display(self):
        print(self.text)
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
