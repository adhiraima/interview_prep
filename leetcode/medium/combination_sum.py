class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        curr_set = []
        def backtracking(remainder,candidates,startIndex):
            if remainder == 0:
                result.append(curr_set[:])
                return
            for i in range(startIndex,len(candidates)):
                if remainder - candidates[i] < 0:
                    break
                remainder -= candidates[i]
                curr_set.append(candidates[i])
                backtracking(remainder,candidates,i)
                remainder += candidates[i]
                curr_set.pop()
        candidates.sort()
        backtracking(target,candidates,0)
        
        return result
