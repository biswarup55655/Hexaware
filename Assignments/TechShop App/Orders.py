class Order:
    def __init__(self, order_id, customer, order_date, total_amount):
        self.__orderID = order_id
        self.__CustomerID = customer
        self.__orderDate = order_date
        self.__TotalAmount = total_amount
        self.__Products = []

    @property
    def orderID(self):
        return self.__orderID

    @property
    def CustomerID(self):
        return self.__CustomerID

    @property
    def orderDate(self):
        return self.__orderDate

    @orderDate.setter
    def orderDate(self, order_date):
        if isinstance(order_date, str):
            self.__orderDate = order_date
        else:
            raise Exception("Invalid input")

    @property
    def TotalAmount(self):
        return self.__TotalAmount

    @TotalAmount.setter
    def TotalAmount(self, total_amount):
        if isinstance(total_amount, (int, float)) and total_amount >= 0:
            self.__TotalAmount = total_amount
        else:
            raise Exception("Must be integer and non negative")

    def setProducts(self, products):
        self.__Products = products

    def GetOrderDetails(self, order_id):
        pass

    def UpdateOrderStatus(self, order_date):
        pass

    def CalculateTotalAmount(self):
        pass

    def CancelOrder(self):
        pass
