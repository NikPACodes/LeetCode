<h1>6. Зигзаговое преобразование

[![ENG](https://img.shields.io/badge/README-English-red.svg)](README.md)
[![RUS](https://img.shields.io/badge/README-Russian-blue.svg)](README.ru.md)
</h1>

Строка `"PAYPALISHIRING"` пишется зигзагообразным узором в заданном количестве строк следующим образом:  
(возможно, вы захотите отобразить этот узор фиксированным шрифтом для лучшей разборчивости)

```
P   A   H   N
A P L S I I G
Y   I   R
```

А затем прочитайте строку за строкой: `"PAHNAPLSIIGYIR"`

Напишите код, который будет принимать строку и выполнять это преобразование с учетом количества строк:
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
- `s` состоит из английских букв (строчных и прописных), `','` и `'.'`.  
- $1 <=$ `numRows` $<= 1000$


<br>
<h2>Solution:</h2>