from Course import Course
from Studnt import Student

def main():
    course1 = Course("Data Structures")
    course2 = Course("Database Systems")
    
    course1.addStudent(Student("Jane", "Doe", 19))
    course1.addStudent(Student("Mark", "Sumphi", 20))
    
    course2.addStudent(Student("Peter", "Smith", 17))
    
    print("The number of students in ", course1.getCourseName(), "is",
          course1.getNumberOfStudents()
          )
    
    students =  course1.getStudents()
    
   
    
    for student in students:
        print(student.getName())
        
    print("\nStudents in", course2.getCourseName())
    
    students =  course2.getStudents()
    
    # course2.dropStudent(students[0])
    
    for student in students:
        print(student.getName())
        
main()