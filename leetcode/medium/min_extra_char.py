class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        result = []
        # print(result)
        index = 0
        for word in dictionary:
            start = 0
            if s.find(word) == -1:
                continue
            row = [-1] * len(s)
            while s.find(word, start) >= 0:
                print("Word: ", word, " found at: ", str(s.find(word, start)))
                start = s.find(word, start)
                for i in range(start, start + len(word)):        
                    row[i] = 1
                start = s.find(word, start) + len(word)
            index += 1
            result.append(row)
        response = 0
        for row in result:
            print(row)
        for i in range(len(s)):
            count = 0
            for j in range(len(result)):
                if result[j][i] == -1:
                    count += 1
                else:
                    break
            if count == len(result):
                response += 1
        return response