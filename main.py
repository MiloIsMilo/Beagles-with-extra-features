from username import username
from get_secret_number import get_secret_number
from get_clues import get_clues

digits_number = 3   # The number of digits you will have to guess
max_guesses = 10    # The amount of 'lives' you will have to guess correct number


def main():
    print("""I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues: 
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.""".format(digits_number))
    print("For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.")

    # Scores for total of all wins and wins in a row
    winner_score = 0
    win_in_a_row_score = 0
    player = username()

    while True:  # Main game loop
        # This scores the secret number the player needs to guess
        secret_num = get_secret_number(digits_number)
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(max_guesses))

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != digits_number or not guess.isdecimal():
                print('Guess #{}: '.format(num_guesses))
                guess = input('> ')

            clues = get_clues(guess, secret_num, player)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                winner_score += 1
                win_in_a_row_score += 1
                print('Your winner score: {}'.format(winner_score))
                print('Wins in a row: {}'.format(win_in_a_row_score))
                break   # They're correct, so break out of this loop.
            if num_guesses > max_guesses:
                print('You ran out of guesses {}.'.format(player))
                print('The answer was {}.'.format(secret_num))
                print('Your winner score: {}'.format(winner_score))
                win_in_a_row_score = 0

            # Ask player if they want to play again.
        print('Do you want to play again? (yes/no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing {}'.format(player))


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
