# CTI-110
# P3HW2 - Salary
# Seth Hollis
# 11/07/2023

# Get employee's name, hours worked, and pay rate
employee_name = input("Enter the name of the employee: ")
hours_worked = float(input("Enter the number of hours the employee worked this week: "))
pay_rate = float(input("Enter the employee's pay rate: "))

# Calculate regular pay and overtime pay
if hours_worked <= 40:
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0
else:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display the results
print("Employee Name:", employee_name)
print("Pay Rate:", pay_rate)
print("Number of Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours if hours_worked > 40 else 0)
print("Overtime Pay:", overtime_pay)
print("Pay for Regular Hours:", regular_pay)
print("Gross Pay:", gross_pay)
