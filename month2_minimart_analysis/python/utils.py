# Utility functions for data conversion and filtering
#apply type conversion and discounts
orders = [
    {"customer": "lateef", "product": "shoe", "qty": 3, "price": 9.5},
    {"customer": "mariam", "product": "pen", "qty": 10, "price": 3.0},
]

def utils_apply_discounts(orders):
 for order in orders:
    order["price"] = float(order["price"])
    if order["qty"] >= 10:
        order["price"] *= 0.9  
    elif order["qty"] >= 5:
        order["price"] *= 0.95
    else:
        order["price"] *= 1.0



utils_apply_discounts(orders)
print(orders)