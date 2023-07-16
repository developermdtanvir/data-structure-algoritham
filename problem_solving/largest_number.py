# TODO: find largest number and array

def find_largest_number(array):
    largest = float('-inf')

    for number in array:
        if number > largest:
            largest = number
    return largest

largest = find_largest_number([1,10,20,30,40,50])

print(largest)




