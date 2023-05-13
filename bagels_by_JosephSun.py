#bagels_by_JosephSun

import random


num_digits=3 #猜測三位數
max_guesses = 10 #最多可以猜十次

def main():
    print('''Bagels, a logic game. 
    
I am thinking of a {}-digit number with no repeated digits. 
Try to guess what it is. Here are some clues:
When I say:         That Means:            
  Pico              One digits is correct but in the wrong position.
  Fermi             One digits is correct and in the right position.
  Bagels            No digit is correct.
For example, if the secret number was 701 and your guess was 021, the clues would be
Fermi Pico'''.format(num_digits))

    while True:
        secretNum= getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(max_guesses))

        numGuess=1
        while numGuess <= max_guesses:
            guess=''

            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}:'.format(numGuess))
                guess = input('> ')
                

            clues = getClues(guess, secretNum)
            print(clues)
            numGuess+=1

            if guess==secretNum:
                break
            if numGuess>max_guesses:
                print('You ran out of guesses.')
                print('The answer was{}'.format(secretNum))
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of num_digits unique random digits."""
    numbers= list('0123456789')
    random.shuffle(numbers)


    secretNum=''
    for i in range(num_digits):
        secretNum+=str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, and bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues=[]

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagels'

    else:
        clues.sort()
        return '  '.join(clues)

if __name__=='__main__':
    main()

