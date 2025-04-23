import sys

from random import randint

print("\nLets play a game of random numbers! You provide a range of number that you will choose from and see if it was the right guess.\n ")

# generate a number from N1 - N2 (N1 & N2 to be provided by the user)
n1, n2 = map(int, input("Provide two numbers :\t").split())
# n2 = int(input("Print another number : "))
print(f'You choose the range to be between {n1} and {n2}\n')
answer = randint(n1, n2)

# print(answer)



while True:
    # check input is a numbers
    try:
        # input from user
        guess = input(f'\nPlease Guess a number between {n1} ~ {n2} for the game :\t')
        if n1 < int(guess) < n2:
            print(f'\nYou chose the number {guess}')
            # Check if number is the right guess. Otherwise ask again!
            if int(guess) == answer:
                print("You chose the correct number. You are a winner!!!")
                break
            else:
                print("\nUnfortunately, you guessed the wrong number. Lets Continue!")

        else:
            print(f'Hay Stupid! I said {n1} ~ {n2}. Can\'t you read?')
    except ValueError :
        print('You failed to provide a number between 1 - 10. Are you stupid! ')
        continue

