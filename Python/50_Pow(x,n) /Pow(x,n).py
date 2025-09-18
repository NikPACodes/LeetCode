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

test = Solution()
print(test.myPow(2.00000, 10))
print(test.myPow(2.10000, 3))
print(test.myPow(2.00000, -2))
print(test.myPow(0.44528, 0))
print(test.myPow(8.95371, -1))


print(test.myPow2(2.00000, 10))
print(test.myPow2(2.10000, 3))
print(test.myPow2(2.00000, -2))
print(test.myPow2(0.44528, 0))
print(test.myPow2(8.95371, -1))

