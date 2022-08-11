class QuizBrain:
    def __init__(self, qlist):
        self.ques_number = 0
        self.question_list = qlist
        self.score = 0

    def still_has_questions(self):
        return self.ques_number < len(self.question_list)

        # if self.ques_number >= len(self.question_list):
        #     return False
        # else:
        #     return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.ques_number}\n")

    def next_question(self):
        qtext = self.question_list[self.ques_number].text
        correct_answer = self.question_list[self.ques_number].answer
        self.ques_number += 1
        user_answer = input(f"Q.{self.ques_number}: {qtext}. (True/False): ")
        self.check_answer(user_answer, correct_answer)









