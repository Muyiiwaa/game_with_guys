from typing import List,Dict

# Define the quiz questions and answers
def get_questions() -> List[Dict]:
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "F. Scott Fitzgerald", "Mark Twain", "Ernest Hemingway"],
            "answer": "Harper Lee"
        }
    ]
    return questions