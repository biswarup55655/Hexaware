from exception.ExceptionHandling import InvalidDataException, Validation


class Customer:

    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__CustomerID = customer_id
        self.__FirstName = first_name
        self.__LastName = last_name
        self.__Email = email
        self.__Phone = phone
        self.__Address = address
        self.__Orders = []

    @property
    def CustomerID(self):
        return self.__CustomerID

    @property
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter
    def FirstName(self, first_name):
        if isinstance(first_name, str):
            self.__FirstName = first_name
        else:
            raise Exception("First name must be a string.")

    @property
    def LastName(self):
        return self.__LastName

    @LastName.setter
    def LastName(self, last_name):
        if isinstance(last_name, str):
            self.__LastName = last_name
        else:
            raise Exception("Last name must be a string.")

    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self, email):
        try:
            Validation.validate_email(email)
            self.__Email = email
        except InvalidDataException as e:
            raise InvalidDataException(str(e))

    @property
    def Phone(self):
        return self.__Phone

    @Phone.setter
    def Phone(self, phone):
        if isinstance(phone, str):
            self.__Phone = phone
        else:
            raise Exception("Phone must be a string.")

    @property
    def Orders(self):
        return self.__Orders

    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, address):
        if isinstance(address, str):
            self.__Address = address
        else:
            raise ValueError("Address must be a string.")

    def calculate_total_orders(self, customer_id):
        pass

    def get_customer_by_id(self, customer_id):
        pass

    def update_customer_info(self, customer_id, new_email, new_phone, new_address):
        pass
