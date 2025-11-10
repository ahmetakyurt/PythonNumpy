import numpy as np
import sys

print("Welcome, you can generate numpy arrays here")
print("This will generate n-dimensional random array.")
print("In every dimension, there will be number generated number from 1 to 10")

dimensionNumber = input("Enter the number of dimensions (1/5): ")

try:
    dimensionNumberInt = int(dimensionNumber)
except:
    print("You did not enter valid number")
    print("Exiting from system.")
    sys.exit(1)

while dimensionNumberInt not in range(1,6):
    print("You did not enter a number between 1-5")
    dimensionNumber = input("Enter the number of dimensions (1/5): ")

dimensionSizeList = []
for dimension in range(dimensionNumberInt):
    dimensionSize = input(f"Enter the size of the dimension number {dimension+1}: ")
    try:
        dimensionSizeInt = int(dimensionSize)
    except:
        print("You did not enter valid number")
        print("Exiting from system.")
        sys.exit(1)

    dimensionSizeList.append(dimensionSizeInt)

randomArray = np.random.randint(0, 10, dimensionSizeList)
print(f"Your random generated numpy array: {randomArray}")