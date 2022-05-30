# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         char_dict = {}
#         for c in magazine:
#             char_dict[c] = char_dict.get(c, 0)+1
#         for c in ransomNote:
#             char_dict[c] = char_dict.get(c, 0)-1
#             if char_dict[c] == -1:
#                 return False
#         return True

import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
