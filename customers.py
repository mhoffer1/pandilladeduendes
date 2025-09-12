"""
Customer management module for the ERP system.
"""
from typing import List, Optional
from models import Customer
from storage import DataStorage


class CustomerManager:
    """Manages customer operations."""
    
    def __init__(self, storage: DataStorage):
        self.storage = storage
    
    def add_customer(self, customer_id: str, name: str, email: str, phone: str = "", address: str = "") -> Customer:
        """Add a new customer."""
        customer = Customer(customer_id, name, email, phone, address)
        self.storage.save_customer(customer)
        return customer
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Get a customer by ID."""
        return self.storage.load_customer(customer_id)
    
    def get_all_customers(self) -> List[Customer]:
        """Get all customers."""
        return self.storage.load_all_customers()
    
    def update_customer(self, customer_id: str, name: str = None, email: str = None, 
                       phone: str = None, address: str = None) -> bool:
        """Update customer information."""
        customer = self.storage.load_customer(customer_id)
        if not customer:
            return False
        
        if name is not None:
            customer.name = name
        if email is not None:
            customer.email = email
        if phone is not None:
            customer.phone = phone
        if address is not None:
            customer.address = address
        
        self.storage.save_customer(customer)
        return True
    
    def delete_customer(self, customer_id: str) -> bool:
        """Delete a customer."""
        return self.storage.delete_customer(customer_id)
    
    def search_customers(self, search_term: str) -> List[Customer]:
        """Search customers by name or email."""
        all_customers = self.storage.load_all_customers()
        search_term = search_term.lower()
        
        return [
            customer for customer in all_customers
            if search_term in customer.name.lower() or search_term in customer.email.lower()
        ]
    
    def get_customer_by_email(self, email: str) -> Optional[Customer]:
        """Get a customer by email address."""
        all_customers = self.storage.load_all_customers()
        for customer in all_customers:
            if customer.email.lower() == email.lower():
                return customer
        return None
    
    def validate_customer_exists(self, customer_id: str) -> bool:
        """Check if a customer exists."""
        return self.storage.load_customer(customer_id) is not None
    
    def get_customer_count(self) -> int:
        """Get total number of customers."""
        return len(self.storage.load_all_customers())
    
    def get_customers_report(self) -> dict:
        """Generate a customers report."""
        all_customers = self.storage.load_all_customers()
        
        return {
            'total_customers': len(all_customers),
            'customers_with_phone': len([c for c in all_customers if c.phone]),
            'customers_with_address': len([c for c in all_customers if c.address])
        }