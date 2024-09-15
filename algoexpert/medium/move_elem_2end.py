def moveElementToEnd(array, toMove):
    # Write your code here.
    end = len(array) - 1
    count = 0
    for elem in array:
        if elem == toMove:
            count += 1
    rep_count = 0
    index = 0
    while index < len(array):
        if index >= end:
            break
        if array[index] == toMove:
            temp = array[index]
            array[index] = array[end]
            array[end] = temp
            end -= 1
        else:
            index += 1
                
    return array