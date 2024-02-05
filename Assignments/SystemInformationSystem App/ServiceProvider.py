from abc import ABC, abstractmethod
from typing import List
from entity.Student import Student
from entity.Course import Course
from entity.Teacher import Teacher
from entity.Enrollment import Enrollment
from entity.Payment import Payment


class ServiceProvider(ABC):

    @abstractmethod
    def initialize_database(self):
        pass

    @abstractmethod
    def retrieve_student_information(self, student_id: int) -> Student:
        pass

    @abstractmethod
    def retrieve_course_information(self, course_id: int) -> Course:
        pass

    @abstractmethod
    def retrieve_teacher_information(self, teacher_id: int) -> Teacher:
        pass

    @abstractmethod
    def retrieve_enrollments_for_course(self, course_id: int) -> List[Enrollment]:
        pass

    @abstractmethod
    def retrieve_payments_for_student(self, student_id: int) -> List[Payment]:
        pass

    @abstractmethod
    def enroll_student_in_courses(self, student_id: int, course_ids: List[int]):
        pass

    @abstractmethod
    def assign_teacher_to_course(self, course_id: int, teacher_id: int):
        pass

    @abstractmethod
    def record_payment_for_student(self, student_id: int, amount: float, payment_date: str):
        pass

    @abstractmethod
    def generate_enrollment_report(self, course_name: str):
        pass

    @abstractmethod
    def add_student(self, first_name: str, last_name: str, date_of_birth: str, email: str, phone_number: str):
        pass