from question import Question

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