class OrderDetail:
    def __init__(self, order_details_id, order_id, product_id, quantity):
        self.__OrderDetailID = order_details_id
        self.__Order = order_id
        self.__ProductID = product_id
        self.__Quantity = quantity

    @property
    def OrderDetailID(self):
        return self.__OrderDetailID

    @property
    def Order(self):
        return self.__Order

    @property
    def ProductID(self):
        return self.__ProductID

    @property
    def Quantity(self):
        return self.__Quantity

    @Quantity.setter
    def Quantity(self, quantity):
        if quantity > 0:
            self.__Quantity = quantity
        else:
            raise Exception("Quantity must be 0 or greater than 0")

    def CalculateSubtotal(self):
        pass

    def GetOrderDetailInfo(self):
        pass

    def UpdateQuantity(self):
        pass

    def AddDiscount(self):
        pass
