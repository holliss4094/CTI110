import random

def generate_quiz(operation):
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    
    if operation == 'add':
        return num1, num2, num1 + num2
    elif operation == 'subtract':
        return num1 + num2, num2, num1
    else:
        return None

def addition_quiz():
    num1, num2, correct_answer = generate_quiz('add')
    return num1, num2, correct_answer

def subtraction_quiz():
    num1, num2, correct_answer = generate_quiz('subtract')
    return num1, num2, correct_answer

def main():
    print("Welcome to the Math Quiz!")

    while True:
        print("\nMenu:")
        print("1. Addition Quiz")
        print("2. Subtraction Quiz")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            num1, num2, correct_answer = addition_quiz()
        elif choice == '2':
            num1, num2, correct_answer = subtraction_quiz()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        guesses = 0
        while True:
            if choice == '1':
                user_answer = int(input(f"{num1} + {num2} = "))
            elif choice == '2':
                user_answer = int(input(f"{num1} - {num2} = "))
            else:
                break  # Exit the inner loop for an invalid choice

            if user_answer == correct_answer:
                guesses += 1
                print(f"Congratulations! That's correct. It took you {guesses} guesses.")
                break
            else:
                guesses += 1
                if user_answer < correct_answer:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")

if __name__ == "__main__":
    main()
