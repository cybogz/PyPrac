filename = "app.log"

info_count = 0
warning_count = 0
error_count = 0

info_name = "INFO"
warning_name = "WARNING"
error_name = "ERROR"

error_messages = []

with open(filename) as file_object:
    for line in file_object:
        if info_name in line:
            info_count += 1

        elif warning_name in line:
            warning_count += 1

        elif error_name in line:
            error_count += 1
            error_messages.append(line.strip())


print("\nError log count")
print("---------------")

print(f"Number of INFO messages: {info_count}")
print(f"Number of WARNING messages: {warning_count}")
print(f"Number of ERROR messages: {error_count}")

print("\nError messages")
print("---------------")

for error in error_messages:
    print(error)