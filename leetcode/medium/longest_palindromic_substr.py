def longestPalindrome(self, s):
    if len(s) <= 1:
        return s

    def expand_string(left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left + 1:right]

    max = 0
    result = ""
    for i in range(len(s)):
        odd = expand_string(i, i)
        even = expand_string(i, i + 1)

        if len(even) > max:
            max = len(even)
            result = even

        if len(odd) > max:
            max = len(odd)
            result = odd
    return result 