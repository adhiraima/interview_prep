def dutch_flag(arr, pivot):
    print(f"Array before {arr}")
    low = equal = 0
    large = len(arr) - 1

    while equal <= large:
        if arr[equal] < pivot:
            temp = arr[low]
            arr[low] = arr[equal]
            arr[equal] = temp
            low += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            temp = arr[equal]
            arr[equal] = arr[large]
            arr[large] = temp
            equal += 1
            large -= 1
    print(f"Array after {arr}")
    return arr


def main():
    arr = [2, 3, 4, 1, 5, 2, 3, 7, 3, 6, 4, 1, 9, 5, 10]
    index = 4
    dutch_flag(arr, arr[index])

if __name__ =="__main__":
    main()
