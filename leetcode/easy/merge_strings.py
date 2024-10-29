class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if word2 is None:
            return word1
        if word1 is None:
            return word2

        count = max(len(word1), len(word2))
        result = ""
        for i in range(count):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return result