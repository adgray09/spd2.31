# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
def get_price():
    base_price = quantity * item_price
    price = 0
    discount_factor = 0
    if base_price > 1000: 
        discount_factor = 0.95
        price = base_price * discount_factor
    else: 
        discount_factor = 0.98
        price = base_price * discount_factor
    return price

