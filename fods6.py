item_prices = [10.0, 15.5, 7.8]  
quantities = [2, 3, 1]           
discount_rate = 10               
tax_rate = 5                     
subtotal = sum([price * qty for price, qty in zip(item_prices, quantities)])
discount = (discount_rate / 100) * subtotal
subtotal_after_discount = subtotal - discount
tax = (tax_rate / 100) * subtotal_after_discount
total_cost = subtotal_after_discount + tax
print("Total cost of purchase:", total_cost)
