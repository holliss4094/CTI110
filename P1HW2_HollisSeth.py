# Travel Expense Calculator
# Date: 2023-10-03
# CTI-110 P1HW2 - Travel Expense
# SETH HOLLIS

# Ask the user to enter their budget
budget = float(input("Enter Budget: $"))

# Ask the user to enter the travel destination
destination = input("Enter your travel destination: ")

# Ask the user for the amount they will spend on gas
gas_expense = float(input("How much do you think you will spend on gas?: $"))

# Ask the user for the amount they will spend on accommodation
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel?: $"))

# Ask the user for the amount they will spend on food
food_expense = float(input("Last, how much do you need for food?: $"))

# Calculate the total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from the budget
remaining_budget = budget - total_expenses

# Display results
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial budget: $", budget)
print("Fuel: $", gas_expense)
print("Accommodation: $", accommodation_expense)
print("Food: $", food_expense)
print("Total Expenses: $", total_expenses)
print("Remaining Balance: $", remaining_budget)
