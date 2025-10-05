# Code to generate dictionary summary reports
#Generate summary report
orders = [
    {"customer": "lateef", "product": "shoe", "qty": 3, "price": 9.5},
    {"customer": "mariam", "product": "pen", "qty": 10, "price": 3.0},
]

report = {}
report["total_products_sold"] = sum(order["qty"] for order in orders)

highest_qty_order = max(orders, key=lambda order: order["qty"])
report["most_popular_product"] = highest_qty_order["product"]

revenue_per_customer = {}
for order in orders:
    customer = order["customer"]      
    quantity = order["qty"]            
    price = order["price"]            
    revenue_for_this_order = quantity * price
    
    if customer in revenue_per_customer:
        revenue_per_customer[customer] += revenue_for_this_order
    else:
        revenue_per_customer[customer] = revenue_for_this_order

report["revenue_per_customer"] = revenue_per_customer
print(report)


