# Calculate car out-the-door price.

def compute_out_the_door_price(make, model, ev_code, msrp):
    if make == "Honda" and model == "Accord":
        percent_off = 0.10
    elif make == "Toyota" and model == "Rav4":
        percent_off = 0.15
    elif ev_code.upper() == "Y":
        percent_off = 0.30
    else:
        percent_off = 0.05

    discount = msrp * percent_off
    sale_price = msrp - discount
    tax = sale_price * 0.07
    total = sale_price + tax

    return total


sum_msrp = 0.0
sum_sales_price = 0.0

choice = input("Do you want to enter vehicle information? yes or no: ")

while choice.lower() == "yes":
    make = input("Enter make: ")
    model = input("Enter model: ")
    ev_code = input("Is it electric? Y or N: ")
    msrp = float(input("Enter MSRP: "))

    total = compute_out_the_door_price(make, model, ev_code, msrp)

    sum_msrp = sum_msrp + msrp
    sum_sales_price = sum_sales_price + total

    print("Make:", make)
    print("Model:", model)
    print("MSRP: $", format(msrp, ".2f"))
    print("Out-the-door price: $", format(total, ".2f"))

    choice = input("Do you want to enter another vehicle? yes or no: ")

print("Sum of all MSRP values: $", format(sum_msrp, ".2f"))
print("Sum of all sales prices: $", format(sum_sales_price, ".2f"))
