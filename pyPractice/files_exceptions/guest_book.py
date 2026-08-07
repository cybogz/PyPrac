filename = 'guest_book.txt'
user_input = ""

while user_input != "exit":
    user_input = input("Please enter your name: ")

    with open(filename, 'a') as file_object:
        if user_input != "exit":
            file_object.write(user_input + " has joined\n")
    print("Welcome to the club " + user_input + "\n")