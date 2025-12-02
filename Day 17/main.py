from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for quest in question_data:
    question_bank.append(Question(quest["question"], quest["correct_answer"]))

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
    print("\n")

print("Congratulations You have completed the quiz!")
print(f"Your final score was {quiz.score} / {quiz.question_number}.")
