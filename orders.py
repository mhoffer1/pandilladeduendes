"""
Order management module for the ERP system.
"""
from typing import List, Optional
from models import Order, OrderItem
from storage import DataStorage
from inventory import InventoryManager
from customers import CustomerManager


class OrderManager:
    """Manages order operations."""
    
    def __init__(self, storage: DataStorage, inventory_manager: InventoryManager, customer_manager: CustomerManager):
        self.storage = storage
        self.inventory_manager = inventory_manager
        self.customer_manager = customer_manager
    
    def create_order(self, order_id: str, customer_id: str) -> Optional[Order]:
        """Create a new order."""
        # Validate customer exists
        if not self.customer_manager.validate_customer_exists(customer_id):
            return None
        
        order = Order(order_id, customer_id)
        self.storage.save_order(order)
        return order
    
    def add_item_to_order(self, order_id: str, product_id: str, quantity: int) -> bool:
        """Add an item to an existing order."""
        order = self.storage.load_order(order_id)
        if not order:
            return False
        
        # Check if product exists and get its price
        product = self.inventory_manager.get_product(product_id)
        if not product:
            return False
        
        # Check if enough stock is available
        if product.stock_quantity < quantity:
            return False
        
        # Create order item
        order_item = OrderItem(product_id, quantity, product.price)
        order.add_item(order_item)
        
        # Update order in storage
        self.storage.save_order(order)
        return True
    
    def complete_order(self, order_id: str) -> bool:
        """Complete an order and update inventory."""
        order = self.storage.load_order(order_id)
        if not order or order.status != "pending":
            return False
        
        # Check stock availability for all items
        for item in order.items:
            stock = self.inventory_manager.check_stock(item.product_id)
            if stock is None or stock < item.quantity:
                return False
        
        # Remove stock for all items
        for item in order.items:
            if not self.inventory_manager.remove_stock(item.product_id, item.quantity):
                # This shouldn't happen if we checked above, but just in case
                return False
        
        # Update order status
        order.status = "completed"
        self.storage.save_order(order)
        return True
    
    def cancel_order(self, order_id: str) -> bool:
        """Cancel an order."""
        order = self.storage.load_order(order_id)
        if not order:
            return False
        
        order.status = "cancelled"
        self.storage.save_order(order)
        return True
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """Get an order by ID."""
        return self.storage.load_order(order_id)
    
    def get_all_orders(self) -> List[Order]:
        """Get all orders."""
        return self.storage.load_all_orders()
    
    def get_customer_orders(self, customer_id: str) -> List[Order]:
        """Get all orders for a specific customer."""
        return self.storage.load_customer_orders(customer_id)
    
    def get_orders_by_status(self, status: str) -> List[Order]:
        """Get orders by status."""
        all_orders = self.storage.load_all_orders()
        return [order for order in all_orders if order.status == status]
    
    def delete_order(self, order_id: str) -> bool:
        """Delete an order."""
        return self.storage.delete_order(order_id)
    
    def get_order_total(self, order_id: str) -> Optional[float]:
        """Get the total amount of an order."""
        order = self.storage.load_order(order_id)
        if not order:
            return None
        return order.total_amount
    
    def remove_item_from_order(self, order_id: str, product_id: str) -> bool:
        """Remove an item from an order."""
        order = self.storage.load_order(order_id)
        if not order or order.status != "pending":
            return False
        
        # Find and remove the item
        original_length = len(order.items)
        order.items = [item for item in order.items if item.product_id != product_id]
        
        if len(order.items) < original_length:
            order.total_amount = order.calculate_total()
            self.storage.save_order(order)
            return True
        return False
    
    def get_sales_report(self) -> dict:
        """Generate a sales report."""
        all_orders = self.storage.load_all_orders()
        completed_orders = [order for order in all_orders if order.status == "completed"]
        pending_orders = [order for order in all_orders if order.status == "pending"]
        cancelled_orders = [order for order in all_orders if order.status == "cancelled"]
        
        total_revenue = sum(order.total_amount for order in completed_orders)
        pending_revenue = sum(order.total_amount for order in pending_orders)
        
        # Calculate product sales
        product_sales = {}
        for order in completed_orders:
            for item in order.items:
                if item.product_id not in product_sales:
                    product_sales[item.product_id] = 0
                product_sales[item.product_id] += item.quantity
        
        return {
            'total_orders': len(all_orders),
            'completed_orders': len(completed_orders),
            'pending_orders': len(pending_orders),
            'cancelled_orders': len(cancelled_orders),
            'total_revenue': total_revenue,
            'pending_revenue': pending_revenue,
            'top_products': sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]
        }