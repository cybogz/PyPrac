favNum = {'cyrus': [19, 20, 15],
          'javy': [69, 420, 5],
          'bap': [666, 13, 19]}

for name, numberList in favNum.items():
    print(name + "'s favorite numbers are: ")

    for numbers in numberList:
        print(numbers)

    print()

