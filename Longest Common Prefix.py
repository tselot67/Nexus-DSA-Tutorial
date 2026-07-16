class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for word in strs:
                if i>= len(word) or word[i] != ch:
                    return common_prefix
            common_prefix += ch
        return common_prefix
