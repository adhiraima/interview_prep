def check_anagrams(array):
    word_map = {}
    for word in array:
        conv_key = get_sorted_key(word)
        if conv_key not in word_map:
            word_map[conv_key] = []
        word_map[conv_key].append(word)
    # result = []
    # for key in word_map.keys():
    #     result.append(word_map[key])
    return [val for val in word_map.values()]

def get_sorted_key(element):
    key_map = {}
    for ch in element:
        if ch in key_map:
            key_map[ch] += 1
        else:
            key_map[ch] = 1
    key_list = list(key_map.keys())
    key_list.sort()

    result = ""
    for key in key_list:
        result += key + str(key_map[key])
    # print(f"Word: {element} and Key: {result}")
    return result

def main():
    array = ["eat", "ate" ,"tea", "nat", "tan", "bat"]

    # array = ["eaatt", "aatte" ,"tteaa", "nat", "tan", "bat"]
    print(check_anagrams(array))

if __name__ == "__main__":
    main()