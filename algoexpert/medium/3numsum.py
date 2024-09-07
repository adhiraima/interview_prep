def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result = []

    for curr in range(len(array)):
        left = curr + 1
        right = len(array) - 1
        while left < right:
            sum = array[curr] + array[left] + array[right]
            if sum > targetSum:
                right -= 1
            elif sum < targetSum:
                left += 1
            else:
                result.append([array[curr], array[left], array[right]])
                left += 1

    return result