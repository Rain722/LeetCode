from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res, nlen = 0, len(nums)
        for i in range(32):
            cnt = 0
            for j in range(nlen):
                cnt += (nums[j] >> i) & 1
            res += cnt*(nlen-cnt)
        return res

if __name__ == '__main__':
    nums = [4,14,2]
    slu = Solution()
    print(slu.totalHammingDistance(nums))