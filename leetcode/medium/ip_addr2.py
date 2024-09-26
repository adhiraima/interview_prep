def get_ip_addresses(ip, start, dot, ip_addr, result):
     pass

def main():
    ip_str = ["101023", "0000", "255255255255", "10101010", "25525511135"]
    
    for ip in ip_str:
        result, ip_addr = [], []
        start = 0
        dot = start + 4
        get_ip_addresses(ip, start, dot, ip_addr, result)
        print(result)

if __name__ == "__main__":
    main()