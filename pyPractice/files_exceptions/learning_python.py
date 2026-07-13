filename = "learning_python.txt"

#reading a whole file
#with open(filename) as file_object:
    #contents = file_object.read()
    #print(file_object.read())

#reading a file line by line
#with open(filename) as file_object:
    #for line in file_object:
        #print(line.strip())

#reading a file from a list and working with it outside the with block
with open(filename) as file_object:
    content = file_object.readlines()

storing_string = ""
for line in content:
    storing_string += line

print(storing_string.strip())