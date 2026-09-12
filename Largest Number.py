class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        result = ""

        for num in nums:
            result += num

        if result[0] == "0":
            return "0"

        return result
