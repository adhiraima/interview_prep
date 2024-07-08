def recursive_max(arr, index = 0, max = -1):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[index]
    if index == len(arr) - 1:
        return max
    if arr[index] >= max:
        max = arr[index]
    return recursive_max(arr, index + 1, max)

def recursive_power(base, exp, result = 1):
    if (exp == 0):
        return result
    result *= base
    exp -= 1
    print(f"Result: {result}, exp: {exp}")
    return recursive_power(base, exp, result)

def recursive_brackets(n:int, s:str = '', open:int = 0, close:int = 0, result = set()):
    if len(s) == n*2:
        result.add(s)
    if open < n:
        recursive_brackets(n, s + '(', open + 1, close, result)
    if close < open:
        recursive_brackets(n, s + ')', open, close + 1, result)
    return result

def recursive_reverse(s: str, start: int = 0, end: int = 0):
    if start >= end:
        return s
    chr_arr = list(s)
    temp = chr_arr[start]
    chr_arr[start] = chr_arr[end]
    chr_arr[end] = temp
    print(f"the interim string is: {s}")
    return recursive_reverse(''.join(chr_arr), start + 1, end - 1)

def recursive_plaindrome(s_arr, start, end) -> bool:
    if len(s_arr) == 1:
        return True
    if start < end:
        if s_arr[start] != s_arr[end]:
            return False
        else:
            return recursive_plaindrome(s_arr, start + 1, end - 1)
    else:
        return True

def main():
    arr = [4, 5, 1, 2, 9, 2, 8, 6]
    print(f"Max: {recursive_max(arr)}")
    print(f"Power function for 2^5: {recursive_power(2, 5)}")
    print(f"Power function for 2^10: {recursive_power(2, 10)}")
    # print(f"Result of 2 factor brackets: {recursive_brackets(2)}")
    print(f"Result of 2 factor brackets: {recursive_brackets(3)}")
    print(f"REverse of pots&pans is: {recursive_reverse('pots&pans', 0, len('pots&pans') - 1)}")
    print(f"Palindrome check for 'racecar' is: {recursive_plaindrome('racecar', 0, len('racecar') - 1)}")
    print(f"Palindrome check for 'raceycar' is: {recursive_plaindrome('raceycar', 0, len('raceycar') - 1)}")

if __name__ == "__main__":
    main()
