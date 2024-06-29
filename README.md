# Student Registration System

This Python-based Student Registration System allows admins to manage students and courses, and enables students to register and manage their courses. Data is stored using a file-based approach.

## Features

### Admin Functions
- Remove Student
- Add Course
- Remove Course
- Unregister Student from Course
- View Student Info
- View All Students

### Student Functions
- Register
- Login
- View Available Courses
- Register for a Course
- View Profile

## Usage

### Main Menu
1. **Admin Login**
2. **Student**
   - Register
   - Login
3. **Exit**

### Admin Login
- Default Admin Email: `admin@gmail.com`
- Default Admin Password: `admin`

### Student Registration
- Students can register by providing their name, student ID, and password.
- Once registered, students can log in using their student ID and password.

### Data Storage
- Students' data is stored in `students.txt`.
- Courses' data is stored in `courses.txt`.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/fitsumhelina/student-registration-system.git
    cd student-registration-system
    ```

2. Run the script:
    ```bash
    python main.py
    ```

## Usage

1. Upon running the script, you will be presented with a menu of options:

    ```
    1. Admin Login
    2. Student
       - Register
       - Login
    3. Exit
    ```

2. Select an option by entering the corresponding number.

3. Follow the prompts to perform the desired action.

## Code Overview

### `RegistrationManager` Class

This class manages the registration system, providing methods for student registration, login, course management, and data persistence.

- `register_student(name, student_id, password)`: Registers a new student.
- `login_student(student_id, password)`: Authenticates a student login.
- `add_course(course_code, course_name)`: Adds a new course to the system.
- `remove_course(course_code)`: Removes a course from the system.
- `remove_student(student_id)`: Removes a student from the system.
- `unregister_student_from_course(student_id, course_code)`: Removes a student from a course.
- `view_student_info(student_id)`: Displays information about a specific student.
- `view_all_students()`: Displays information about all registered students.
- `load_data()`: Loads data from storage (students and courses files).
- `save_data()`: Saves data to storage (students and courses files).

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner via [LinkedIn](https://www.linkedin.com/in/fitsum-helina-57164828a/).

## License

This project is licensed under the MIT License - see the [LICENSE](./licence) file for details.
