#!/usr/bin/env python3
"""
Simple ERP System - Main Application
A command-line interface for managing products, customers, and orders.
"""
import sys
import uuid
from typing import List
from storage import DataStorage
from inventory import InventoryManager
from customers import CustomerManager
from orders import OrderManager


class ERPSystem:
    """Main ERP system controller."""
    
    def __init__(self):
        self.storage = DataStorage()
        self.inventory = InventoryManager(self.storage)
        self.customers = CustomerManager(self.storage)
        self.orders = OrderManager(self.storage, self.inventory, self.customers)
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("           SIMPLE ERP SYSTEM")
        print("="*50)
        print("1. Product Management")
        print("2. Customer Management")
        print("3. Order Management")
        print("4. Reports")
        print("5. Exit")
        print("="*50)
    
    def product_menu(self):
        """Handle product management operations."""
        while True:
            print("\n--- Product Management ---")
            print("1. Add Product")
            print("2. View All Products")
            print("3. View Product")
            print("4. Update Product")
            print("5. Add Stock")
            print("6. Remove Stock")
            print("7. Search Products")
            print("8. Delete Product")
            print("9. Back to Main Menu")
            
            choice = input("\nChoose an option (1-9): ").strip()
            
            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.view_all_products()
            elif choice == "3":
                self.view_product()
            elif choice == "4":
                self.update_product()
            elif choice == "5":
                self.add_stock()
            elif choice == "6":
                self.remove_stock()
            elif choice == "7":
                self.search_products()
            elif choice == "8":
                self.delete_product()
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def customer_menu(self):
        """Handle customer management operations."""
        while True:
            print("\n--- Customer Management ---")
            print("1. Add Customer")
            print("2. View All Customers")
            print("3. View Customer")
            print("4. Update Customer")
            print("5. Search Customers")
            print("6. Delete Customer")
            print("7. Back to Main Menu")
            
            choice = input("\nChoose an option (1-7): ").strip()
            
            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.view_all_customers()
            elif choice == "3":
                self.view_customer()
            elif choice == "4":
                self.update_customer()
            elif choice == "5":
                self.search_customers()
            elif choice == "6":
                self.delete_customer()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def order_menu(self):
        """Handle order management operations."""
        while True:
            print("\n--- Order Management ---")
            print("1. Create Order")
            print("2. View All Orders")
            print("3. View Order")
            print("4. Add Item to Order")
            print("5. Remove Item from Order")
            print("6. Complete Order")
            print("7. Cancel Order")
            print("8. View Customer Orders")
            print("9. Back to Main Menu")
            
            choice = input("\nChoose an option (1-9): ").strip()
            
            if choice == "1":
                self.create_order()
            elif choice == "2":
                self.view_all_orders()
            elif choice == "3":
                self.view_order()
            elif choice == "4":
                self.add_item_to_order()
            elif choice == "5":
                self.remove_item_from_order()
            elif choice == "6":
                self.complete_order()
            elif choice == "7":
                self.cancel_order()
            elif choice == "8":
                self.view_customer_orders()
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def reports_menu(self):
        """Handle reporting operations."""
        while True:
            print("\n--- Reports ---")
            print("1. Inventory Report")
            print("2. Sales Report")
            print("3. Customer Report")
            print("4. Low Stock Alert")
            print("5. Back to Main Menu")
            
            choice = input("\nChoose an option (1-5): ").strip()
            
            if choice == "1":
                self.inventory_report()
            elif choice == "2":
                self.sales_report()
            elif choice == "3":
                self.customer_report()
            elif choice == "4":
                self.low_stock_alert()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
    
    # Product Management Methods
    def add_product(self):
        """Add a new product."""
        try:
            product_id = input("Product ID: ").strip()
            if not product_id:
                print("Product ID cannot be empty.")
                return
            
            # Check if product already exists
            if self.inventory.get_product(product_id):
                print(f"Product with ID '{product_id}' already exists.")
                return
            
            name = input("Product Name: ").strip()
            description = input("Description: ").strip()
            price = float(input("Price: $").strip())
            stock = int(input("Initial Stock (default 0): ").strip() or "0")
            
            product = self.inventory.add_product(product_id, name, description, price, stock)
            print(f"Product added successfully: {product}")
            
        except ValueError:
            print("Invalid input. Please enter valid numbers for price and stock.")
    
    def view_all_products(self):
        """View all products."""
        products = self.inventory.get_all_products()
        if not products:
            print("No products found.")
            return
        
        print(f"\n{'Product ID':<15} {'Name':<20} {'Stock':<8} {'Price':<10} {'Description'}")
        print("-" * 80)
        for product in products:
            print(f"{product.product_id:<15} {product.name:<20} {product.stock_quantity:<8} ${product.price:<9.2f} {product.description}")
    
    def view_product(self):
        """View a specific product."""
        product_id = input("Enter Product ID: ").strip()
        product = self.inventory.get_product(product_id)
        
        if product:
            print(f"\nProduct Details:")
            print(f"ID: {product.product_id}")
            print(f"Name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Price: ${product.price:.2f}")
            print(f"Stock: {product.stock_quantity}")
            print(f"Created: {product.created_at}")
        else:
            print("Product not found.")
    
    def update_product(self):
        """Update product information."""
        product_id = input("Enter Product ID to update: ").strip()
        product = self.inventory.get_product(product_id)
        
        if not product:
            print("Product not found.")
            return
        
        print(f"Current product: {product}")
        print("Leave blank to keep current value.")
        
        name = input(f"New name (current: {product.name}): ").strip()
        description = input(f"New description (current: {product.description}): ").strip()
        price_str = input(f"New price (current: ${product.price:.2f}): ").strip()
        
        try:
            price = float(price_str) if price_str else None
            
            if self.inventory.update_product(product_id, 
                                           name if name else None,
                                           description if description else None,
                                           price):
                print("Product updated successfully.")
            else:
                print("Failed to update product.")
        except ValueError:
            print("Invalid price format.")
    
    def add_stock(self):
        """Add stock to a product."""
        product_id = input("Enter Product ID: ").strip()
        try:
            quantity = int(input("Quantity to add: ").strip())
            if self.inventory.add_stock(product_id, quantity):
                new_stock = self.inventory.check_stock(product_id)
                print(f"Stock added successfully. New stock level: {new_stock}")
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid quantity.")
    
    def remove_stock(self):
        """Remove stock from a product."""
        product_id = input("Enter Product ID: ").strip()
        try:
            quantity = int(input("Quantity to remove: ").strip())
            if self.inventory.remove_stock(product_id, quantity):
                new_stock = self.inventory.check_stock(product_id)
                print(f"Stock removed successfully. New stock level: {new_stock}")
            else:
                print("Product not found or insufficient stock.")
        except ValueError:
            print("Invalid quantity.")
    
    def search_products(self):
        """Search for products."""
        search_term = input("Enter search term: ").strip()
        products = self.inventory.search_products(search_term)
        
        if products:
            print(f"\nFound {len(products)} product(s):")
            for product in products:
                print(f"- {product}")
        else:
            print("No products found.")
    
    def delete_product(self):
        """Delete a product."""
        product_id = input("Enter Product ID to delete: ").strip()
        confirm = input(f"Are you sure you want to delete product '{product_id}'? (y/N): ").strip().lower()
        
        if confirm == 'y':
            if self.inventory.delete_product(product_id):
                print("Product deleted successfully.")
            else:
                print("Product not found.")
        else:
            print("Deletion cancelled.")
    
    # Customer Management Methods
    def add_customer(self):
        """Add a new customer."""
        customer_id = input("Customer ID: ").strip()
        if not customer_id:
            print("Customer ID cannot be empty.")
            return
        
        # Check if customer already exists
        if self.customers.get_customer(customer_id):
            print(f"Customer with ID '{customer_id}' already exists.")
            return
        
        name = input("Customer Name: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone (optional): ").strip()
        address = input("Address (optional): ").strip()
        
        customer = self.customers.add_customer(customer_id, name, email, phone, address)
        print(f"Customer added successfully: {customer}")
    
    def view_all_customers(self):
        """View all customers."""
        customers = self.customers.get_all_customers()
        if not customers:
            print("No customers found.")
            return
        
        print(f"\n{'Customer ID':<15} {'Name':<20} {'Email':<25} {'Phone':<15}")
        print("-" * 80)
        for customer in customers:
            print(f"{customer.customer_id:<15} {customer.name:<20} {customer.email:<25} {customer.phone:<15}")
    
    def view_customer(self):
        """View a specific customer."""
        customer_id = input("Enter Customer ID: ").strip()
        customer = self.customers.get_customer(customer_id)
        
        if customer:
            print(f"\nCustomer Details:")
            print(f"ID: {customer.customer_id}")
            print(f"Name: {customer.name}")
            print(f"Email: {customer.email}")
            print(f"Phone: {customer.phone}")
            print(f"Address: {customer.address}")
            print(f"Created: {customer.created_at}")
        else:
            print("Customer not found.")
    
    def update_customer(self):
        """Update customer information."""
        customer_id = input("Enter Customer ID to update: ").strip()
        customer = self.customers.get_customer(customer_id)
        
        if not customer:
            print("Customer not found.")
            return
        
        print(f"Current customer: {customer}")
        print("Leave blank to keep current value.")
        
        name = input(f"New name (current: {customer.name}): ").strip()
        email = input(f"New email (current: {customer.email}): ").strip()
        phone = input(f"New phone (current: {customer.phone}): ").strip()
        address = input(f"New address (current: {customer.address}): ").strip()
        
        if self.customers.update_customer(customer_id,
                                        name if name else None,
                                        email if email else None,
                                        phone if phone else None,
                                        address if address else None):
            print("Customer updated successfully.")
        else:
            print("Failed to update customer.")
    
    def search_customers(self):
        """Search for customers."""
        search_term = input("Enter search term: ").strip()
        customers = self.customers.search_customers(search_term)
        
        if customers:
            print(f"\nFound {len(customers)} customer(s):")
            for customer in customers:
                print(f"- {customer}")
        else:
            print("No customers found.")
    
    def delete_customer(self):
        """Delete a customer."""
        customer_id = input("Enter Customer ID to delete: ").strip()
        confirm = input(f"Are you sure you want to delete customer '{customer_id}'? (y/N): ").strip().lower()
        
        if confirm == 'y':
            if self.customers.delete_customer(customer_id):
                print("Customer deleted successfully.")
            else:
                print("Customer not found.")
        else:
            print("Deletion cancelled.")
    
    # Order Management Methods
    def create_order(self):
        """Create a new order."""
        order_id = input("Order ID (leave blank for auto-generate): ").strip()
        if not order_id:
            order_id = str(uuid.uuid4())[:8]
        
        customer_id = input("Customer ID: ").strip()
        
        order = self.orders.create_order(order_id, customer_id)
        if order:
            print(f"Order created successfully: {order}")
        else:
            print("Failed to create order. Customer may not exist.")
    
    def view_all_orders(self):
        """View all orders."""
        orders = self.orders.get_all_orders()
        if not orders:
            print("No orders found.")
            return
        
        print(f"\n{'Order ID':<12} {'Customer ID':<15} {'Items':<6} {'Total':<10} {'Status':<10}")
        print("-" * 65)
        for order in orders:
            print(f"{order.order_id:<12} {order.customer_id:<15} {len(order.items):<6} ${order.total_amount:<9.2f} {order.status:<10}")
    
    def view_order(self):
        """View a specific order."""
        order_id = input("Enter Order ID: ").strip()
        order = self.orders.get_order(order_id)
        
        if order:
            print(f"\nOrder Details:")
            print(f"Order ID: {order.order_id}")
            print(f"Customer ID: {order.customer_id}")
            print(f"Status: {order.status}")
            print(f"Created: {order.created_at}")
            print(f"Total Amount: ${order.total_amount:.2f}")
            print(f"\nItems:")
            if order.items:
                for item in order.items:
                    print(f"  - {item}")
            else:
                print("  No items in this order.")
        else:
            print("Order not found.")
    
    def add_item_to_order(self):
        """Add an item to an order."""
        order_id = input("Enter Order ID: ").strip()
        product_id = input("Enter Product ID: ").strip()
        
        try:
            quantity = int(input("Quantity: ").strip())
            if self.orders.add_item_to_order(order_id, product_id, quantity):
                print("Item added to order successfully.")
            else:
                print("Failed to add item. Check if order exists, product exists, and sufficient stock is available.")
        except ValueError:
            print("Invalid quantity.")
    
    def remove_item_from_order(self):
        """Remove an item from an order."""
        order_id = input("Enter Order ID: ").strip()
        product_id = input("Enter Product ID to remove: ").strip()
        
        if self.orders.remove_item_from_order(order_id, product_id):
            print("Item removed from order successfully.")
        else:
            print("Failed to remove item. Order may not exist or may be completed/cancelled.")
    
    def complete_order(self):
        """Complete an order."""
        order_id = input("Enter Order ID to complete: ").strip()
        
        if self.orders.complete_order(order_id):
            print("Order completed successfully. Inventory has been updated.")
        else:
            print("Failed to complete order. Check if order exists, is pending, and sufficient stock is available.")
    
    def cancel_order(self):
        """Cancel an order."""
        order_id = input("Enter Order ID to cancel: ").strip()
        
        if self.orders.cancel_order(order_id):
            print("Order cancelled successfully.")
        else:
            print("Failed to cancel order. Order may not exist.")
    
    def view_customer_orders(self):
        """View orders for a specific customer."""
        customer_id = input("Enter Customer ID: ").strip()
        orders = self.orders.get_customer_orders(customer_id)
        
        if orders:
            print(f"\nOrders for Customer {customer_id}:")
            for order in orders:
                print(f"- {order}")
        else:
            print("No orders found for this customer.")
    
    # Report Methods
    def inventory_report(self):
        """Display inventory report."""
        report = self.inventory.get_inventory_report()
        print("\n--- Inventory Report ---")
        print(f"Total Products: {report['total_products']}")
        print(f"Total Inventory Value: ${report['total_inventory_value']:.2f}")
        print(f"Low Stock Products: {report['low_stock_count']}")
        if report['low_stock_products']:
            print("Low Stock Product IDs:", ", ".join(report['low_stock_products']))
    
    def sales_report(self):
        """Display sales report."""
        report = self.orders.get_sales_report()
        print("\n--- Sales Report ---")
        print(f"Total Orders: {report['total_orders']}")
        print(f"Completed Orders: {report['completed_orders']}")
        print(f"Pending Orders: {report['pending_orders']}")
        print(f"Cancelled Orders: {report['cancelled_orders']}")
        print(f"Total Revenue: ${report['total_revenue']:.2f}")
        print(f"Pending Revenue: ${report['pending_revenue']:.2f}")
        
        if report['top_products']:
            print("\nTop Selling Products:")
            for product_id, quantity in report['top_products']:
                print(f"  {product_id}: {quantity} units sold")
    
    def customer_report(self):
        """Display customer report."""
        report = self.customers.get_customers_report()
        print("\n--- Customer Report ---")
        print(f"Total Customers: {report['total_customers']}")
        print(f"Customers with Phone: {report['customers_with_phone']}")
        print(f"Customers with Address: {report['customers_with_address']}")
    
    def low_stock_alert(self):
        """Display low stock alert."""
        try:
            threshold = int(input("Enter stock threshold (default 5): ").strip() or "5")
            low_stock_products = self.inventory.get_low_stock_products(threshold)
            
            if low_stock_products:
                print(f"\n--- Low Stock Alert (threshold: {threshold}) ---")
                for product in low_stock_products:
                    print(f"⚠️  {product.name} (ID: {product.product_id}) - Stock: {product.stock_quantity}")
            else:
                print(f"No products with stock below {threshold}.")
        except ValueError:
            print("Invalid threshold value.")
    
    def run(self):
        """Run the main application loop."""
        print("Welcome to the Simple ERP System!")
        
        while True:
            self.display_menu()
            choice = input("\nChoose an option (1-5): ").strip()
            
            if choice == "1":
                self.product_menu()
            elif choice == "2":
                self.customer_menu()
            elif choice == "3":
                self.order_menu()
            elif choice == "4":
                self.reports_menu()
            elif choice == "5":
                print("Thank you for using the Simple ERP System!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")


def main():
    """Main entry point."""
    try:
        erp = ERPSystem()
        erp.run()
    except KeyboardInterrupt:
        print("\n\nExiting... Thank you for using the Simple ERP System!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()