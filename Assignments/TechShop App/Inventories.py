class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.__InventoryID = inventory_id
        self.__Product = product
        self.__QuantityInStock = quantity_in_stock
        self.__LastStockUpdate = last_stock_update

    @property
    def InventoryID(self):
        return self.__InventoryID

    @property
    def Product(self):
        return self.__Product

    @property
    def QuantityInStock(self):
        return self.__QuantityInStock

    @property
    def LastStockUpdate(self):
        return self.__LastStockUpdate

    @QuantityInStock.setter
    def QuantityInStock(self, quantity):
        if quantity >= 0:
            self.__QuantityInStock = quantity
        else:
            raise Exception("Quantity must be a non-negative integer.")

    def get_product(self, inventory_id):
        pass

    def get_quantity_in_stock(self, inventory_id):
        pass

    def add_to_inventory(self, inventory_id, quantity):
        pass

    def remove_from_inventory(self, inventory_id, quantity):
        pass

    def update_stock_quantity(self, inventory_id, new_quantity):
        pass

    def is_product_available(self, inventory_id, quantity_to_check):
        pass

    def get_inventory_value(self, inventory_id):
        pass

    def list_low_stock_products(self, threshold):
        pass

    def list_out_of_stock_products(self):
        pass

    def list_all_products(self):
        pass
