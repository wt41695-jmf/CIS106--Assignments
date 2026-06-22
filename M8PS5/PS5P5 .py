# This returns discount amount and discounted price.

def compute_discount(quantity, price, discount_rate):
    total = quantity * price
    discount_amount = total * discount_rate
    discounted_price = total - discount_amount
    return discount_amount, discounted_price


quantity = float(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate as decimal, example 0.10: "))

discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)

print("Quantity:", quantity)
print("Price: $", format(price, ".2f"))
print("Discount Amount: $", format(discount_amount, ".2f"))
print("Discounted Price: $", format(discounted_price, ".2f"))
