import json

user_input = input("Enter your username: ")
filename = 'username.json'

with open(filename, 'w') as file_obj:
    json.dump(user_input, file_obj)
    print("we will remember you when you come back " + user_input)