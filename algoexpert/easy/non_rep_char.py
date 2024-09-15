def firstNonRepeatingCharacter(string):
    # Write your code here.
    char_map = {}
    for ch in string:
        if ch in char_map.keys():
            char_map[ch] += 1
        else:
            char_map[ch] = 1        
    for i in range(len(string)):
        if char_map[string[i]] == 1:
            return i
    return -1
