from question_model import *
# from data import question_data
from data1 import question_data
from quiz_brain import *


question_bank = []
item = 0

for question in question_data:
    # qno = "Question" + str(item)
    qno = Question(question["question"], question["correct_answer"])
    question_bank.append(qno)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    tot_score = quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.ques_number}")


# num = 0
# score = 0
# # should_continue = True
#
# while num < 12:
#
#     ans = input(question_bank[num].text)
# #
#     if ans == question_bank[num].answer:
#         print("Right answer")
#         score += 1
#         num += 1
#     else:
#         print("Wrong answer")
#         num += 1
#
# print(f"Your total score is {score}")
