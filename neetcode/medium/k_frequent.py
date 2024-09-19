def k_frequent(arr, k):
    count = {}
    for item in arr:
        if item in count.keys():
            count[item] += 1
        else:
            count[item] = 1
    
    sort_count = sorted(count.items(), key=lambda count:count[1])
    return [x for x, v in sort_count[-k:]]

def main():
    k = 2
    arr = [2, 2, 2, 3, 3, 3, 4, 1]
    print(k_frequent(arr, k))

if __name__ == "__main__":
    main()