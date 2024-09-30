class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # not in place
        # print(nums[k:-k])
        # result = []
        # for i in nums[-k:]:
        #     result.append(i)
        # for i in nums[:k+1]:
        #     result.append(i)
        # print(result)
        # nums = result

        #time limit exceeded    
        # for i in range(k):
        #     last = nums[len(nums) - 1]
        #     index = len(nums) - 1
        #     while index > 0:S
        #         nums[index] = nums[index - 1]
        #         index -= 1
        #     nums[0] = last
        # print(nums)

        k = k % len(nums)
        rotate = len(nums) - k
        slice = nums[0:rotate]
        nums[0:rotate] = []
        nums.extend(slice)