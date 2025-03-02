# by Medina Kubanychbekova
# 03/01/2025
# Problem 4: Return unique elements from a list

def uniqueList(lst):
    unique_elements = []
    for num in lst:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

# Test case
print("Unique elements:", uniqueList([1, 3, 3, 3, 6, 2, 3, 5]))