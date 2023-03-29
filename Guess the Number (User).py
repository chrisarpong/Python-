import random  

def guess(x): 
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('sorry, guess again. Too Low.')
        elif guess > random_number:
            print('sorry, guess again. Too high.')

    print(f'Congratulation, you have won the Jackpot. {random_number} Join us in our Bio for the Grand price!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 
    print(f'Congratulatiion! The computer guessed your number, {guess}, correctly!')


computer_guess(10) 
