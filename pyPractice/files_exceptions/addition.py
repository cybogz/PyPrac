print("Please enter 2 numbers to add. Press q to quit")

while True:

    first_number = input("Please enter the first number: ")
    if first_number == 'q':
        break
    second_number = input("Please enter the second number: ")
    try:
        added_number = int(first_number) + int(second_number)
    except ValueError:
        print("You cannot enter text to be added")
    else:
        print(added_number) 