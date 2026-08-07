filename = "programming.txt"

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    

with open(filename) as file_object:
    print(file_object.read())