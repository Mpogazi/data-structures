
# For this method the array inputs must be from [0 to n]
# where n is the size of the array
def find_repeating_numbers(array):
    size = len(array)
    duplicates = list()
    for i in range (0, size):
        if array[abs(array[i])] >= 0:
            array[abs(array[i])] = - array[abs(array[i])]
        else:
            duplicates.append(array[abs(array[i])])
    return duplicates

# For general array elements
def find_repeated_elements(array):
    new_container, duplicates = set(), list()
    for x in array:
        if x in new_container:
            duplicates.append(x)
        else:
            new_container.add(x)
    return duplicates

# Median Finding algorithm
def find_median(array):
    pass
