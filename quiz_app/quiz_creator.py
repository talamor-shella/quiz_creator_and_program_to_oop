from quiz_app.quiz_manager import QuizManager
from question import Question

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
