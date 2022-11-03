class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        x_str = bin(x)[2:].zfill(32)
        y_str = bin(y)[2:].zfill(32)
        for i in range(32):
            if x_str[i] != y_str[i]:
                ret += 1
        return ret


if __name__ == '__main__':
    slu = Solution()
    print(slu.hammingDistance(1, 4))
