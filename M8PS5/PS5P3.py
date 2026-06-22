# Forecast next month's sales.

def compute_forecast(month, sales):
    if month in ["Jan", "Feb", "Mar"]:
        percent = 0.10
    elif month in ["Apr", "May", "Jun"]:
        percent = 0.15
    elif month in ["Jul", "Aug", "Sep"]:
        percent = 0.20
    elif month in ["Oct", "Nov", "Dec"]:
        percent = 0.25
    else:
        percent = 0.0

    next_month_sales = sales * (1 + percent)
    return next_month_sales


choice = input("Do you want to enter sales information? yes or no: ")

while choice.lower() == "yes":
    last_name = input("Enter last name: ")
    month = input("Enter month abbreviation, example Jan: ")
    sales = float(input("Enter sales: "))

    forecast = compute_forecast(month, sales)

    print("Last Name:", last_name)
    print("Month:", month)
    print("Next Month Forecast: $", format(forecast, ".2f"))

    choice = input("Do you want to enter another? yes or no: ")
