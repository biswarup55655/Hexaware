class InvalidDataException(Exception):
    pass


class InsufficientStockException(Exception):
    pass


class IncompleteOrderException(Exception):
    pass


class DuplicateEmailException(Exception):
    pass


class DAOException(Exception):
    pass


class Validation:
    @staticmethod
    def validate_email(email):
        if '@' not in email or '.' not in email:
            raise InvalidDataException("Invalid email format")
