class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0
        holder = 0
        seeker = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                seeker += 1
            else:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
                seeker += 1
        return nums
