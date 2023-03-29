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

guess(10)
