print("Give me two number, and I'll divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("\First Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Can't divide by 0")
    else:
        print(answer)
