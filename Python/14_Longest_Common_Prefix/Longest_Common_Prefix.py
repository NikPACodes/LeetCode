class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref = ''
        len_pref = 0
        for i, v_str in enumerate(strs):
            if i == 0:
                pref, len_pref = v_str, len(v_str)
            else:
                if len_pref > len(v_str):
                    len_pref = len(v_str)
                    pref = pref[:len_pref]
                while True:
                    if v_str[:len_pref] == pref:
                        break
                    else:
                        len_pref -= 1
                        pref = pref[:len_pref]
                if len_pref == 0:
                    break
        return pref

#
# test = Solution()
# print(test.prefix(["flower","flow","flight"]))
# print(test.prefix(["dog","racecar","car"]))
# print(test.prefix(["dog","dogs","dog"]))
#
