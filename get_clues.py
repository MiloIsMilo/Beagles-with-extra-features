def get_clues(guess, secret_num, player=''):
    """Returns a string with the pico, fermi, beagles clues for a guess and secret number pair."""
    if guess == secret_num:
        return 'You got it right {}!'.format(player)

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order doesn't give information away
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)
