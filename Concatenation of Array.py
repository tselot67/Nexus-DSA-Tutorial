class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        x = 2*n
        for i in range(x):
            if i < n:
                ans.append(nums[i])
            else:
                ans.append(nums[i-n])
        return ans
