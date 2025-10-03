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