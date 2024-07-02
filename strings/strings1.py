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


def main():
    print(f"Unique chars in abcdef: {unique_chars('abcdef')}")
    print(f"Unique chars in abcaef: {unique_chars('abcaef')}")
    print(f"Unique chars in aabcdeef: {unique_chars('aabcdeef')}")

if __name__ == "__main__":
    main()
