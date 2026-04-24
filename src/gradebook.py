from src.student import Student
from src.course import Course

class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        
    def add_student(self, student_id, name):
        if student_id in self.students:
            print(f"Student already exists with ID {student_id}.")
            return
        self.students[student_id] = Student(name, student_id)
    
    def add_course(self, course_name):
        if course_name in self.courses:
            print(f"Course already exists with name {course_name}.")
            return
        self.courses[course_name] = Course(course_name)