import argparse


def message_count(filename):

    info_name = "INFO"
    warning_name = "WARNING"
    error_name = "ERROR"

    info_count = 0
    warning_count = 0
    error_count = 0

    with open(filename) as file_object:
        for line in file_object:
            if info_name in line:
                info_count += 1

            elif warning_name in line:
                warning_count += 1

            elif error_name in line:
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

    parser = argparse.ArgumentParser(description="analyze a log file") # creates the parser object
    parser.add_argument("filename", help="Path to the log file") # what arguments you want
    args = parser.parse_args() # parses the argument/s

    info_count, warning_count, error_count = message_count(args.filename) #args.filename is how we access the data in the argument
    display_error = get_error_messages(args.filename)
    display_information(info_count, warning_count, error_count, display_error)

main()
