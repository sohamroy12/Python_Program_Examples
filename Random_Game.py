# Second attempt to write the code :: makes the testing easy.
from random import randint


def generate_random_number(n1, n2):
    return randint(n1, n2)


def is_valid_guess(guess, n1, n2):
    return n1 <= guess <= n2


def play_guessing_game(n1, n2, guess, answer):
    if not is_valid_guess(guess, n1, n2):
        return f"Invalid guess! Guess should be between {n1} and {n2}."
    if guess == answer:
        return "Correct! You are a winner!"
    else:
        return "Wrong guess. Try again!"


def get_valid_range():
    while True:
        user_input = input("Provide two numbers (space separated): ").strip()
        try:
            n1, n2 = map(int, user_input.replace(',', ' ').split())
            if n1 >= n2:
                print("First number must be smaller than the second. Try again.")
                continue
            return n1, n2
        except ValueError:
            print("Invalid input. Please enter two integers (e.g., 1 10).")


def main():
    print("\nLet's play a game of random numbers!")

    n1, n2 = get_valid_range()
    print(f"\nYou chose the range to be between {n1} and {n2}")
    answer = generate_random_number(n1, n2)
    # print(answer)

    while True:
        try:
            guess = int(input(f"Guess a number between {n1} and {n2}: "))
            result = play_guessing_game(n1, n2, guess, answer)
            print(result)
            if "Correct!" in result:
                break
        except ValueError:
            print("Please enter a valid Number!.")


if __name__ == "__main__":
    main()

# First attempt of writing the code
# import sys
# from random import randint
#
# print("\nLets play a game of random numbers! You provide a range of number that you will choose from and see if it was the right guess.\n ")
#
# # accept Two numbers from User
# n1, n2 = map(int, input("Provide two numbers :\t").split())
#
# # generate a random number from N1 - N2 (N1 & N2 to be provided by the user)
# def generateRandomNumbers(n1, n2):
#     return randint(n1, n2)
#
# # n2 = int(input("Print another number : "))
# print(f'You choose the range to be between {n1} and {n2}\n')
# answer = randint(n1, n2)
#
# # print(answer)
#
#
#
# while True:
#     # check input is a numbers
#     try:
#         # input from user
#         guess = input(f'\nPlease Guess a number between {n1} ~ {n2} for the game :\t')
#         if n1 < int(guess) < n2:
#             print(f'\nYou chose the number {guess}')
#             # Check if number is the right guess. Otherwise ask again!
#             if int(guess) == answer:
#                 print("You chose the correct number. You are a winner!!!")
#                 break
#             else:
#                 print("\nUnfortunately, you guessed the wrong number. Lets Continue!")
#
#         else:
#             print(f'Hay Stupid! I said {n1} ~ {n2}. Can\'t you read?')
#     except ValueError :
#         print('You failed to provide a number between 1 - 10. Are you stupid! ')
#         continue
#
""""#Note: To write test cases for a script like this, you need to separate the logic from the user interaction. Right now, the code is tightly coupled with input() and print() which makes it hard to test.

✅ Step-by-step to make it testable:
Extract the core logic into functions

Use parameters instead of input()

Return values instead of using print()

Mock input() and randint() during tests
"""