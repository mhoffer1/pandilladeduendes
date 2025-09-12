"""
Inventory management module for the ERP system.
"""
from typing import List, Optional
from models import Product
from storage import DataStorage


class InventoryManager:
    """Manages product inventory operations."""
    
    def __init__(self, storage: DataStorage):
        self.storage = storage
    
    def add_product(self, product_id: str, name: str, description: str, price: float, initial_stock: int = 0) -> Product:
        """Add a new product to the inventory."""
        product = Product(product_id, name, description, price, initial_stock)
        self.storage.save_product(product)
        return product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID."""
        return self.storage.load_product(product_id)
    
    def get_all_products(self) -> List[Product]:
        """Get all products in inventory."""
        return self.storage.load_all_products()
    
    def update_product(self, product_id: str, name: str = None, description: str = None, price: float = None) -> bool:
        """Update product information."""
        product = self.storage.load_product(product_id)
        if not product:
            return False
        
        if name is not None:
            product.name = name
        if description is not None:
            product.description = description
        if price is not None:
            product.price = price
        
        self.storage.save_product(product)
        return True
    
    def add_stock(self, product_id: str, quantity: int) -> bool:
        """Add stock to a product."""
        product = self.storage.load_product(product_id)
        if not product:
            return False
        
        product.stock_quantity += quantity
        self.storage.save_product(product)
        return True
    
    def remove_stock(self, product_id: str, quantity: int) -> bool:
        """Remove stock from a product."""
        product = self.storage.load_product(product_id)
        if not product:
            return False
        
        if product.stock_quantity < quantity:
            return False  # Insufficient stock
        
        product.stock_quantity -= quantity
        self.storage.save_product(product)
        return True
    
    def check_stock(self, product_id: str) -> Optional[int]:
        """Check stock level for a product."""
        product = self.storage.load_product(product_id)
        if not product:
            return None
        return product.stock_quantity
    
    def get_low_stock_products(self, threshold: int = 5) -> List[Product]:
        """Get products with low stock levels."""
        all_products = self.storage.load_all_products()
        return [product for product in all_products if product.stock_quantity <= threshold]
    
    def delete_product(self, product_id: str) -> bool:
        """Delete a product from inventory."""
        return self.storage.delete_product(product_id)
    
    def search_products(self, search_term: str) -> List[Product]:
        """Search products by name or description."""
        all_products = self.storage.load_all_products()
        search_term = search_term.lower()
        
        return [
            product for product in all_products
            if search_term in product.name.lower() or search_term in product.description.lower()
        ]
    
    def get_inventory_value(self) -> float:
        """Calculate total inventory value."""
        all_products = self.storage.load_all_products()
        return sum(product.price * product.stock_quantity for product in all_products)
    
    def get_inventory_report(self) -> dict:
        """Generate an inventory report."""
        all_products = self.storage.load_all_products()
        total_products = len(all_products)
        total_value = self.get_inventory_value()
        low_stock_products = self.get_low_stock_products()
        
        return {
            'total_products': total_products,
            'total_inventory_value': total_value,
            'low_stock_count': len(low_stock_products),
            'low_stock_products': [product.product_id for product in low_stock_products]
        }