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