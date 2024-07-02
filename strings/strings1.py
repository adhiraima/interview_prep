def reverse_sentence(s: str) -> str:
    if s.find(" ") < 0:
        return s

    return ""

def unique_chars(s: str) -> bool:
    char_dict = []
    for ch in s:
        if ch in char_dict:
            return False
        else:
            char_dict.append(ch)
    return True


def remove_dupes_bf(s: str) -> str:
    for i in range(0, len(s) - 1):
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                s =  s[:j] + s[j + 1:]
            else:
                j += 1
    return s

def anagrams(s: str, x: str) -> bool:
    inter_x = [0] * 256
    inter_s = [0] * 256
    if len(s) != len(x):
        return False
    else:
        for i in range(0, len(x)):
            inter_x[ord(x[i])] += 1
            inter_s[ord(s[i])] += 1
    for i in range(0, 256):
        if inter_x[i] == 0 and inter_s[i] == 0:
            continue
        print(f"Comparing {chr(i)}: {inter_x[i]} with {inter_s[i]}")
        if inter_x[i] != inter_s[i]:
            return False
    # print(inter)
    return True

def encode_spaces(s: str) ->  str:
    return ''.join([x if x != " " else "%20" for x in s])

def main():
    # print(f"Unique chars in abcdef: {unique_chars('abcdef')}")
    # print(f"Unique chars in abcaef: {unique_chars('abcaef')}")
    # print(f"Unique chars in aabcdeef: {unique_chars('aabcdeef')}")
    # print(f"Response: {remove_dupes_bf("abcdaabcd")}")
    # print(f"Response: {remove_dupes_bf("aaaa")}")
    # print(f"Response: {remove_dupes_bf("ab")}")
    # print(f"Response: {remove_dupes_bf("a")}")
    # print(f"Anagrams: abcd & bcda {anagrams('abcd', 'bcda')}")
    # print(f"Anagrams: abbcddddcca & ccbcdaabddd {anagrams('abbcddddcca', 'ccbcdaabddd')}")
    # print(f"Anagrams: abc & bcda {anagrams('abc', 'bcda')}")
    #print(f"Anagrams: abcddd & bbbcda {anagrams('abcddd', 'bbbcda')}")
    print(f"""String 'This is a beautiful day' after encoding: {encode_spaces('This is a beautiful day')}""")

if __name__ == "__main__":
    main()
