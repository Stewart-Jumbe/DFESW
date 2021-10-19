
#In a new Python file, create a class of students.

#It should contain the following attributes: name, age, and class with default value "student".

#It should also contain a method which takes in 3 test scores and prints the students average test score.
class Students:

    def __init__(self, name, age, class_="Student"): #class_ has been set to a default value of "Student"
        self.name = name
        self.age = age 
        self.class_ = class_ # defaults should be at the bottom otherwise everything beneath will also need a default
    
    def testscore(self,score1,score2,score3): #Method to calculte score
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        result = (score1 +score2 +score3)/3
        return result


Stewart = Students("Stewart", 29) #creating an object
Henry = Students("Henry", 25)
Pipper = Students(name, age)

result_Stewart = Stewart.testscore(10, 20, 30)

#reassigning age of Stewart
Stewart.age = 55
print(result_Stewart)
print(getattr(Stewart,"age"))