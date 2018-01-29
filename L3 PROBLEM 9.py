
# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of an integer between 0 and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!


x = 100
numGuesses = 0
low = 0
high = x
ans = int((high + low)/2)
print("Please think of a number between 0 and 100!")
print("is your secret number", str(ans) + "?")
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while guess != 'c':
    if guess == 'h':
        high = ans
    elif guess == 'l':
        low = ans
    else:
        print("Sorry, I did not understand your input.")
    ans = int((high + low) / 2)
    print("is your secret number", str(ans) + "?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
if guess == 'c':
    print("Game over. Your secret number was:", str(ans))
