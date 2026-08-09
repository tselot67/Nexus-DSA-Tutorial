class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        holder = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] == 0:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
            seeker += 1
        x = nums.count(0)
        holder = x
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] == 1:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
            seeker += 1
        return nums
