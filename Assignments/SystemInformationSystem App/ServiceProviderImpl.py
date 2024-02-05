from dao.ServiceProvider import ServiceProvider
from datetime import datetime
from decimal import Decimal
import mysql.connector
from typing import List
from entity.Student import Student
from entity.Course import Course
from entity.Teacher import Teacher
from entity.Enrollment import Enrollment
from entity.Payment import Payment
from exception.custom_exceptions import *


class ServiceProviderImpl(ServiceProvider):
    def __init__(self, connection):
        self.connection = connection

    def initialize_database(self):
        try:
            cursor = self.connection.cursor()
            # Create tables if they don't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Students (
                    student_id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    date_of_birth DATE,
                    email VARCHAR(255),
                    phone_number VARCHAR(20)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Courses (
                    course_id INT AUTO_INCREMENT PRIMARY KEY,
                    course_name VARCHAR(255),
                    credits INT,
                    teacher_id INT,
                    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Enrollments (
                    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
                    student_id INT,
                    course_id INT,
                    enrollment_date DATE,
                    FOREIGN KEY (student_id) REFERENCES Students(student_id),
                    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Teacher (
                    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    email VARCHAR(255),
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Payments (
                    payment_id INT AUTO_INCREMENT PRIMARY KEY,
                    student_id INT,
                    amount DECIMAL(10, 2),
                    payment_date DATE,
                    FOREIGN KEY (student_id) REFERENCES Students(student_id)
                )
            """)
            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as e:
            raise DatabaseInitializationException(f"Error initializing database: {e}")

    def add_student(self, first_name: str, last_name: str, date_of_birth: str, email: str, phone_number: str):
        try:
            if not (first_name and last_name and date_of_birth and email and phone_number):
                raise InvalidStudentDataException("Incomplete student information provided")
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number)
                VALUES (%s, %s, %s, %s, %s)
            """, (first_name, last_name, date_of_birth, email, phone_number))
            self.connection.commit()
            cursor.close()
            print("Student added successfully!")
        except mysql.connector.Error as e:
            raise DAOException(f"Error adding student: {e}")

    def retrieve_student_information(self, student_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Students WHERE student_id = %s", (student_id,))
            student_data = cursor.fetchone()
            cursor.close()
            if student_data:
                return Student(*student_data)
            else:
                return None
        except mysql.connector.Error as e:
            raise DAOException(f"Error retrieving student information: {e}")

    def retrieve_course_information(self, course_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Courses WHERE course_id = %s", (course_id,))
            course_data = cursor.fetchone()
            cursor.close()
            if course_data:
                return Course(*course_data)
            else:
                return None
        except mysql.connector.Error as e:
            raise DAOException(f"Error retrieving course information: {e}")

    def retrieve_teacher_information(self, teacher_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Teacher WHERE teacher_id = %s", (teacher_id,))
            teacher_data = cursor.fetchone()
            cursor.close()
            if teacher_data:
                return Teacher(*teacher_data)
            else:
                return None
        except mysql.connector.Error as e:
            raise DAOException(f"Error retrieving teacher information: {e}")

    def retrieve_enrollments_for_course(self, course_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Enrollments WHERE course_id = %s", (course_id,))
            enrollment_data = cursor.fetchall()
            enrollments = [Enrollment(*enrollment) for enrollment in enrollment_data]
            cursor.close()
            return enrollments
        except mysql.connector.Error as e:
            raise DAOException(f"Error retrieving enrollments: {e}")

    def retrieve_payments_for_student(self, student_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Payments WHERE student_id = %s", (student_id,))
            payment_data = cursor.fetchall()
            payments = [Payment(*payment) for payment in payment_data]
            cursor.close()
            return payments
        except mysql.connector.Error as e:
            raise DAOException(f"Error retrieving payments: {e}")

    def enroll_student_in_courses(self, student_id: int, course_ids: List[int]):
        try:
            cursor = self.connection.cursor()
            for course_id in course_ids:
                cursor.execute("SELECT * FROM Enrollments WHERE student_id = %s AND course_id = %s",
                               (student_id, course_id))
                existing_enrollment = cursor.fetchone()
                if existing_enrollment:
                    raise DuplicateEnrollmentException("Student is already enrolled in the course")

                # Check if the course exists
                cursor.execute("SELECT * FROM Courses WHERE course_id = %s", (course_id,))
                course_data = cursor.fetchone()
                if not course_data:
                    raise CourseNotFoundException("Course not found")
                cursor.execute("""
                           INSERT INTO Enrollments (student_id, course_id, enrollment_date)
                           VALUES (%s, %s, %s)
                       """, (student_id, course_id, datetime.now().date()))

            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as e:
            raise DAOException(f"Error enrolling student in courses: {e}")

    def assign_teacher_to_course(self, course_id: int, teacher_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Courses SET teacher_id = %s WHERE course_id = %s", (teacher_id, course_id))
            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as e:
            raise DAOException(f"Error assigning teacher to course: {e}")

    def record_payment_for_student(self, student_id: int, amount: Decimal, payment_date: datetime):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO Payments (student_id, amount, payment_date)
                VALUES (%s, %s, %s)
            """, (student_id, amount, payment_date))
            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as e:
            raise DAOException(f"Error recording payment for student: {e}")

    def generate_enrollment_report(self, course_name: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT Students.*, Courses.course_name
                FROM Students
                INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id
                INNER JOIN Courses ON Enrollments.course_id = Courses.course_id
                WHERE Courses.course_name = %s
            """, (course_name,))
            enrollment_data = cursor.fetchall()
            cursor.close()
            return enrollment_data
        except mysql.connector.Error as e:
            raise DAOException(f"Error generating enrollment report: {e}")
