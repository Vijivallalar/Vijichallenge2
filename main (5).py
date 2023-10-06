def sort_students(student_list):
    # Sort the student list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Define a Student class to represent student objects
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test the function with a list of student objects
if __name__ == "__main__":
    # Create a list of student objects
    students = [
        Student("Alice", "A101", 3.9),
        Student("Bob", "B102", 3.7),
        Student("Charlie", "C103", 4.0),
        Student("David", "D104", 3.5),
    ]

    # Call the sort_students function to sort the students
    sorted_students = sort_students(students)

    # Print the sorted list of students
    print("Students sorted by CGPA (descending order):")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
      