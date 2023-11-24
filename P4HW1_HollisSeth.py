#CTI-110
#P4HW1 - Score List
#Seth Hollis
#11/24/2023
#


# Ask user to enter the number of scores they would like to enter
num_scores = int(input("How many scores do you want to enter?"))

# Initialize an empty list to store scores
scores = []

# Collect scores from the user
for i in range(1, num_scores + 1):
    while True:
        try:
            # Get a valid score from the user
            score = float(input(f"Enter score #{i}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Display the lowest score entered
lowest_score = min(scores)
print(f"Lowest score entered: {lowest_score}")

# Remove the lowest score from the list
scores.remove(lowest_score)

# Display the modified score list
print("Score List after dropping lowest score:", scores)

# Calculate the average of scores in the modified list
average_score = sum(scores) / len(scores)
print(f"Average score: {average_score:.2f}")

# Determine the letter grade for the calculated average
if 90 <= average_score <= 100:
    print("Letter Grade: A")
elif 80 <= average_score < 90:
    print("Letter Grade: B")
elif 70 <= average_score < 80:
    print("Letter Grade: C")
elif 60 <= average_score < 70:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")
