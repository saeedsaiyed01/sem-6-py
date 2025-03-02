#20. Write a Python program to using multiple inheritance.

class student:
    def __init__(self,rollno,name):
        self.rollno=rollno,
        self.name=name

class marks:
    def __init__(self,s1,s2,s3):
        self.s1=s1,
        self.s2=s2,
        self.s3=s3,
        self.total=s1+s2+s3

class result(student,marks):
     def __init__(self, rollno, name,s1,s2,s3):
         student.__init__(self,rollno,name)
         marks.__init__(self,s1,s2,s3)


     def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rollno)
        print("Sub 1:",self.s1)
        print("Sub 2:",self.s2)
        print("Sub 3:",self.s3)
        print("Total =",self.total)

obj=result("Saeed",122,33,55,66)
obj.display()
    


