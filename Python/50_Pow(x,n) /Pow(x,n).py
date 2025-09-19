class Solution:
    # Через рекурсию
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

    # Через цикл
    def myPow2(self, x: float, n: int) -> float:
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