class Users():

    def __init__(self, first_name, last_name, age, user_id):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.user_id = user_id
        
    
    def describe_user(self):
        print("The users name is " + self.first_name + " " + self.last_name + " they are " + str(self.age) + 
              " years old")
        
    def greet_user(self):
        print("Hello " + self.first_name + " welcome")

class Admin(Users):

    def __init__(self, first_name, last_name, age, user_id):

        super().__init__(first_name, last_name, age, user_id)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):

        print("These are the privileges that " + self.first_name + " can have\n")

        for user_privileges in self.privileges:
            print(user_privileges)


