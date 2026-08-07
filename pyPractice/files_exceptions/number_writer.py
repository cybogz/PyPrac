import json

filename = 'numbers.json'

#numbers_list = [1,2,3,4,5,6,7,10]

with open(filename) as file_obj:
    number = json.load(file_obj)

print(number)