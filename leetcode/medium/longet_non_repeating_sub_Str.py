def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    sub_str = []
    max = 0

    for i in range(len(s)):
        if s[i] in sub_str:
            # print("Match found for: ", s[i])
            # print("Match found at: ", sub_str.index(s[i]))
            if sub_str.index(s[i]) == 0:
                sub_str.pop(0)
                # print("Sub str after front pop: ", sub_str)
            else:
                for j in range(0, sub_str.index(s[i])):
                    # print("Removing: ", j)
                    sub_str.pop(0)
                # print("Sub str after pops: ", sub_str)
        sub_str.append(s[i])
        # print(sub_str)        
        if len(sub_str) > max:
            max = len(sub_str)
    return max