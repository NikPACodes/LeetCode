class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        negative_num = False if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else True
        dividend, divisor = map(abs, (dividend, divisor))

        if dividend == divisor:
            return -1 if negative_num else 1
        elif dividend < divisor:
            return 0
        elif divisor == 1:
            if dividend >= 2147483648:
                return -2147483648 if negative_num else 2147483647
            return -dividend if negative_num else dividend

        hash_tabl = []
        mult, res = 1, 0
        mult_div = divisor
        right_ind = 0
        while True:

            if dividend == 0 or dividend < divisor:
                break

            if dividend > mult_div:
                dividend -= mult_div
                res += mult
                hash_tabl.append((mult_div, mult))
                mult += mult
                mult_div += mult_div
                right_ind += 1
            else:
                for val in reversed(hash_tabl[:right_ind]):
                    if dividend >= val[0]:
                        mult = val[1]
                        mult_div = val[0]
                        right_ind = hash_tabl.index(val) + 1
                        dividend -= mult_div
                        res += mult
                        break

        if negative_num:
            res = -res if res <= 2147483648 else -2147483648
        else:
            res = res if res < 2147483648 else 2147483647
        return res