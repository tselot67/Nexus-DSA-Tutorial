class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        values = []

        current = head

        while current:
            values.append(current.val)
            current = current.next

        return values == values[::-1]
