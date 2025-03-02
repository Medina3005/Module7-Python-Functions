# by Medina Kubanychbekova
# 03/01/2025
# Problem 3: Multiply all numbers in a list

def multiplyList(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Test case
print("Product of list:", multiplyList([5, 2, 7, -1]))