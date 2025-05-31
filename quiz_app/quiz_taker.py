import random 
from quiz_app.quiz_manager import QuizManager

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
        
        total = self.correct_count + self.incorrect_count 
        print(f"\nQuiz Completed! Out of {total} questions:")  
        print(f"Correct answers: {self.correct_count}")  
        print(f"Wrong answers: {self.incorrect_count}")  