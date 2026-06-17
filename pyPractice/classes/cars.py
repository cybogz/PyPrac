class Cars():

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """prints the long name of the car being created"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """prints a statement showing the car's milage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """method to update the mileage of the car"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back the odometer")
    
    def increment_odometer(self, miles):
        """increments the mileage by a user input"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Please do not enter a negative odometer number")

class Battery():
    """creates an electrical car battery class"""
    def __init__(self, batter_size=70):
        self.battery_size = batter_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " KWh battery") 

class ElectricCar(Cars):
    """represents the aspects of a electric car specifically"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. Then initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery = Battery()

inheri_electric_class = ElectricCar('toyota', 'prius', 2026)
print(inheri_electric_class.get_descriptive_name())

inheri_electric_class.battery.describe_battery()



#my_new_car = Cars('audi', 'a4', 2016)
#print(my_new_car.get_descriptive_name())

#my_new_car.update_odometer(25000)
#my_new_car.read_odometer()
#my_new_car.increment_odometer(-100)
#my_new_car.read_odometer()