for oddNumbers in range(1,20,2):
    print(oddNumbers)

print("\n")

for multiplesOfThrees in range(3,30,3):
    print(multiplesOfThrees)

print("\n")

for cubeValues in range(1,10):
    print(cubeValues**3)

print("\n")

cubes = [value**3 for value in range(1,10)]
print(cubes)