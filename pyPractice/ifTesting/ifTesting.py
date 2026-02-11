cars = ["bmw", "ford", "toyota", "vw"]

for car in cars:
    if car == "ford":
        print(car.upper())
        cars[car] = "nissan"
    else:
        print(car.title())

print(cars)