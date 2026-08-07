import json

def get_stored_number():
    
    filename = 'favnumber.json'

    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def new_fav_number():

    filename = 'favnumber.json'

    user_input = input("Please enter your favorite number: ")

    with open(filename, 'w') as f_obj:
        json.dump(user_input, f_obj)

    return user_input

def user_message():

    favorite_number = get_stored_number()

    if favorite_number:
        print(f"Your favorite number is {favorite_number}")
    else:
        favorite_number = new_fav_number()
        print(f"Your favorite number is {favorite_number}")

user_message()






    