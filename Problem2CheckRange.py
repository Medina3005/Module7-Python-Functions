
# by Medina Kubanychbekova
# 03/01/2025
# Problem 2: Check if a number is in range

def checkRange(n):
    if n in range(1, 10):
        print(f"{n} is in the range.")
    else:
        print(f"{n} is not in the range.")

# Test case
checkRange(5)
checkRange(15)