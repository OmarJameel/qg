# questions.py
from datetime import datetime  # Add this line to import the datetime module

questions_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": "Blue Whale"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Beijing", "Tokyo", "Seoul", "Bangkok"],
        "answer": "Tokyo"
    },
    # Add more questions as needed
]

def load_questions():
    # You can modify this function to load questions from a file or a database.
    return questions_data

def save_score(score):
    with open("scores.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: Scored {score}/{len(questions_data)}\n")
