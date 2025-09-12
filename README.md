# Simple ERP System

A lightweight Enterprise Resource Planning (ERP) system built in Python. This system provides basic functionality for managing products, customers, and sales orders through a command-line interface.

## Features

### 📦 Product Management
- Add, view, update, and delete products
- Track inventory levels (stock quantities)
- Add/remove stock with validation
- Search products by name or description
- Low stock alerts
- Inventory valuation

### 👥 Customer Management
- Add, view, update, and delete customers
- Store customer contact information (email, phone, address)
- Search customers by name or email
- Customer reporting

### 📋 Order Management
- Create sales orders
- Add/remove items from orders
- Complete orders (automatically updates inventory)
- Cancel orders
- View order history by customer
- Order status tracking (pending, completed, cancelled)

### 📊 Reporting
- Inventory reports (total value, low stock alerts)
- Sales reports (revenue, top products, order statistics)
- Customer statistics

## Installation & Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd pandilladeduendes
```

2. Run the application:
```bash
python main.py
```

No external dependencies are required - the system uses only Python standard library.

## Usage

Run the main application and navigate through the menu system:

```bash
python main.py
```

### Main Menu Options:
1. **Product Management** - Manage your inventory
2. **Customer Management** - Manage customer information
3. **Order Management** - Create and manage sales orders
4. **Reports** - View business reports and analytics
5. **Exit** - Close the application

### Data Storage

The system uses JSON files for data persistence:
- `data/products.json` - Product inventory data
- `data/customers.json` - Customer information
- `data/orders.json` - Sales order data

Data files are created automatically when you first run the application.

## Example Workflow

1. **Add Products**: Start by adding products to your inventory
   - Set product ID, name, description, price, and initial stock

2. **Add Customers**: Create customer records
   - Store customer ID, name, email, and optional phone/address

3. **Create Orders**: Process sales orders
   - Create order for a customer
   - Add products to the order
   - Complete the order (automatically deducts inventory)

4. **Monitor Business**: Use reports to track
   - Inventory levels and low stock alerts
   - Sales performance and revenue
   - Customer metrics

## File Structure

```
pandilladeduendes/
├── main.py          # Main CLI application
├── models.py        # Data models (Product, Customer, Order)
├── storage.py       # JSON-based data persistence
├── inventory.py     # Product inventory management
├── customers.py     # Customer management
├── orders.py        # Order processing and management
├── data/           # Data storage directory (auto-created)
│   ├── products.json
│   ├── customers.json
│   └── orders.json
└── README.md
```

## Key Classes

- **Product**: Represents inventory items with pricing and stock tracking
- **Customer**: Stores customer contact and identification information
- **Order/OrderItem**: Manages sales transactions and line items
- **InventoryManager**: Handles product operations and stock management
- **CustomerManager**: Manages customer CRUD operations
- **OrderManager**: Processes orders and coordinates with inventory
- **DataStorage**: Provides JSON-based persistence layer

## System Requirements

- Python 3.6 or higher
- No external dependencies required

## Data Validation

The system includes built-in validation:
- Stock levels cannot go negative
- Orders can only be completed if sufficient inventory exists
- Customer and product IDs must be unique
- Required fields are validated during data entry

## Future Enhancements

Potential improvements for the system:
- Web-based user interface
- Database integration (SQLite, PostgreSQL)
- User authentication and authorization
- Multi-location inventory tracking
- Barcode scanning support
- Email notifications
- Advanced reporting and analytics
- Import/export functionality

## Contributing

This is a simple educational ERP system. Feel free to extend and modify it for your needs.

## License

Open source - use and modify as needed.