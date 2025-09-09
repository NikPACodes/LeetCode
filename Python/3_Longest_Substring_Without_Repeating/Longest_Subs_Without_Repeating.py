class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        check_dict = {}
        left = 0
        for right, ch in enumerate(s):
            if ch in check_dict and check_dict[ch] >= left:
                left = check_dict[ch] + 1
            else:
                max_len = max(max_len, right - left + 1)
            check_dict[ch] = right
        return max_len

#
#
# test = Solution()
# print(test.lengthOfLongestSubstring("abcabcbb"))
# print(test.lengthOfLongestSubstring("bbbbb"))
# print(test.lengthOfLongestSubstring("pwwkew"))
# print(test.lengthOfLongestSubstring(" "))
# print(test.lengthOfLongestSubstring("dvdf"))
# print(test.lengthOfLongestSubstring("tmmzuxt"))
