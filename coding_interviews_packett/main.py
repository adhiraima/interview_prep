def main():
    arr = [1, 2, 3, 4, 5]
    sum = 0
    for i in arr:
        sum += i

    total = int(len(arr)*(len(arr) - 1)/2)

    print(sum - total)

    print(f"Duplicate : {sum - total}")

if __name__ == "__main__":
    main()
