import random
def main():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    main()
