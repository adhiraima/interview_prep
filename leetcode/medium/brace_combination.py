def braces(n, open, close, result, seed):
    if len(seed) == n*2:
        result.append("".join(seed))
        return
    if open < n:
        seed.append("(")
        braces(n, open + 1, close, result, seed)
        seed.pop()
    if close < open:
        seed.append(")")
        braces(n, open, close + 1, result, seed)
        seed.pop()

def main():
    n, open, close = 4, 0, 0
    result, seed = [], []
    braces(n, open, close, result, seed)
    print(result)

if __name__ == "__main__":
    main()