class ConditionalStatements:
    def __init__(self, num= None, name=None, score=None, attendance=None):
        self.name = name
        self.score = score
        self.attendance = attendance
        self.num = num
        print("initialize constructor")

    def check_positive(self):
        if self.num >0:
            return "positive number"
        else:
            pass

    def check_even_or_odd(self):
        if self.num % 2 == 0:
            return "even number"
        else:
            return "odd number"
        
    def check_grade(self):
        if self.num > 90:
            return "A"
        elif self.num < 90 and self.num > 50:
            return "B"
        elif self.num < 50:
            return "D"

    def check_pass_status(self):
        if self.score >= 50:
            if self.attendance >= 80:
                return f"{self.name} has passed the exam with a score of {self.score} and good attendance."
            else:
                return f"{self.name} has passed the exam with a score of {self.score} but low attendance."
        else:
            return f"{self.name} has failed the exam with a score of {self.score}."
        
number_checker = ConditionalStatements(num =93)  
result = number_checker.check_positive()
result1 = number_checker.check_even_or_odd()
result2 = number_checker.check_grade()
print(result)
print(result1)
print(result2)

student1 = ConditionalStatements(name ="Alice", score = 60, attendance = 85)
student2 = ConditionalStatements(name ="Bob", score = 40, attendance = 75)
student3 = ConditionalStatements(name ="Charlie", score = 55, attendance = 90)

print(student1.check_pass_status())
print(student2.check_pass_status())
print(student3.check_pass_status())