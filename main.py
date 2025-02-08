from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

brain = QuizzBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print("The quiz is over.")
print(f"The final score was: {brain.score}/{brain.question_number}")