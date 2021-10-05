#returns do not print things out, returns should be used in fuctions not procedures
#procedures use prints to the terminal. 
### Do this later



####Exercise####
from math import ceil
# def exam_grade(name,homework_score,ass_score,exam_score):
#     final_result = ((homework_score + ass_score + exam_score)/175)*100
    
#     return f'{name} your ICT grade as a percentage is {final_result}% ' 

# print(exam_grade('Stewart', 25, 50, 100))

def exm_score_procedure ():


    if final_result >= 95:
        grade = 'A'
        return f'{name} your ICT grade as a percentage is {final_result}% '
    elif 95 > final_result >= 65:
        grade = 'B'
        #return f'{name} your ICT grade as a percentage is {final_result}%, your grade is {grade} '
    else:
        #return f'{name} your ICT grade as a percentage is {final_result}% , please try again next year '
        #return f'{name} your ICT grade as a percentage is {final_result}% ' 

def exam_grade_cal(name,homework_score,ass_score,exam_score):
    
    final_result = (((homework_score + ass_score + exam_score)/175)*100)
    

exam_grade('Stewart', 25, 50, 25)


