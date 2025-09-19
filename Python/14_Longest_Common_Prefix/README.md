<h1>14. Longest Common Prefix

[![ENG](https://img.shields.io/badge/README-English-red.svg)](README.md)
[![RUS](https://img.shields.io/badge/README-Russian-blue.svg)](README.ru.md)
</h1>

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

__Example 1:__
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

__Example 2:__
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```


__Constraints:__
- $1 <=$ `strs.length` $<= 200$
- $0 <=$ `strs[i].length` $<= 200$
- `strs[i]` consists of only lowercase English letters if it is non-empty.


<br>
<h2>Solution:</h2>

1) Let's create variables `pref` (_to store the prefix_) and `len_pref` (_the length of the prefix_)
2) Let's start iterating over the input array of strings `strs`.
3) For the first element of the array `strs[0]`:
   - we write the entire string `v_str` (`strs[0]`) into the variable `pref`
   - we write the string length to the `len_pref` variable.
    ```python
    if i == 0:
        pref, len_pref = v_str, len(v_str)
    ```
4) For all subsequent elements we carry out the check:
   1. If the length of the current line __is less__ than the value of the `len_pref` variable, then:
     - update the value of `len_pref`: `len_pref` is equal to the length of the __current__ string
     - update the value of `pref`: `pref` __is shortened__ to the length of `len_pref`
     ```python
     if len_pref > len(v_str):
        len_pref = len(v_str)
        pref = pref[:len_pref]
     ```
   2. In the loop, we check whether the prefix of the current line matches the search prefix.
5) Checking whether the current prefix matches the one being searched for:
   - If the current string's prefix __matches__ the searched prefix, we __move to the next element__ of the string array `strs`
   - If the prefix __does not match__, then:
     1. __decrease the length__ of the sought prefix `len_pref` by $1$
     2. __shorten__ the `pref` prefix by one character
    ```python
    if v_str[:len_pref] == pref:
        break
    else:
        len_pref -= 1
        pref = pref[:len_pref]
    ```
6) Steps 4-5 are repeated until the list of strings `strs` __ends__, or the length of the searched prefix `len_pref` __decreases to $0$__
7) We return the remaining prefix `pref`, which is the solution to our function.

### Code
```python
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
```