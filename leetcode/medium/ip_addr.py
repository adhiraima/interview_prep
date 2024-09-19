class Solution(object):
    def restoreIpAddresses(self, s):
        print("Coming here!!!!!")
        result, ip_Addr = [], []
        self.create_ips(s, -1, 3, ip_Addr, result)
        return result


    def valid(self, octet):
        print("Validating: ", octet)
        if len(octet) > 3:
            return False
        if octet[0] == "0" and len(octet) > 1:
            return False
        int_val = int(str(octet))
        if int_val > 0 and int_val <= 255:
            return True
        if int_val == 0 and len(octet) == 1:
            return True
        return False


    def finalize_ip(self, s, curr_dot, ip_addr, result):
        octet = s[curr_dot + 1: len(s)]
        if self.valid(octet):
            ip_addr.append(octet)
            print("Finalising result: ", ip_addr)
            result.append(".".join(ip_addr))
            ip_addr.pop()

    def create_ips(self, s, prev_dot, dots, ip_addr, result):
        print("min:", str(prev_dot + 1), " max:", str(min(len(s) - 1, prev_dot + 4)))
        for curr_dot in range(prev_dot + 1, min(len(s) - 1, prev_dot + 4)):
            print("octet start: ", str(prev_dot + 1), " end: ", str(curr_dot + 1))
            octet = s[prev_dot + 1:curr_dot + 1]
            print("Octet: ", octet)
            if self.valid(octet):
                ip_addr.append(octet)

                if dots - 1 == 0: #last octet
                    self.finalize_ip(s, curr_dot, ip_addr, result)
                else:
                    self.create_ips(s, curr_dot, dots - 1, ip_addr, result)
                ip_addr.pop()

def main():
    ip_str = ["101023", "0000", "255255255255", "10101010", "25525511135"]
    for ip in ip_str:
        print(Solution().restoreIpAddresses(ip))

if __name__ == "__main__":
    main()