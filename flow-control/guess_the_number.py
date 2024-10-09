import random

def guess_random():
    secret_num = random.randint(1,20)
    print('I am thinking of a number between 1 and 20.')

    for guess_taken in range(1,7):
        print('Take a guess')
        guess = int(input())
        if guess < secret_num:
            print('your guess is low')
        elif guess > secret_num:
            print('your guess is high')
        else:
            break
    if guess == secret_num:
        print('Good job! You guessed my number in ' + str(guess_taken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secret_num))

def main():
    guess_random()

if __name__ == "__main__":
    main()