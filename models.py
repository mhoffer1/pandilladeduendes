"""
Core data models for the simple ERP system.
"""
from datetime import datetime
from typing import List, Dict, Any


class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, product_id: str, name: str, description: str, price: float, stock_quantity: int = 0):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity
        self.created_at = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert product to dictionary for storage."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock_quantity': self.stock_quantity,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Product':
        """Create product from dictionary."""
        product = cls(
            product_id=data['product_id'],
            name=data['name'],
            description=data['description'],
            price=data['price'],
            stock_quantity=data['stock_quantity']
        )
        product.created_at = datetime.fromisoformat(data['created_at'])
        return product
    
    def __str__(self) -> str:
        return f"Product({self.product_id}: {self.name}, Stock: {self.stock_quantity}, Price: ${self.price:.2f})"


class Customer:
    """Represents a customer in the system."""
    
    def __init__(self, customer_id: str, name: str, email: str, phone: str = "", address: str = ""):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.created_at = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert customer to dictionary for storage."""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Customer':
        """Create customer from dictionary."""
        customer = cls(
            customer_id=data['customer_id'],
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', ''),
            address=data.get('address', '')
        )
        customer.created_at = datetime.fromisoformat(data['created_at'])
        return customer
    
    def __str__(self) -> str:
        return f"Customer({self.customer_id}: {self.name}, {self.email})"


class OrderItem:
    """Represents an item in an order."""
    
    def __init__(self, product_id: str, quantity: int, unit_price: float):
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = quantity * unit_price
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert order item to dictionary for storage."""
        return {
            'product_id': self.product_id,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'total_price': self.total_price
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'OrderItem':
        """Create order item from dictionary."""
        return cls(
            product_id=data['product_id'],
            quantity=data['quantity'],
            unit_price=data['unit_price']
        )
    
    def __str__(self) -> str:
        return f"OrderItem(Product: {self.product_id}, Qty: {self.quantity}, Total: ${self.total_price:.2f})"


class Order:
    """Represents a sales order."""
    
    def __init__(self, order_id: str, customer_id: str, items: List[OrderItem] = None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items or []
        self.created_at = datetime.now()
        self.status = "pending"  # pending, completed, cancelled
        self.total_amount = self.calculate_total()
    
    def add_item(self, item: OrderItem):
        """Add an item to the order."""
        self.items.append(item)
        self.total_amount = self.calculate_total()
    
    def calculate_total(self) -> float:
        """Calculate the total amount of the order."""
        return sum(item.total_price for item in self.items)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert order to dictionary for storage."""
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'items': [item.to_dict() for item in self.items],
            'created_at': self.created_at.isoformat(),
            'status': self.status,
            'total_amount': self.total_amount
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Order':
        """Create order from dictionary."""
        items = [OrderItem.from_dict(item_data) for item_data in data.get('items', [])]
        order = cls(
            order_id=data['order_id'],
            customer_id=data['customer_id'],
            items=items
        )
        order.created_at = datetime.fromisoformat(data['created_at'])
        order.status = data.get('status', 'pending')
        order.total_amount = data.get('total_amount', order.calculate_total())
        return order
    
    def __str__(self) -> str:
        return f"Order({self.order_id}: Customer {self.customer_id}, Items: {len(self.items)}, Total: ${self.total_amount:.2f}, Status: {self.status})"