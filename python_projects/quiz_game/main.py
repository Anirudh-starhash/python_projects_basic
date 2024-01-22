from data import question_data
from question_model import question
from quiz_brain import Quiz_brain

question_bank=[]
for every_ques in question_data:
    text=every_ques['text']
    answer=every_ques['answer']
    ques=question(text,answer)
    question_bank.append(ques) 
     

quiz=Quiz_brain(question_bank)

while quiz.still_has_questions():
    quiz.check_answer()
    
print('You have successfully completed the quiz congrats!')
print(f'You score is {quiz.score}/{len(quiz.question_list)}')