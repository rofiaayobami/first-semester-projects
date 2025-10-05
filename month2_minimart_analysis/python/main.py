# Entry point for the MiniMart data reporting system
#simulate new orders in a minimart
orders = [
    {"customer": "lateef", "product": "shoe", "qty": 3, "price": 9.5},
    {"customer": "mariam", "product": "pen", "qty": 10, "price": 3.0},
]

#identify large orders
def identify_large_orders(orders):
 for order in orders:
    if order["qty"] > 5 or order["price"] * order["qty"] > 25:
        print(f"Large order: {order['customer']}") 
    else:
        print(f"Regular order: {order['customer']}") 
        


identify_large_orders(orders)
print(orders) 