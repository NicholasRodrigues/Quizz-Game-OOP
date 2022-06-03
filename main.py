from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for _ in range(len(question_data)):
    question_text = question_data[_]["text"]
    question_answer = (question_data[_]["answer"])
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

quiz.endgame()


