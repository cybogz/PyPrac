class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        
        print("The name of the resturant is " + self.restaurant_name)
        print("They are " + self.cuisine_type + " food")

    def open_restaurant(self):

        print(self.restaurant_name + " is now open")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(self, restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "strawberry", "oreo"]