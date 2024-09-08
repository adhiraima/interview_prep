def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    i1, i2 = 0, 0
    min, result = float("inf"), []
    while i1 < len(arrayOne) and i2 < len(arrayTwo):
        if abs(arrayOne[i1] - arrayTwo[i2]) < min:
            min = abs(arrayOne[i1] - arrayTwo[i2])
            result = [arrayOne[i1], arrayTwo[i2]]
        if arrayOne[i1] > arrayTwo[i2]:
            i2 += 1
        else:
            i1 += 1
    return result