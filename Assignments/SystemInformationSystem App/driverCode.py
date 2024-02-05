from entity.Course import Course
from entity.Student import Student
from entity.Payment import Payment


def main():
    students = []
    courses = []
    teachers = []
    while True:
        print("\nWelcome to Student Information System (SIS)")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Assign Teacher to Course")
        print("5. Record Payment")
        print("6. Display Student Information")
        print("7. Display Course Information")
        print("8. Generate Enrollment Report")
        print("9. Generate Payment Report")
        print("10. Update Student Information")
        print("11. Update Course Information")
        print("12. Update Teacher Information")
        print("13. Display Teacher Information")
        print("14. Display Enrollment Information")
        print("15. Display Payment Information")
        print("16. Get Enrolled Courses")
        print("17. Get Payment History")
        print("18. Get Enrollments")
        print("19. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = int(input("Enter Student ID: "))
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
            email = input("Enter Email: ")
            phone_number = input("Enter Phone Number: ")
            student = Student(student_id, first_name, last_name, date_of_birth, email, phone_number)
            students.append(student)
            print("Student added successfully!")

        elif choice == '2':
            course_id = int(input("Enter Course ID: "))
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor_name = input("Enter Instructor Name: ")
            course = Course(course_id, course_name, course_code, instructor_name)
            courses.append(course)
            print("Course added successfully!")

        elif choice == '3':
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            student = next((s for s in students if s.student_id == student_id), None)
            course = next((c for c in courses if c.course_id == course_id), None)
            if student and course:
                student.enroll_in_course(course)
                print("Student enrolled in course successfully!")
            else:
                print("Student or course not found!")

        elif choice == '4':
            course_id = int(input("Enter Course ID: "))
            teacher_name = input("Enter Teacher Name: ")
            course = next((c for c in courses if c.course_id == course_id), None)
            if course:
                course.assign_teacher(teacher_name)
                print("Teacher assigned to course successfully!")
            else:
                print("Course not found!")

        elif choice == '5':
            student_id = int(input("Enter Student ID: "))
            amount = float(input("Enter Payment Amount: "))
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                student.record_payment(amount)
                print("Payment recorded successfully!")
            else:
                print("Student not found!")

        elif choice == '6':
            student_id = int(input("Enter Student ID: "))
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                student.display_student_info()
            else:
                print("Student not found!")

        elif choice == '7':
            course_id = int(input("Enter Course ID: "))
            course = next((c for c in courses if c.course_id == course_id), None)
            if course:
                course.display_course_info()
            else:
                print("Course not found!")

        elif choice == '8':
            course_id = int(input("Enter Course ID: "))
            course = next((c for c in courses if c.course_id == course_id), None)
            if course:
                enrollments = course.get_enrollments()
                print(f"Enrollment Report for Course: {course.course_name} (ID: {course.course_id})")
                print("===================================")
                for enrollment in enrollments:
                    student = enrollment.get_student()
                    print(f"Student ID: {student.student_id}, Student Name: {student.first_name} {student.last_name}")
            else:
                print("Course not found!")

        elif choice == '9':
            student_id = int(input("Enter Student ID: "))
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                payment_history = student.get_payment_history()
                print(f"Payment Report for Student ID: {student_id}")
                print("===================================")
                for payment in payment_history:
                    if isinstance(payment, Payment):
                        print(
                            f"Payment ID: {payment.payment_id}, Amount: {payment.amount}, Date: {payment.payment_date}")
                    else:
                        print("Invalid payment object found in payment history.")
            else:
                print("Student not found!")

        elif choice == '10':
            student_id = int(input("Enter Student ID: "))
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
                email = input("Enter Email: ")
                phone_number = input("Enter Phone Number: ")
                student.update_student_info(first_name, last_name, date_of_birth, email, phone_number)
                print("Student information updated successfully!")
            else:
                print("Student not found!")

        elif choice == '11':
            course_id = int(input("Enter Course ID: "))
            course = next((c for c in courses if c.course_id == course_id), None)
            if course:
                course_name = input("Enter Course Name: ")
                course_code = input("Enter Course Code: ")
                instructor_name = input("Enter Instructor Name: ")
                course.update_course_info(course_name, course_code, instructor_name)
                print("Course information updated successfully!")
            else:
                print("Course not found!")

        elif choice == '12':
            teacher_id = int(input("Enter Teacher ID: "))
            teacher = next((t for t in teachers if t.teacher_id == teacher_id), None)
            if teacher:
                name = input("Enter Teacher Name: ")
                email = input("Enter Teacher Email: ")
                expertise = input("Enter Teacher Expertise: ")
                teacher.update_teacher_info(name, email, expertise)
                print("Teacher information updated successfully!")
            else:
                print("Teacher not found!")

        elif choice == '13':
            teacher_id = int(input("Enter Teacher ID: "))
            teacher = next((t for t in teachers if t.teacher_id == teacher_id), None)
            if teacher:
                teacher.display_teacher_info()
            else:
                print("Teacher not found!")

        elif choice == '14':
            course_id = int(input("Enter Course ID: "))
            course = next((c for c in courses if c.course_id == course_id), None)
            if course:
                enrollments = course.get_enrollments()
                for enrollment in enrollments:
                    student = enrollment.get_student()
                    print(f"Student ID: {student.student_id}, Course ID: {course.course_id}")
            else:
                print("Course not found!")
        elif choice == '15':
            student_id = int(input("Enter Student ID: "))
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                payments = student.get_payment_history()
                for payment in payments:
                    print(f"Payment ID: {payment.payment_id}, Amount: {payment.amount}, Date: {payment.date}")
            else:
                print("Student not found!")

        elif choice == '16':
            student_id = int(input("Enter Student ID: "))
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                enrolled_courses = student.get_enrolled_courses()
                for course in enrolled_courses:
                    print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")
            else:
                print("Student not found!")

        elif choice == '17':
            student_id = int(input("Enter Student ID: "))
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                payment_history = student.get_payment_history()
                for payment in payment_history:
                    if isinstance(payment, Payment):
                        print(
                            f"Payment ID: {payment.payment_id}, Amount: {payment.amount}, Date: {payment.payment_date}")
                    else:
                        print("Invalid payment object found in payment history.")
            else:
                print("Student not found!")

        elif choice == '18':
            course_id = int(input("Enter Course ID: "))
            course = next((c for c in courses if c.course_id == course_id), None)
            if course:
                enrollments = course.get_enrollments()
                for enrollment in enrollments:
                    student = enrollment.get_student()
                    print(f"Student ID: {student.student_id}, Course ID: {course.course_id}")
            else:
                print("Course not found!")

        elif choice == '19':
            print("Thank you for using Student Information System (SIS). Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
