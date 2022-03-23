'''
--1.
    Create a QuizBrain class
    init with question_number set default to 0
    question_list as a input
--2.create next_question method
    retrieve the item at the current question_number from the question list
    Use the input() function to show the user the Question text and ask for the user's answer
--3. Create a quiz_continue() method
--4. Check the ansers and keeping score  check_answer()
'''


class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def quiz_continue(self):
        n = len(self.question_list)
        while self.question_number < n:
            self.next_question()
        print("You have finished!")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You're right.")
        else:
            print("That's wrong.")
        print(f"The correct answer is: {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}.")
        print('\n')


        