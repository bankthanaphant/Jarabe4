# 👉 Code for Stage 6 goes here
class Student:
    
    std_count = 0
    
    def __init__(self, f_name, l_name, age, courses, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.courses = courses
        self.money = 0
        self.salary = salary
        Student.std_count += 1
        
    def fullname(self):
        return self.f_name + " " + self.l_name
        
    def display_student_info(student):
        print("FirstName:", student.f_name)
        print("LastName:", student.l_name)
        print(student.fullname())
        print("Age:", student.age)
        print("Courses:", ", ".join(student.courses))
        print("Money: ", student.money)
        print("-" * 20)

student1 = Student("Alice","totel", 20, ["Math", "English"], 5000)
student2 = Student("Bob","maley", 22, ["Physics", "History"], 3000)
stugent3 = Student("bank","gamo", 21, ["computer", "Chinese"], 7000)

student1.display_student_info()
student2.display_student_info()

print(Student.std_count)