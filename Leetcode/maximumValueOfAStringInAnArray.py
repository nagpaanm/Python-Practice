class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_ = 0

        # O(n)
        for string in strs:
            if string.isnumeric():
                max_ = max(max_, int(string))
            else:
                max_ = max(max_, len(string))
        return max_