class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()

        left = 0
        right = len(skill) - 1

        team_skill = skill[left] + skill[right]
        chemistry = 0

        while left < right:
            if skill[left] + skill[right] != team_skill:
                return -1

            chemistry += skill[left] * skill[right]

            left += 1
            right -= 1

        return chemistry
