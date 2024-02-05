from abc import ABC, abstractmethod


class CustomerDAO(ABC):
    @abstractmethod
    def add_customer(self, customer):
        pass

    @abstractmethod
    def delete_customer(self, customer):
        pass

    @abstractmethod
    def get_all_customers(self):
        pass


class ProductDAO(ABC):
    @abstractmethod
    def add_products(self, product):
        pass

    @abstractmethod
    def delete_products(self, product_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass


class OrderDAO(ABC):
    @abstractmethod
    def create_orders(self, order, order_details):
        pass

    @abstractmethod
    def display_orders(self):
        pass


class OrderdetailsDAO(ABC):
    @abstractmethod
    def GetAllOrderDetail(self):
        pass


class InventoryDAO(ABC):
    @abstractmethod
    def get_inventory_info(self, inventory_id):
        pass
