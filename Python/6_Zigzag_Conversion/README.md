<h1>6. Zigzag Conversion

[![ENG](https://img.shields.io/badge/README-English-red.svg)](README.md)
[![RUS](https://img.shields.io/badge/README-Russian-blue.svg)](README.ru.md)
</h1>

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string s, int numRows);
```
    

__Example 1:__
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

__Example 2:__
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

__Example 3:__
```
Input: s = "A", numRows = 1
Output: "A"
```

__Constraints:__

- $1 <=$ `s.length` $<= 1000$  
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.  
- $1 <=$ `numRows` $<= 1000$


<br>
<h2>Solution:</h2>

To solve this problem, we simply iterate over the string s once and split it into numRows rows. 
We'll use a flag to form these rows in a zig-zag pattern.  
This solution will have linear complexity of _($$O(n)$$)_.

1) Let's check that the input string `s` has a length __greater__ than the required number of rows `numRows`.  
If this __is not the case__, then we simply __return the string__ `s`, which will be the solution.
    ```python
    lstr = len(s)
    if numRows == 1 or numRows >= lstr:
        return s
    ```
2) Next, we'll create __a list of `numRows` lists__ (`zigzag`), as well as __a pointer__ to the list into which we'll write the value (`zz_ind`)  
and __the flag__ needed to calculate the index (`down`).
3) We loop through the input string `s` and perform the following steps:
   - __Write__ the value to the list at index `zz_ind`
   - Next, we check our flag:
     - If the index __is__ $0$, we __change__ it to `True`.
     - If the index __is__ `numRows - 1`, we __set__ it to `False`
   - Calculate __the index__ for writing the __next__ element:
     - If the flag __is__ `True`, we write the element to the __next__ list in order, i.e. `zz_ind += 1`
     - Otherwise, if the flag __is__ `False`, we go in the opposite direction and write to the __previous__ list, i.e. `zz_ind -= 1`
    ```python
    for i in range(lstr):
        zigzag[zz_ind].append(s[i])
        if zz_ind == 0:
            down = True
        elif zz_ind == numRows - 1:
            down = False
        zz_ind += 1 if down is True else -1
    ```
4) After iterating through the entire string `s` in step 3, __concatenate__ all the resulting lists from `zigzag` into one.
5) __Return__ the resulting list as a __concatenated string__, which will be the solution.

### Code
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lstr = len(s)
        if numRows == 1 or numRows >= lstr:
            return s

        result = list()
        zigzag = [[] for _ in range(numRows)]
        zz_ind, down = 0, True
        for i in range(lstr):
            zigzag[zz_ind].append(s[i])
            if zz_ind == 0:
                down = True
            elif zz_ind == numRows - 1:
                down = False
            zz_ind += 1 if down is True else -1

        for line in zigzag:
            result += line
        return(''.join(result))
```