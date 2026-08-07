filename = 'app.log'

with open(filename) as file_object:
    for line in file_object:
        if 'ERROR' in line:
            print(line.strip())