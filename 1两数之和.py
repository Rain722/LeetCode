from typing import List


# 方法一
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i]+nums[j] == target:
#                     return [i, j]
#         return []

# 方法二
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    slu = Solution()
    print(slu.twoSum([3,2,4], 6))
