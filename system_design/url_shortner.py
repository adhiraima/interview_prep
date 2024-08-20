import hashlib

def url_shortner(url: str, user: str=None, num_chars: int=4) -> str:
    print(hashlib.algorithms_guaranteed)
    # for encoder in hashlib.algorithms_available:
    # print(url.encode)
    hash_str = hashlib.sha256(url.encode("utf-8"))
    count = 1
    print(type(hash_str.hexdigest()))
    return 'tiny.com/'+ hash_str.hexdigest()[0:num_chars]


def main():
    print(f"Shorthnad for 'www.google.com' is: {url_shortner('www.google.com', num_chars=6)}")


if __name__ == "__main__":
    main()