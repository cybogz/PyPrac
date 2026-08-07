filename = "guest.txt"

user_input = input("Please enter your name: ")

with open(filename, 'w') as file_object:
    file_object.write(user_input)
    
with open(filename) as file_object:   
    print(file_object.read())