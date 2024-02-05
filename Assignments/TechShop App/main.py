import mysql.connector
from entity.Customers import Customer
from dao.ServiceProviderImpl import CustomerDAOImpl, ProductDAOImpl, OrderDAOImpl, OrderdetailsDAOImpl, InventoryDAOImpl
from entity.OrderDetails import OrderDetail
from entity.Orders import Order
from entity.Product import Product
from datetime import datetime


class MainClass:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rupen',
            database='techshop'
        )
        self.customers_dao = CustomerDAOImpl(self.connection)
        self.products_dao = ProductDAOImpl(self.connection)
        self.orders_dao = OrderDAOImpl(self.connection)
        self.order_detail_dao = OrderdetailsDAOImpl(self.connection)
        self.inventory_dao = InventoryDAOImpl(self.connection)

    @staticmethod
    def display_menu():
        print("\n++++++++++Welcome to TechShop Management System++++++++++++")
        print("1. Manage Customers")
        print("2. Manage Products")
        print("3. Manage Orders")
        print("4. Manage Order Details")
        print("5. Manage Inventory")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.manage_customers()
            elif choice == '2':
                self.manage_product()
            elif choice == '3':
                self.manage_orders()
            elif choice == '4':
                self.manage_order_details()
            elif choice == '5':
                self.manage_inventory()
            elif choice == '6':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                """elif choice == '4':
                    self.manage_inventory()"""

    def manage_customers(self):
        print("\n+++++++++++++++++CUSTOMER MENU+++++++++++++++++++")
        while True:
            print("\nMenu:")
            print("1. Add Customer(C)")
            print("2. Get all Customer Details(R)")
            print("3. Update Customer Information(U)")
            print("4. Delete Customer(D)")
            print("5. View Specific Customer Details")
            print("6. Calculate Total Orders")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone: ")
                address = input("Enter Address: ")
                customer = Customer(None, first_name, last_name, email, phone, address)
                self.customers_dao.add_customer(customer)
                print("Customer added successfully.")

            elif choice == "2":
                customers = self.customers_dao.get_all_customers()
                if customers:
                    for customer in customers:
                        customer_id, first_name, last_name, email, phone, address = customer
                        print(
                            f"Customer ID: {customer_id} || Name: {first_name} {last_name} || Email: {email} ||"
                            f" Phone: {phone} || Address: {address}")
                else:
                    print("No customers found")

            elif choice == "3":
                customer_id = int(input("Enter Customer ID: "))
                if self.customers_dao.get_customer_by_id(customer_id):
                    new_email = input("Enter new Email (leave blank to keep unchanged): ").strip() or None
                    new_phone = input("Enter new Phone (leave blank to keep unchanged): ").strip() or None
                    new_address = input("Enter new Address (leave blank to keep unchanged): ").strip() or None
                    self.customers_dao.update_customer_info(customer_id, new_email, new_phone, new_address)
                    print("Customer information updated successfully.")
                else:
                    print("Not found.")

            elif choice == "4":
                customer_id = int(input("Enter Customer ID: "))
                if self.customers_dao.get_customer_by_id(customer_id):
                    self.customers_dao.delete_customer(customer_id)
                    print("Customer deleted successfully.")
                else:
                    print("id not found")

            elif choice == "5":
                customer_id = int(input("Enter Customer ID: "))
                customer = self.customers_dao.get_customer_by_id(customer_id)
                if customer:
                    print(f"Customer ID: {customer.CustomerID} \n"
                          f"First Name: {customer.FirstName} \n" 
                          f"Last Name: {customer.LastName} \n" 
                          f"Email: {customer.Email} \n" 
                          f"Phone: {customer.Phone} \n"
                          f"Address: {customer.Address} \n")
                else:
                    print("Customer not found.")

            elif choice == "6":
                customer_id = int(input("Enter Customer ID: "))
                if self.customers_dao.get_customer_by_id(customer_id):
                    total_orders = self.customers_dao.calculate_total_orders(customer_id)
                    print(f"Total orders for customer {customer_id}: {total_orders}")
                else:
                    print("Customer not found.")

            elif choice == "7":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def manage_product(self):
        print("\n+++++++++++++++++PRODUCT MENU+++++++++++++++++++")
        while True:
            print("\nMenu:")
            print("1. Add Product(C)")
            print("2. Get all Product Details(R)")
            print("3. Update Product Information(U)")
            print("4. Delete Product(D)")
            print("5. View Specific Product Details")
            print("6. Is Product In Stock?")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                product_name = input("Enter Product Name: ")
                description = input("Enter the Description: ")
                price = float(input("Enter the Price: "))
                product = Product(None, product_name, description, price)
                self.products_dao.add_products(product)
                print("Product added successfully.")

            elif choice == "2":
                products = self.products_dao.get_all_products()
                if products:
                    for product in products:
                        product_id, product_name, description, price = product
                        print(f"Product ID: {product_id} || Name: {product_name} || Description: {description} || "
                              f"Price: {price}")
                else:
                    print("No Product found")

            elif choice == "3":
                product_id = int(input("Enter Product ID: "))
                if self.products_dao.get_product_by_id(product_id):
                    new_price = input("Enter new Price (leave blank to keep unchanged): ").strip() or None
                    self.products_dao.update_product_info(product_id, new_price)
                    print("Product information updated successfully.")
                else:
                    print("Not found.")

            elif choice == "4":
                product_id = int(input("Enter Product ID: "))
                if self.products_dao.get_product_by_id(product_id):
                    self.products_dao.delete_products(product_id)
                    print("Product deleted successfully.")
                else:
                    print("Product not found")

            elif choice == "5":
                product_id = int(input("Enter Product ID: "))
                product = self.products_dao.get_product_by_id(product_id)
                if product:
                    print(f"Product ID: {product.ProductID} \n Name: {product.ProductName} \n Description: "
                          f"{product.Description} \n Price: {product.Price}")
                else:
                    print("Product not found.")

            elif choice == "6":
                product_id = int(input("Enter Product ID: "))
                if self.products_dao.get_product_by_id(product_id):
                    if self.products_dao.is_product_in_stock(product_id):
                        print("Currently in Stock")
                    else:
                        print("Out of Stock")
                else:
                    print("Product not found.")

            elif choice == "7":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def manage_orders(self):
        print("\n+++++++++++++++++ORDER MENU+++++++++++++++++++")
        while True:
            print("\nMenu:")
            print("1. Create Order(C)")
            print("2. Display Orders(R)")
            print("3  Cancel Order(D)")
            print("4. Get Order Details")
            print("5. Calculate Total Amount")
            print("6. UpdateOrderStatus (Processed/ shipped)")
            print("7. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                customer_id = input("Enter Customer id: ")
                order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                order_details = []
                while True:
                    product_id = input("Enter Product ID: ")
                    quantity = int(input("Enter Quantity: "))
                    order_detail = OrderDetail(None, None, product_id, quantity)
                    order_details.append(order_detail)
                    add_more = input("Add more products? (yes/no): ").lower()
                    if add_more != 'yes':
                        break
                order = Order(None, customer_id, order_date, None)
                self.orders_dao.create_orders(order, order_details)
                print("Order added successfully.")

            elif choice == "2":
                orders = self.orders_dao.display_orders()
                if orders:
                    for order in orders:
                        order_id, customer_id, order_date, total_amount = order
                        print(
                            f"Order ID: {order_id} || Customer ID: "
                            f"{customer_id} || Order Date: {order_date} || Total Amount: {total_amount}")
                else:
                    print("No Order found")

            elif choice == "3":
                order_id = int(input("Enter Order ID: "))
                if self.orders_dao.GetOrderDetails(order_id):
                    self.orders_dao.CancelOrder(order_id)
                    print("Order cancelled successfully.")
                else:
                    print("Order not found")

            elif choice == "4":
                order_id = int(input("Enter Order ID: "))
                orders = self.orders_dao.GetOrderDetails(order_id)
                if orders:
                    for order in orders:
                        print("Order ID:", order.orderID)
                        print("Customer ID:", order.CustomerID)
                        print("Order Date:", order.orderDate)
                        print("Total Amount:", order.TotalAmount)
                else:
                    print("Order not found for this customer.")

            elif choice == "5":
                print(self.orders_dao.CalculateTotalAmount())
            elif choice == "6":
                order_id = int(input("Enter Order ID: "))
                print(self.orders_dao.UpdateOrderStatus(order_id))

            elif choice == "7":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def manage_order_details(self):
        print("\n+++++++++++++++++ORDER DETAILS MENU+++++++++++++++++++")
        while True:
            print("\nMenu:")
            print("1. Calculate Subtotal")
            print("2. Get Order Detail Info")
            print("3. Update Quantity")
            print("4. Add Discount")
            print("5. Display All OderDetails")
            print("6. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                order_detail_id = int(input("Enter Order Detail ID: "))
                subtotal = self.order_detail_dao.CalculateSubtotal(order_detail_id)
                if subtotal is not None:
                    print("Subtotal:", subtotal)
                else:
                    print("Order detail not found.")

            elif choice == "2":
                order_detail_id = int(input("Enter Order Detail ID: "))
                if self.order_detail_dao.GetOrderDetailInfo(order_detail_id):
                    self.order_detail_dao.GetOrderDetailInfo(order_detail_id)
                else:
                    print("No orders with this ID")

            elif choice == "3":
                order_detail_id = int(input("Enter Order Detail ID: "))
                if self.order_detail_dao.GetOrderDetailInfo(order_detail_id):
                    new_quantity = int(input("Enter new quantity: "))
                    self.order_detail_dao.UpdateQuantity(order_detail_id, new_quantity)
                else:
                    print("No orders with this ID")
            elif choice == "4":
                order_detail_id = int(input("Enter Order Detail ID: "))
                if self.order_detail_dao.GetOrderDetailInfo(order_detail_id):
                    discount_percentage = float(input("Enter discount percentage: "))
                    self.order_detail_dao.AddDiscount(order_detail_id, discount_percentage)
                else:
                    print("No orders with this ID")

            elif choice == "5":
                orders = self.order_detail_dao.GetAllOrderDetail()
                if orders:
                    for order in orders:
                        print(f"Order Detail ID:{order[0]} || "
                              f"Order ID:{order[1]} || "
                              f"Product ID: {order[2]} ||"
                              f"Quantity: {order[3]}")
                else:
                    print("No Order found")

            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def manage_inventory(self):
        print("\n+++++++++++++++++INVENTORY MENU+++++++++++++++++++")
        while True:
            print("\nMenu:")
            print("0. Show Inventory Table ")
            print("1. List all products in inventory")
            print("2. Get product details")
            print("3. Add product to inventory")
            print("4. Remove product from inventory")
            print("5. Update stock quantity")
            print("6. Check product availability")
            print("7. Calculate inventory value")
            print("8. List low stock products")
            print("9. List out-of-stock products")
            print("A. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                inventory_id = input("Enter Inventory ID: ")
                if self.inventory_dao.get_inventory_info(inventory_id):
                    self.inventory_dao.list_all_products()
                else:
                    print("Inventory ID not found")
            elif choice == "2":
                inventory_id = input("Enter Inventory ID: ")
                if self.inventory_dao.get_inventory_info(inventory_id):
                    self.inventory_dao.get_product(inventory_id)
                else:
                    print("Inventory ID not found")
            elif choice == "3":
                inventory_id = input("Enter Inventory ID: ")
                if self.inventory_dao.get_inventory_info(inventory_id):
                    quantity = int(input("Enter quantity to add: "))
                    self.inventory_dao.add_to_inventory(inventory_id, quantity)
                else:
                    print("Inventory ID not found")
            elif choice == "4":
                inventory_id = input("Enter Inventory ID: ")
                if self.inventory_dao.get_inventory_info(inventory_id):
                    product_id = input("Enter product ID: ")
                    quantity = int(input("Enter quantity to remove: "))
                    self.inventory_dao.remove_from_inventory(product_id, quantity)
                else:
                    print("Inventory ID not found")
            elif choice == "5":
                inventory_id = input("Enter Inventory ID: ")
                if self.inventory_dao.get_inventory_info(inventory_id):
                    new_quantity = int(input("Enter new quantity: "))
                    self.inventory_dao.update_stock_quantity(inventory_id, new_quantity)
                else:
                    print("Inventory ID not found")
            elif choice == "6":
                inventory_id = input("Enter Inventory ID: ")
                if self.inventory_dao.get_inventory_info(inventory_id):
                    quantity_to_check = int(input("Enter quantity to check: "))
                    self.inventory_dao.is_product_available(inventory_id, quantity_to_check)
                else:
                    print("Inventory ID not found")
            elif choice == "7":
                inventory_id = input("Enter Inventory ID: ")
                if self.inventory_dao.get_inventory_info(inventory_id):
                    print(self.inventory_dao.get_inventory_value(inventory_id))
                else:
                    print("Inventory ID not found")
            elif choice == "8":
                threshold = int(input("Enter threshold for low stock: "))
                self.inventory_dao.list_low_stock_products(threshold)
            elif choice == "9":
                self.inventory_dao.list_out_of_stock_products()
            elif choice == "0":
                inventory = self.inventory_dao.get_inventory_info(0)
                if inventory:
                    for item in inventory:
                        inventory_id, product_name, description, quantity_in_stock = item
                        print(
                            f"Inventory ID: {inventory_id} ||"
                            f" Product Name: {product_name} ||"
                            f" Description: {description} ||"
                            f" Quantity in Stock: {quantity_in_stock}")
                else:
                    print("No Product found")
            elif choice == "A":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == '__main__':
    menu = MainClass()
    menu.run()
