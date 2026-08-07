filename = "programming_polling.txt"
user_input = ""

while user_input != 'q':
    user_input = input("Give me one reason for liking to program. Press 'q' to quit: " )

    with open(filename, 'a') as user_data:
        if user_input != 'q':
            user_data.write(user_input + "\n")

with open(filename) as user_data:
    for line in user_data:
        print(line.strip())
