squares = []

for number in range(1,5):
    print(number)

listOfNum = list(range(1,10))
print(listOfNum)

evenNumbers = list(range(2,12,2))
print(evenNumbers)

for value in range(1,11):
    squares.append(value**2)
print(squares)

print(sum(squares))