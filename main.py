import os
import hashlib

class Student:
    def __init__(self, name, student_id, password):
        self.name = name
        self.student_id = student_id
        self.password = password
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def display_courses(self):
        if self.courses:
            print(f"{self.name} is registered for the following courses:")
            for course in self.courses:
                print(f"- {course}")
        else:
            print(f"{self.name} is not registered for any courses.")


class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code

    def __str__(self):
        return f"{self.name} ({self.course_code})"


class RegistrationManager:
    def __init__(self, student_file="students.txt", course_file="courses.txt"):
        self.student_file = student_file
        self.course_file = course_file
        self.students = {}
        self.courses = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.student_file):
            with open(self.student_file, "r") as f:
                for line in f:
                    values = line.strip().split(",")
                    if len(values) >= 3:
                        name, student_id, password = values[:3]
                        courses = values[3].split(";") if len(values) > 3 and values[3] else []
                        student = Student(name, student_id, password)
                        student.courses = courses
                        self.students[student_id] = student

        if os.path.exists(self.course_file):
            with open(self.course_file, "r") as f:
                for line in f:
                    name, course_code = line.strip().split(",")
                    self.courses[course_code] = Course(name, course_code)

    def save_data(self):
        with open(self.student_file, "w") as f:
            for student in self.students.values():
                courses = ";".join(student.courses)
                f.write(f"{student.name},{student.student_id},{student.password},{courses}\n")

        with open(self.course_file, "w") as f:
            for course in self.courses.values():
                f.write(f"{course.name},{course.course_code}\n")

    def add_student(self, name, student_id, password):
        if student_id not in self.students:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            self.students[student_id] = Student(name, student_id, hashed_password)
            self.save_data()
            print(f"Student {name} added successfully.")
        else:
            print("Student ID already exists.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            print("Student removed successfully.")
        else:
            print("Student not found.")

    def add_course(self, name, course_code):
        if course_code not in self.courses:
            self.courses[course_code] = Course(name, course_code)
            self.save_data()
            print(f"Course {name} added successfully.")
        else:
            print("Course code already exists.")

    def remove_course(self, course_code):
        if course_code in self.courses:
            del self.courses[course_code]
            self.save_data()
            print("Course removed successfully.")
        else:
            print("Course not found.")

    def register_student_for_course(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            self.students[student_id].add_course(self.courses[course_code].name)
            self.save_data()
            print("Student registered for course successfully.")
        else:
            print("Student or course not found.")

    def unregister_student_from_course(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            self.students[student_id].remove_course(self.courses[course_code].name)
            self.save_data()
            print("Student unregistered from course successfully.")
        else:
            print("Student or course not found.")

    def display_student_info(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Student Name: {student.name}")
            print(f"Student ID: {student.student_id}")
            student.display_courses()
        else:
            print("Student not found.")

    def display_all_students(self):
        if self.students:
            print("Registered Students:")
            for student_id, student in self.students.items():
                print(f"\nStudent ID: {student_id}")
                self.display_student_info(student_id)
        else:
            print("No registered students.")

    def display_courses(self):
        if self.courses:
            print("Available courses:")
            for course in self.courses.values():
                print(f"- {course.name} ({course.course_code})")
        else:
            print("No courses available.")


def authenticate_user(role, reg_manager):
    if role == "admin":
        email = input("Enter admin email: ")
        password = input("Enter admin password: ")
        return email == "admin@gmail.com" and password == "admin"
    elif role == "student":
        student_id = input("Enter your student ID: ")
        password = input("Enter your password: ")
        if student_id in reg_manager.students:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            return reg_manager.students[student_id].password == hashed_password
        else:
            return False
    return None


def admin_menu(reg_manager):
    while True:
        print("\n1. Remove Student\n2. Add Course\n3. Remove Course\n4. Unregister Student from Course\n5. View Student Info\n6. View All Students\n7. Logout\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter the student ID: ")
            reg_manager.remove_student(student_id)

        elif choice == '2':
            course_name = input("Enter the course name: ")
            course_code = input("Enter the course code: ")
            reg_manager.add_course(course_name, course_code)

        elif choice == '3':
            course_code = input("Enter the course code: ")
            reg_manager.remove_course(course_code)

        elif choice == '4':
            student_id = input("Enter the student ID: ")
            course_code = input("Enter the course code: ")
            reg_manager.unregister_student_from_course(student_id, course_code)

        elif choice == '5':
            student_id = input("Enter the student ID: ")
            reg_manager.display_student_info(student_id)

        elif choice == '6':
            reg_manager.display_all_students()

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")


def student_menu(reg_manager, student_id):
    while True:
        print("\n1. View Available Courses\n2. Register for a Course\n3. View My Profile\n4. Logout\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            reg_manager.display_courses()

        elif choice == '2':
            course_code = input("Enter the course code: ")
            reg_manager.register_student_for_course(student_id, course_code)

        elif choice == '3':
            reg_manager.display_student_info(student_id)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")


def student_registration(reg_manager):
    name = input("Enter your name: ")
    student_id = input("Enter your student ID: ")
    password = input("Enter your password: ")
    reg_manager.add_student(name, student_id, password)
    print("Registration successful. You can now log in.")


def main_menu():
    reg_manager = RegistrationManager()

    while True:
        print("\n1. Admin Login\n2. Student\n3. Exit\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            if authenticate_user("admin", reg_manager):
                admin_menu(reg_manager)
            else:
                print("Invalid admin credentials.")

        elif choice == '2':
            print("\n1. Register\n2. Login\n")
            student_choice = input("Enter your choice: ")

            if student_choice == '1':
                student_registration(reg_manager)
            elif student_choice == '2':
                student_id = input("Enter your student ID: ")
                if authenticate_user("student", reg_manager):
                    student_menu(reg_manager, student_id)
                else:
                    print("Invalid student ID or password.")
            else:
                print("Invalid choice. Please try again.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
