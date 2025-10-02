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
    

__Пример 1:__
```
Входные данные: s = "PAYPALISHIRING", numRows = 3
Выходные данные: "PAHNAPLSIIGYIR"
```

__Пример 2:__
```
Входные данные: s = "PAYPALISHIRING", numRows = 4
Выходные данные: "PINALSIGYAHRPI"
Пояснение:
P     I    N
A   L S  I G
Y A   H R
P     I
```

__Пример 3:__
```
Входные данные: s = "A", numRows = 1
Выходные данные: "A"
```

__Ограничения:__

- $1 <=$ `s.length` $<= 1000$  
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.  
- $1 <=$ `numRows` $<= 1000$


<br>
<h2>Solution:</h2>