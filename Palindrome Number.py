class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed_n = 0
        original = x
        while x>0:
            digit = x%10
            reversed_n = reversed_n * 10 + digit
            x = x//10
        return original == reversed_n
