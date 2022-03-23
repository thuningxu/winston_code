from random import randint
number_guessed = False
print('Number Game!')
number = randint(1, 1000)
while True:
    guess = input('Guess a number between 1 and 1000')
    guess = int(guess)
    if guess > number:
        print('Guess lower')
    elif guess < number:
        print('Guess higher')
    else:
        print('You guessed it!')
        break
    
        
