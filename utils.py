from typing import List,Dict

# Define the quiz questions and answers


real_questions = [
    {
        "question": "Become a husband first",
        "options": ["Joel", "Lekan", "Muyiwa"]
    },
    {
        "question": "Become a wife first",
        "options": ["Monica", "Semilore", "Tomisin"]
    },
    {
        "question": "Say 'I love you' to their partner the most",
        "options": ["Semilore", "Muyiwa", "Joel", "Tomi", "Lekan"]
    },
    {
        "question": "The clingy couple?",
        "options": ["Tomi and Muyiwa", "Joel and Monica", "Lekan and Semilore"]
    },
    {
        "question": "Become a movie star",
        "options": ["Lekan", "Tomi", "Joel", "Muyiwa", "Semilore", "Monica"]
    },
    {
        "question": "Eat the most food at a gathering",
        "options": ["Lekan", "Tomi", "Semilore", "Muyiwa", "Joel", "Monica"]
    },
    {
        "question": "Get fat when life gets more comfortable",
        "options": ["Monica", "Semilore", "Muyiwa", "Joel", "Tomi", "Lekan"]
    },
    {
        "question": "Get caught drunk",
        "options": ["Monica", "Semilore", "Muyiwa", "Joel", "Tomi", "Lekan"]
    },
    {
        "question": "Try to joke their way out of trouble",
        "options": ["Lekan", "Tomi", "Joel", "Semilore", "Muyiwa", "Monica"]
    },
    {
        "question": "Buy something they can't pay for and run away",
        "options": ["Monica", "Semilore", "Muyiwa", "Joel", "Tomi", "Lekan"]
    },
    {
        "question": "Get in a fist fight",
        "options": ["Monica", "Joel", "Semilore", "Tomi", "Lekan", "Muyiwa"]
    },
    {
        "question": "Who is the best cook?",
        "options": ["Monica", "Muyiwa", "Tomi", "Joel", "Lekan", "Semilore"]
    },
    {
        "question": "Who is the most reserved?",
        "options": ["Muyiwa", "Monica", "Tomi", "Joel", "Lekan", "Semilore"]
    },
    {
        "question": "Who is the fixer?",
        "options": ["Semilore", "Monica", "Muyiwa", "Tomi", "Lekan", "Joel"]
    },
    {
        "question": "Who is the life of the party?",
        "options": ["Semilore", "Muyiwa", "Tomi", "Monica", "Lekan", "Joel"]
    },
    {
        "question": "Who is the funniest?",
        "options": ["Joel", "Semilore", "Monica", "Muyiwa", "Lekan", "Tomi"]
    },
    {
        "question": "Who is the best dancer?",
        "options": ["Muyiwa", "Monica", "Joel", "Tomi", "Lekan", "Semilore"]
    },
    {
        "question": "Who comes off as the bookworm?",
        "options": ["Monica", "Muyiwa", "Tomi", "Semilore", "Joel", "Lekan"]
    },
    {
        "question": "Who is the smartest?",
        "options": ["Monica", "Lekan", "Joel", "Muyiwa", "Semilore", "Tomi"]
    },
    {
        "question": "Who is the clumsiest?",
        "options": ["Lekan", "Muyiwa", "Monica", "Semilore", "Tomi", "Joel"]
    },
    {
        "question": "Who is the most fashionable?",
        "options": ["Monica", "Muyiwa", "Semilore", "Lekan", "Joel", "Tomi"]
    }
]

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

def get_questions(inputs:List = questions) -> List[Dict]:
    return inputs

if __name__ == "__main__":
    print(len(real_questions))