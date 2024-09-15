def firstDuplicateValue(array):
    # Write your code here.
    occur = [0]*len(array)
    for elem in array:
        if occur[elem - 1] == 0:
            occur[elem - 1] += 1
        else:
            return elem
    return -1