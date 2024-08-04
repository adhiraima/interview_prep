import math

def max_crossing_subarray(arr, low, mid, high):
    left_max = -math.inf
    sum = 0
    max_left = -1
    for i in range(mid, low):
        sum += arr[i]
        if sum > left_max:
            left_max = sum
            max_left = i
    sum = 0
    right_max = -math.inf
    max_right = -1
    for i in range(mid, high):
        sum += arr[i]
        if sum > right_max:
            right_max = sum
            max_right = i
    print(f"Left Index: {max_left}, Right Index: {max_right}, Max Sum: {right_max + left_max}")
    return (max_left, max_right, right_max + left_max)

def max_subarray(arr, left, right):
    if left == right:
        return (arr, left, right)
    else:
        mid = math.floor((left+right)/2)
        lleft, lright, lsum = max_subarray(arr, left, mid)
        rleft, rright, rsum = max_subarray(arr, mid + 1, left)
        cleft, cright, csum = max_crossing_subarray(arr, left, mid, right)
    if lsum >= rsum >= csum:
        return (lleft, lright, lsum)
    elif rsum >= lsum >= csum:
        return (rleft, rright, rsum)
    else:
        return (cleft, cright, csum)

def main():
    arr = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    print(max_subarray(arr, 0, len(arr)))

if __name__ =="__main__":
    main()
