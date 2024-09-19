def arr_product(arr):
    prod = 1
    for item in arr:
        prod *= item
    print(prod)

    return [int(prod/i) for i in arr]
def main():
    arr = [1, 2, 3, 4]
    print(arr_product(arr))

if __name__ == "__main__":
    main()