"""
Simple JSON-based data storage for the ERP system.
"""
import json
import os
from typing import List, Dict, Any, Optional
from models import Product, Customer, Order


class DataStorage:
    """Handles data persistence using JSON files."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.products_file = os.path.join(data_dir, "products.json")
        self.customers_file = os.path.join(data_dir, "customers.json")
        self.orders_file = os.path.join(data_dir, "orders.json")
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Initialize empty files if they don't exist
        self._init_file(self.products_file)
        self._init_file(self.customers_file)
        self._init_file(self.orders_file)
    
    def _init_file(self, filename: str):
        """Initialize a JSON file with empty list if it doesn't exist."""
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump([], f)
    
    def _load_json(self, filename: str) -> List[Dict[str, Any]]:
        """Load data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_json(self, filename: str, data: List[Dict[str, Any]]):
        """Save data to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    # Product storage methods
    def save_product(self, product: Product):
        """Save a product to storage."""
        products_data = self._load_json(self.products_file)
        
        # Update existing product or add new one
        for i, existing_product in enumerate(products_data):
            if existing_product['product_id'] == product.product_id:
                products_data[i] = product.to_dict()
                break
        else:
            products_data.append(product.to_dict())
        
        self._save_json(self.products_file, products_data)
    
    def load_product(self, product_id: str) -> Optional[Product]:
        """Load a specific product by ID."""
        products_data = self._load_json(self.products_file)
        for product_data in products_data:
            if product_data['product_id'] == product_id:
                return Product.from_dict(product_data)
        return None
    
    def load_all_products(self) -> List[Product]:
        """Load all products from storage."""
        products_data = self._load_json(self.products_file)
        return [Product.from_dict(product_data) for product_data in products_data]
    
    def delete_product(self, product_id: str) -> bool:
        """Delete a product from storage."""
        products_data = self._load_json(self.products_file)
        original_length = len(products_data)
        products_data = [p for p in products_data if p['product_id'] != product_id]
        
        if len(products_data) < original_length:
            self._save_json(self.products_file, products_data)
            return True
        return False
    
    # Customer storage methods
    def save_customer(self, customer: Customer):
        """Save a customer to storage."""
        customers_data = self._load_json(self.customers_file)
        
        # Update existing customer or add new one
        for i, existing_customer in enumerate(customers_data):
            if existing_customer['customer_id'] == customer.customer_id:
                customers_data[i] = customer.to_dict()
                break
        else:
            customers_data.append(customer.to_dict())
        
        self._save_json(self.customers_file, customers_data)
    
    def load_customer(self, customer_id: str) -> Optional[Customer]:
        """Load a specific customer by ID."""
        customers_data = self._load_json(self.customers_file)
        for customer_data in customers_data:
            if customer_data['customer_id'] == customer_id:
                return Customer.from_dict(customer_data)
        return None
    
    def load_all_customers(self) -> List[Customer]:
        """Load all customers from storage."""
        customers_data = self._load_json(self.customers_file)
        return [Customer.from_dict(customer_data) for customer_data in customers_data]
    
    def delete_customer(self, customer_id: str) -> bool:
        """Delete a customer from storage."""
        customers_data = self._load_json(self.customers_file)
        original_length = len(customers_data)
        customers_data = [c for c in customers_data if c['customer_id'] != customer_id]
        
        if len(customers_data) < original_length:
            self._save_json(self.customers_file, customers_data)
            return True
        return False
    
    # Order storage methods
    def save_order(self, order: Order):
        """Save an order to storage."""
        orders_data = self._load_json(self.orders_file)
        
        # Update existing order or add new one
        for i, existing_order in enumerate(orders_data):
            if existing_order['order_id'] == order.order_id:
                orders_data[i] = order.to_dict()
                break
        else:
            orders_data.append(order.to_dict())
        
        self._save_json(self.orders_file, orders_data)
    
    def load_order(self, order_id: str) -> Optional[Order]:
        """Load a specific order by ID."""
        orders_data = self._load_json(self.orders_file)
        for order_data in orders_data:
            if order_data['order_id'] == order_id:
                return Order.from_dict(order_data)
        return None
    
    def load_all_orders(self) -> List[Order]:
        """Load all orders from storage."""
        orders_data = self._load_json(self.orders_file)
        return [Order.from_dict(order_data) for order_data in orders_data]
    
    def load_customer_orders(self, customer_id: str) -> List[Order]:
        """Load all orders for a specific customer."""
        orders_data = self._load_json(self.orders_file)
        customer_orders = [order_data for order_data in orders_data if order_data['customer_id'] == customer_id]
        return [Order.from_dict(order_data) for order_data in customer_orders]
    
    def delete_order(self, order_id: str) -> bool:
        """Delete an order from storage."""
        orders_data = self._load_json(self.orders_file)
        original_length = len(orders_data)
        orders_data = [o for o in orders_data if o['order_id'] != order_id]
        
        if len(orders_data) < original_length:
            self._save_json(self.orders_file, orders_data)
            return True
        return False