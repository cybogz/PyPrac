filename = "learning_python.txt"

with open(filename) as file_object:
    for line in file_object:
        line = line.replace('python', 'c')
        print(line.strip())

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())