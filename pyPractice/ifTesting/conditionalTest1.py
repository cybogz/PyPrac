car = "datsun"
fruit = "apple"
music = "Metal"
city = "San Diego"
testingNumber = 10
listOfCars = ["bmw", "ford", "toyota", "vw"]


print("Is car == to 'toyota? I think its true")
print(car == "toyota")

print("\nIs fruit == to 'Apple'? I think false")
print(fruit == "Apple")

print("\nIs music.lower() == to 'metal? I think its true")
print(music.lower() == "metal")

if testingNumber < 15:
    print("\nThis number is too small\n")

for numbers in range(1,10):
    if numbers != 5:
        print("These numbers suck")
    else:
        print("Bingo")

if fruit != "peaches":
    print("\nYou have bad taste in fruit\n")

print("toyota" in listOfCars)

for newCar in listOfCars:
    if newCar == "vw":
        print("Youve got a jetta\n")

if car not in listOfCars:
    print(car + " is not on the list")