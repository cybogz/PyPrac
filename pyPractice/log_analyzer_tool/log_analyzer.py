import argparse

def user_cli_argument():

    parser = argparse.ArgumentParser(description="analyze a log file") # creates the parser object
    parser.add_argument("filename", nargs="?", default="app.log", help="Path to the log file") # what arguments you want
    args = parser.parse_args() # parses the argument/s

    return args.filename

def message_count(filename):
    """gets the count for info, warning, and error in the log file"""

    info_count = 0
    warning_count = 0
    error_count = 0

    with open(filename) as file_object:
        for line in file_object:
            if "INFO" in line:
                info_count += 1

            elif "WARNING" in line:
                warning_count += 1

            elif "ERROR" in line:
                error_count += 1

    return info_count, warning_count, error_count

def get_error_messages(filename):

    error_messages = []

    with open(filename) as file_object:
        for error in file_object:
            if "ERROR" in error:
                error_messages.append(error.strip())

    return error_messages

def display_information(info_count, warning_count, error_count, display_error):

    print("\n*Error Log Count*")
    print("---------------")

    print(f"Number of INFO messages: {info_count}")
    print(f"Number of WARNING messages: {warning_count}")
    print(f"Number of ERROR messages: {error_count}")

    print("\n*Error Messages*")
    print("---------------")

    for error in display_error:
        print(error)

def main():

    filename = user_cli_argument()

    print("Analyzing: " + filename) 

    info_count, warning_count, error_count = message_count(filename) #args.filename is how we access the data in the argument
    display_error = get_error_messages(filename)
    display_information(info_count, warning_count, error_count, display_error)

main()
