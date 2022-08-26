import json


def username():
    filename = 'username.json'
    try:
        with open(filename, 'r') as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        with open('user/' + filename, 'w') as file_object:
            username = input("Enter your nickname:\n>>> ")
            json.dump(username.title(), file_object)
    else:
        print('Your nickname: ' + username.title())
        while True:
            try:
                choice = input('Do you want to change your nickname? (yes/no): ')
                if choice.lower().startswith('y'):
                    with open(filename, 'w') as file_object:
                        username = input("Enter your nickname:\n>>> ")
                        json.dump(username.title(), file_object)
                        break
                elif choice.lower().startswith('n'):
                    break
            except ValueError:
                print("Error! Please type (yes/no)!")

    return username.title()
