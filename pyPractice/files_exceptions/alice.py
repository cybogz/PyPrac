def letter_count(filename):
    """Counts all the letters and spaces in a file"""

    try:
        with open(filename) as file_object:
            content = file_object.read()
            #print(content.strip())
    except FileNotFoundError:
        error_message = "File does not exist. add a file"
        print(error_message)
    else:
        letters = content.strip()
        length_of_title = len(letters)
        print(length_of_title)


filename = ["moby_dick.txt", "lord_of_the_rings.txt", "title.txt"]

for files in filename:
    letter_count(files)