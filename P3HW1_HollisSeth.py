# My Last Name

# This program takes a number grade, determines the average, and displays a letter grade for the average.

# Enter grades for six modules
mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = int(total / len(grades))

# Display lowest grade, highest grade, sum of grades, and average
print('Lowest Grade:', low)
print('Highest Grade:', high)
print('Sum of Grades:', total)
print('Average Grade:', avg)

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
else:
    print('Your grade is: F')

