class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for ch in words[0]:
            if all(ch in words[i] for i in range(1, len(words))):
                    result.append(ch)
                    for i in range(len(words)):
                        words[i] = words[i].replace(ch, "", 1)      
        return result
