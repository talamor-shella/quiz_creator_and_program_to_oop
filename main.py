from quiz_creator import QuizCreator
from quiz_taker import QuizTaker

def main():
    while True:
        print("\n--- Quiz Program ---")
        print("1. Create a Quiz")
        print("2. Take a Quiz")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            creator = QuizCreator()
            creator.creating_quiz_questions()
        elif choice == "2":
            taker = QuizTaker()
            taker.start_quiz_taker()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
