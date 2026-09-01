from name_function import get_formated_name

print("Please enter 'q' to quit at any time")

while True:
    first = input("Please enter a first name: ")
    if first == 'q':
        break
    last = input("Please enter a last name: ")
    if last == 'q':
        break
    middle = input("Please enter a middle name or press enter to skip: ")
    if middle == 'q':
        break

    if middle == "":
        formatted_name = get_formated_name(first, last)
        print("This is your first and last name: " + formatted_name)
    else:
        formatted_name = get_formated_name(first, last, middle)
        print("This is your first, middle, and last name: " + formatted_name)
    