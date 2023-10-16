class Solution:
    # O(n * m)
    def numDifferentIntegers(self, word: str) -> int:
        new_str = ""
        list_ = []
        # O(n)
        for i in range(len(word)):
            if word[i].isdigit():
                new_str += str(word[i])
            else:
                if len(new_str) > 0:
                    if len(new_str) >= 2:
                        if new_str[0] == "0":
                            # O(m)
                            while new_str[0] == "0" and len(new_str) > 1:
                                new_str = new_str[1:]
                            list_.append(new_str)
                        else:
                            list_.append(new_str)
                    else:
                        list_.append(new_str)
                new_str = ""
        if len(new_str) > 0:
            if len(new_str) >= 2:
                if new_str[0] == "0":
                    # O(m)
                    while new_str[0] == "0" and len(new_str) > 1:
                        new_str = new_str[1:]
                    list_.append(new_str)
                else:
                    list_.append(new_str)
            else:
                list_.append(new_str)
        return len(set(list_))