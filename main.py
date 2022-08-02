from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for data in question_data:
    question = Questions(data['question'], data['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

quiz.final_score()