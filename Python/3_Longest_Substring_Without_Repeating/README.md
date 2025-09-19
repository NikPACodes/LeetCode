<h1>3. Longest Substring Without Repeating Characters

[![ENG](https://img.shields.io/badge/README-English-red.svg)](README.md)
[![RUS](https://img.shields.io/badge/README-Russian-blue.svg)](README.ru.md)
</h1>

Given a string `s`, find the length of the __longest substring__ without duplicate characters.

__Example 1:__
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

__Example 2:__
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

__Example 3:__
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

__Constraints:__
- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces.


<br>
<h2>Solution:</h2>

To solve this problem, we can use the two-pointer method.
The first index points to the beginning of the substring being searched for, and the second to the end.

1) Let's create the necessary variables:
   - `max_len` - the length of the longest substring without repeating characters
   - `check_dict` - a dictionary for storing characters and their indices in a string
   - `left` - substring start index
2) We begin to iterate over the indexed (_using the `enumerate` function_) string `s`.
3) Checking:
   - If the character of the string `s` (`ch`) __is in the dictionary__ `check_dict` and the index of the character __is greater__ than or __equal__ to the index of the beginning of the string `left`,
   then the new value of the index of the beginning of the string `left` becomes __equal__ to the index of the character `check_dict[ch]` plus $1$
   - If the dictionary `check_dict` __does not contain__ the character `s` (`ch`) of the string and the length of the current substring __is greater__ than the maximum length `max_len`,
   then we __update__ the maximum substring length indicator.
    ```python
    if ch in check_dict and check_dict[ch] >= left:
        left = check_dict[ch] + 1
    else:
        max_len = max(max_len, right - left + 1)
    ```
4) Adding/updating an entry in our dictionary of unique symbols `check_dict`: `check_dict[ch] = right`
5) Repeat steps 3-4 until the line is complete `s`
6) Return the length of the longest substring `max_len`

### Code
```python
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
```