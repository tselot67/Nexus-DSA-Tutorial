class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1,1000):
            if i%2 == 0 and i%n == 0:
                break
        return i
        
