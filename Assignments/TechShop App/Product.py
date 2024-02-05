class Product:

    def __init__(self, product_id, name, description, price):
        self.__ProductID = product_id
        self.__ProductName = name
        self.__Description = description
        self.__Price = price

    @property
    def ProductID(self):
        return self.__ProductID

    @property
    def ProductName(self):
        return self.__ProductName

    @ProductName.setter
    def ProductName(self, product_name):
        if isinstance(product_name, str):
            self.__ProductName = product_name
        else:
            raise Exception("PRODUCT NAME MUST BE STRING")

    @property
    def Description(self):
        return self.__Description

    @Description.setter
    def Description(self, product_description):
        if isinstance(product_description, str):
            self.__Description = product_description
        else:
            raise Exception("DESCRIPTION MUST BE STRING")

    @property
    def Price(self):
        return self.__Price

    @Price.setter
    def Price(self, product_price):
        if isinstance(product_price, int) and product_price > 0:
            self.__Price = product_price
        else:
            raise Exception("PRICE MUST BE NUMERIC AND NON NEGATIVE")

    def get_product_by_id(self, product_id):
        pass

    def update_product_info(self, price):
        pass

    def is_product_in_stock(self, product_id):
        pass
