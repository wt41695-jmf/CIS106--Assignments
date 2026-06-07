# Get principle amount and years to maturity
principle = float(input("Enter principle amount: "))
years = int(input("Enter years to maturity: "))

# Determine interest rate
if principle > 100000 and years == 5:
    interest_rate = 0.06
elif principle >= 50000 and principle <= 100000 and years == 10:
    interest_rate = 0.05
elif principle >= 50000 and principle <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

# Calculate first year interest
interest_amount = principle * interest_rate

# Display results
print(f"Principle: ${principle:.2f}")
print(f"Interest Rate: {interest_rate:.2%}")
print(f"First Year Interest: ${interest_amount:.2f}")
