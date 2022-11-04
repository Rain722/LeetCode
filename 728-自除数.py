from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num:int) -> bool:
            x = num
            while x:
                x, d = divmod(x, 10)
                if d == 0 or num %d:
                    return False
            return True
        return [i for i in range(left, right+1) if isSelfDividing(i)]

if __name__ == '__main__':
    nums = [4, 14, 2]
    slu = Solution()
    print(slu.selfDividingNumbers(47, 85))