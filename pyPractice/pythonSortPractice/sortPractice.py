placesTOVisits = ["Osaka", "Morroco", "Manchester", "New York", "London", "Thailand"]

print("This is the list in its original order")
print(placesTOVisits)

print("\nThis is the sorted list")
print(sorted(placesTOVisits))

print("\nThis is the sorted list in reverse order")
print(sorted(placesTOVisits, reverse=True))

print("\nPrinting the list again to show that it is back in its orginal order after using the sorted function")
print(placesTOVisits)

print("\nPrinting using the reverse method to reverse the order")
placesTOVisits.reverse()
print(placesTOVisits)

print("\nPrinting using the reverse method to put the list back into the original order")
placesTOVisits.reverse()
print(placesTOVisits)

print("\nThis is the length of the list")
print(len(placesTOVisits))

print(placesTOVisits[4])