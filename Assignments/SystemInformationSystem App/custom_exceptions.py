class DuplicateEnrollmentException(Exception):
    pass


class CourseNotFoundException(Exception):
    pass


class StudentNotFoundException(Exception):
    pass


class TeacherNotFoundException(Exception):
    pass


class PaymentValidationException(Exception):
    pass


class InvalidStudentDataException(Exception):
    pass


class InvalidPaymentDataException(Exception):
    pass


class InvalidCourseDataException(Exception):
    pass


class InvalidEnrollmentDataException(Exception):
    pass


class InvalidTeacherDataException(Exception):
    pass


class InsufficientFundsException(Exception):
    pass


class DatabaseInitializationException(Exception):
    pass


class DAOException(Exception):
    pass
