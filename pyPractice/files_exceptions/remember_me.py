import json

def get__stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name: ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get__stored_username()
    if username:
        print("welcome back " + username)
    else:
        username = get_new_username()
        print("welcome back " + username)

greet_user()