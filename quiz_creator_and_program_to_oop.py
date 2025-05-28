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
        self.questions = []
        
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
            print("No quiz found in this category")
            return False
        return True
    
# define quiz creator class that inherits from quiz manager
class QuizCreator(QuizManager): 
    # constructor asks the user to choose a category
    def __init__(self):
        category = input("Enter a category for the quiz (Math, English, Science, Hisitory): ").lower()
        super().__init__(category) #initialize parent class with that category 

    # start creating the quiz questions
    def creating_quiz_questions(self):
        print("\n---Quiz Creator---")
        
        #while loop to allow adding multiple questions
        while True:
            text = input("\nEnter a question: ")  
            choices = {  
                'a': input("Option a: "),
                'b': input("Option b: "),
                'c': input("Option c: "),
                'd': input("Option d: ")
            }
            correct_answer = input("Enter the correct answer (a/b/c/d): ").lower()  

            question = Question(text, choices, correct_answer) #create a Question object
            question.display()  # Show the question

            confirm = input("Is this correct? (yes/no): ").lower()  
            if confirm == "yes":  
                with open(self.filename, "a") as file:  
                    file.write(question.format_for_file())  
                print("Question added successfully!")  

            more = input("Add another question? (yes/no): ").lower()  
            if more != "yes":  
                print("Exiting Quiz Creator.")  
                break  

# define class quiz taker that inherits from quiz manager
class QuizTaker(QuizManager):
    # constructor asks for category and sets counters
    def __init__(self):
        category = input("Enter a quiz category (Math, English, Science, History): ")
        super().__init__(category)
        self.correct_count = 0
        self.incorrect_count = 0
    
    # start taking the quiz
    def start_quiz_taker(self):
        if not self.load_questions_from_file():  # Try to load questions
            return
        print("\n--- Quiz Taker ---")  
        while self.questions:  
            question = random.choice(self.questions)  # Picks a random question
            correct = question.ask_user()  

            if correct:  
                print("Correct!\n")  
                self.correct_count += 1  
            else:
                print(f"Wrong! The correct answer is {question.correct_answer}\n")  
                self.incorrect_count += 1  

            self.questions.remove(question)  # Remove the asked question

            cont = input("Do you want to continue? (yes/no): ").lower()  
            if cont != "yes": 
                break

    
# define main function