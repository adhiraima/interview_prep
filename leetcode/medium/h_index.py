class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        count = 0
        for i in reversed(range(len(citations))):
            if count < citations[i]:
                count += 1
            else:
                break
        return count