def sortedSquaredArray(array):
    # Write your code here.
    result = [x*x for x in array]
    result.sort()
    return result
