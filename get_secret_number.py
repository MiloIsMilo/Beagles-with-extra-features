import random


def get_secret_number(digits_number):
    """Returns a string made up of digits_number unique random digits"""
    numbers = list('0123456789')    # Create a list of digits from 0 to 9
    random.shuffle(numbers)         # Shuffle them into random order.

    # Get the first digits_number digits in the list for the secret number:
    secret_num = ''
    for i in range(digits_number):
        secret_num += str(numbers[i])
    return secret_num
