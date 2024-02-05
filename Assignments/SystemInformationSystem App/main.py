import mysql.connector
from decimal import Decimal
from dao.ServiceProviderImpl import ServiceProviderImpl
from exception.custom_exceptions import *

MENU_OPTIONS = {
    '1': "Initialize Database",
    '2': "Retrieve Student Information",
    '3': "Retrieve Course Information",
    '4': "Retrieve Teacher Information",
    '5': "Retrieve Enrollments for Course",
    '6': "Retrieve Payments for Student",
    '7': "Enroll Student in Courses",
    '8': "Assign Teacher to Course",
    '9': "Record Payment for Student",
    '10': "Generate Enrollment Report",
    '11': "Add Student",
    '12': "Exit"
}


def display_menu():

    print("\nMenu:")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")


def handle_choice(choice, service_provider):
    if choice == '1':
        service_provider.initialize_database()
        print("Database initialized successfully!")
    elif choice == '2':
        student_id = int(input("Enter Student ID: "))
        student = service_provider.retrieve_student_information(student_id)
        if student:
            print("Student Information:")
            print("Student Information:")
            print("Student ID:", student.student_id)
            print("First Name:", student.first_name)
            print("Last Name:", student.last_name)
            print("Date of Birth:", student.date_of_birth)
            print("Email:", student.email)
            print("Phone Number:", student.phone_number)
        else:
            print("Student not found.")
    elif choice == '3':
        course_id = int(input("Enter Course ID: "))
        course = service_provider.retrieve_course_information(course_id)
        if course:
            print("Course Information:")
            print(f"Course ID: {course.course_id}")
            print(f"Course Name: {course.course_name}")
            print(f"Credits: {course.credits}")
            print(f"Teacher ID: {course.teacher_id}")
        else:
            print("Course not found.")
    elif choice == '4':
        teacher_id = int(input("Enter Teacher ID: "))
        teacher = service_provider.retrieve_teacher_information(teacher_id)
        if teacher:
            print("Teacher Information:")
            print("Course Information:")
            print(f"Course ID: {teacher.teacher_id}")
            print(f"Course Name: {teacher.first_name}")
            print(f"Credits: {teacher.last_name}")
            print(f"Teacher ID: {teacher.email}")
        else:
            print("Teacher not found.")
    elif choice == '5':
        course_id = int(input("Enter Course ID: "))
        enrollments = service_provider.retrieve_enrollments_for_course(course_id)
        if enrollments:
            print("Enrollments for Course:")
            for enrollment in enrollments:
                print(enrollment)
        else:
            print("No enrollments found for the course.")
    elif choice == '6':
        student_id = int(input("Enter Student ID: "))
        payments = service_provider.retrieve_payments_for_student(student_id)
        if payments:
            print("Payments for Student:")
            for payment in payments:
                print(f"Payment ID: {payment.payment_id} || Student ID: {payment.student_id} || "
                      f"Amount: {payment.amount} || Payment Date: {payment.payment_date}")
        else:
            print("No payments found for the student.")
    elif choice == '7':
        student_id = int(input("Enter Student ID: "))
        courses = list(map(int, input("Enter Course IDs (separated by comma): ").split(',')))
        try:
            service_provider.enroll_student_in_courses(student_id, courses)
            print("Student enrolled in courses successfully!")
        except (DuplicateEnrollmentException, CourseNotFoundException, DAOException) as e:
            print(f"Error: {e}")
    elif choice == '8':
        course_id = int(input("Enter Course ID: "))
        teacher_id = int(input("Enter Teacher ID: "))
        try:
            service_provider.assign_teacher_to_course(course_id, teacher_id)
            print("Teacher assigned to course successfully!")
        except (CourseNotFoundException, TeacherNotFoundException, DAOException) as e:
            print(f"Error: {e}")
    elif choice == '9':
        student_id = int(input("Enter Student ID: "))
        amount = Decimal(input("Enter Payment Amount: "))
        payment_date = input("Enter Payment Date (YYYY-MM-DD): ")
        try:
            service_provider.record_payment_for_student(student_id, amount, payment_date)
            print("Payment recorded successfully!")
        except (InvalidPaymentDataException, DAOException) as e:
            print(f"Error: {e}")
    elif choice == '10':
        course_name = input("Enter Course Name: ")
        try:
            enrollment_report = service_provider.generate_enrollment_report(course_name)
            if enrollment_report:
                print("Enrollment Report:")
                for data in enrollment_report:
                    formatted_data = ', '.join(str(item) for item in data)
                    print(formatted_data)
            else:
                print("No data found for the course.")
        except DAOException as e:
            print(f"Error: {e}")
    elif choice == '11':
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")
        try:
            service_provider.add_student(first_name, last_name, date_of_birth, email, phone_number)
        except InvalidStudentDataException as e:
            print(f"Error adding student: {e}")

    elif choice == '12':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")


def main():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rupen',
            database='sisdb'
        )

        service_provider = ServiceProviderImpl(connection)
        print("\n+++++++++++WELCOME TO Student Information System (SIS)+++++++++++")
        while True:
            display_menu()
            choice = input("Enter your choice: ")
            handle_choice(choice, service_provider)

    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    main()
