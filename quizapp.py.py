import random

# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": 2,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": 0,
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_answer": 2,
    },
]

# Function to shuffle the quiz questions
def shuffle_questions():
    random.shuffle(quiz_data)

# Function to display and grade the quiz
def take_quiz():
    shuffle_questions()
    score = 0
    total_questions = len(quiz_data)

    print("Welcome to the Quiz!")
    for i, question_data in enumerate(quiz_data, start=1):
        print(f"\nQuestion {i}: {question_data['question']}")
        for j, option in enumerate(question_data['options'], start=1):
            print(f"{j}. {option}")

        user_answer = int(input("Your answer (1-4): ")) - 1  # Adjust for 0-based index

        if 0 <= user_answer < len(question_data['options']) and user_answer == question_data['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"\nYou got {score} out of {total_questions} questions correct.")

# Main menu
while True:
    print("\nMain Menu:")
    print("1. Take Quiz")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        take_quiz()
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
