class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m = len(nums1)
        n = len(nums2)
        for i in range(m):
            for j in range(n):
                if nums1[i] > nums2[j]:
                    nums1 = nums2[j] + nums1
                else:
                    k = i+1
                    nums1 = nums1[i] + nums2[j] + nums1[k:]
                    break
        return nums1
