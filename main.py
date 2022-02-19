from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


NUM_QUESTIONS = 10


question_bank = []


parameters = {
    'amount': NUM_QUESTIONS,
    'type': 'boolean',
    }


# Get Data from API
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()   # Check for response errors
question_data = response.json()['results']  # Get json data from response


for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

