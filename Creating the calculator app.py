'''
Create a grade calculator that computes for the semestral grade of a course.
Students could type their names, the name of the course, then their prelim,
midterm, and final grade.
The program should print the semestral grade in 2 decimal points and should
display the following emojis depending on the situation:
happy - when grade is greater than 70.00
laughing - when grade is exactly 70.00
sad - when grade is below 70.00
'''
happy, lol, sad = "\U0001F600","\U0001F923","\U0001F619"


class Student_details:
    
    def __init__(self):
        self.student_name = "Default text"
        self.course = "Default text"
        self.pg = "Default text"
        self.mg = "Default text"
        self.fg = "Default text"

    def set_student_details(self):
        self.student_name = input("Enter your name: ")
        self.course = input("Enter your course: ")
        self.pg = float(input("Enter prelim grade: "))
        self.mg = float(input("Enter midterm grade: "))
        self.fg = float(input("Enter finals grade: "))

class Operations:
    
    def __init__(self):
        self.student_lists = list()

    def add_student(self):
       stud_details = Student_details()
       stud_details.set_student_details()
       self.student_lists.append(stud_details)

    def compute(self):
        w_pg, w_mg, w_fg = 0.3, 0.3, 0.4
        for grade in self.student_lists:
            sem_grade = grade.pg*w_pg + grade.mg*w_mg + grade.fg*w_fg

        if sem_grade > 70:
            print(happy)

        elif sem_grade == 70:
            print(lol)

        else:
            print(sad)
            
        

class Menu:
   def __init__(self):
       print("Grade calculator")
       print("Menu")
       print("1. Add your details minna")
       print("2. Compute for your semestral grade")


if __name__ == '__main__':
   operation = Operations()
   #customer = Customers()
   user_choice = "1"
   while user_choice == "1":
       menu = Menu()
       user_choice = input("Input selected option: ")
       if user_choice == "1":
           operation.add_student() 
       elif user_choice == "2":
           operation.compute()
           
       user_choice = input("Press 1 to Continue, Press 2 to Exit ")  
    
    


        
