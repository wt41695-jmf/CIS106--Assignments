# Get employee information
last_name = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
job_level = int(input("Enter job level: "))

# Determine bonus rate
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

# Calculate bonus
bonus = salary * bonus_rate

# Display results
print("Employee Last Name:", last_name)
print(f"Bonus: ${bonus:.2f}")
