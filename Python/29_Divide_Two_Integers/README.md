<h1>29. Divide Two Integers

[![ENG](https://img.shields.io/badge/README-English-red.svg)](README.md)
[![RUS](https://img.shields.io/badge/README-Russian-blue.svg)](README.ru.md)
</h1>

Given two integers `dividend` and `divisor`, divide two integers __without__ using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.  
Return _the __quotient__ after dividing `dividend` by `divisor`_.  
__Note__: Assume we are dealing with an environment that could only store integers within the __32-bit__ signed integer range: $[−2^{31}, 2^{31} − 1]$. 
For this problem, if the quotient is __strictly greater than__ $2^{31} - 1$, then return $2^{31} - 1$, and if the quotient is __strictly less than__ $-2^{31}$, then return $-2^{31}$.


__Example 1:__
```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
```

__Example 2:__
```
Input: dividend = 7, divisor = -3
Output: -2
Explanation: There is no common prefix among the input strings.
```

__Constraints:__
- $-2^{31} <=$ `dividend, divisor` $<= 2^{31} - 1$
- `divisor` $!= 0$


<br>
<h2>Solution:</h2>
