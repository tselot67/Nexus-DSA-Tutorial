class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        holder = 0
        seeker = 0
        for i in range(len(nums)):
            if nums[seeker] == 0:
                seeker += 1
            else:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
                seeker += 1
        return nums
