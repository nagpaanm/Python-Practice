class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            tmp = str2
            str2 = str1
            str1 = tmp
        string = ""
        tmp = ""

        # O(n)
        for j in range(len(str2)):
            tmp += str2[j]
            if len(str2) % len(tmp) == 0 and len(str1) % len(tmp) == 0:
                div1 = len(str2) // len(tmp)
                div2 = len(str1) // len(tmp)
                if tmp * div1 == str2 and tmp * div2 == str1:
                    string = tmp
        return string