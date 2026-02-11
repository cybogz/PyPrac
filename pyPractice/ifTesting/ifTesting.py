fruit = "apple"
cars = ["bmw", "Ford", "toyota", "vw"]

for car in cars:
    if car.lower() == "ford":
        print(car.upper())
        #cars[car] = "nissan"
    else:
        print(car.title())

if fruit != "apple":
    print("This is not an apple")
else:
    print("You can eat the apple")
