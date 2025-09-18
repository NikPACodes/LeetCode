<h1>50. Pow(x, n)

[![ENG](https://img.shields.io/badge/README-English-red.svg)](README.md)
[![RUS](https://img.shields.io/badge/README-Russian-blue.svg)](README.ru.md)
</h1>

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

__Example 1:__
```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

__Example 2:__
```
Input: x = 2.10000, n = 3
Output: 9.26100
```

__Example 3:__
```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: (2)^-2 = (1/2)^2 = 1/4 = 0.25
```

__Constraints:__
- `-100.0 < x < 100.0`
- `(-2)^31 <= n <= (2^31)-1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`
- `-10^4 <= x^n <= 10^4`


<br>
<h2>Solution:</h2>

There are two possible approaches to solving this problem:
- _using a loop_
- _using recursion_

To solve this, we will look at all cases of raising a number to a power. ($x^n$):
- `n < 0` => $x^{-n} = (1/x)^n$
- `n = 0` => $x^0 = 1$
- `n > 0` =>:
  - If `n` is even, then $x^n = (x^2)^{n/2}$  
  Example: $2^8 = (2^2)^4 = (4^2)^2 = 16^2 = 256$
  - If `n` is odd, then $x^n = x^{n-1}*x$  
  Example: $2^7 = 2^6 * 2 = (2^2)^3 * 2 = 4^2 * 4 * 2 = 16 * 8 = 128$
- According to the problem statement, `n` is an integer, so we __won\`t consider__ this option, where `n` is a fraction and we need to find the root of the number.


### 1. Solution using a loop

Solving the problem using a loop:
1) Let's create a variable `dop` (_our additional multiplier_) with a default value of $1$
2) Let's check whether the power `n` is a __negative number or $0$__
   - When `n` is $0$, our function __returns__ $1$: `return 1`
   - If `n` is __negative__, __replace__ the value of `x` with `1/x` and __get rid of the negative sign__ in the power `n`
    ```python
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n *= -1
    ``` 
3) We start a loop to calculate the value of the function $x^n$ and the additional multiplier `dop`.
4) Check if `n` is an __odd__ number:
   - If it is, then we calculate the additional multiplier as `dop` multiplied by `x`
    ```python
    if n % 2 != 0:
        dop *= x
    ```
5) We calculate the values of the variable `x` and the exponent `n`:
   - the value of `x` is __multiplied__ by itself
   - the value of `n` becomes equal to the __integer part__ of `n` divided by $2$
6) Steps 4-5 are repeated until the exponent `n` __becomes equal to__ $1$
7) When `n` __equals__ $1$, we exit the loop and __return__ the resulting value of `x` multiplied by `dop`.

### Code
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        dop = 1
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n *= -1
        while True:
            if n == 1:
                break

            if n % 2 != 0:
                dop *= x
            x *= x
            n //= 2
        return x * dop
```
<br>


### 2. Solutions using recursion

Solving a problem using recursion.
We have a function that receives as input the value of a number `x` and a power of `n`.
1) Let's check if the degree is a __negative number or $0$__
   - If `n` __is__ $0$, then the function __returns__ $1$: `return 1`
   - If `n` is __less__ than $0$, then __replace__ the value of `x` with `1/x` and __get rid of the negative sign__ to the power of `n`
    ```python
    if n == 0:
        return 1
    elif n < 0:
        x = 1/x
        n *= -1
    ```
2) If the value `n` is __greater__ than $0$, we perform a second check:
   - If `n` is an __even__ number (i.e. `n % 2 == 0`),
   then the function returns __itself__ with the following parameters:
     1. parameter `x`: the __square__ of the number `x` is passed
     2. parameter `n`: __the integer part__ of the division of `n` by $2$ is passed
   ```python
   return self.myPow(x * x, n // 2)
   ```
   - If `n` is an __odd__ number (i.e. `n % 2 != 0`), 
   then the function returns __itself__ (with the same parameters as with an even value) __multiplied__ by `x`:
   ```python
   return self.myPow(x * x, n // 2) * x
   ```
3) The recursion is repeated until `n` becomes __equal__ to $0$

### Code
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
             x = 1/x
             n *= -1
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2) * x
```