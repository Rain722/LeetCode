
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

输入：s = "([)]"
输出：false
"""



class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': "{", ']': '['}
        stack = []
        for paren in s:
            if paren in pairs.values():
                stack.append(paren)
            elif paren in pairs.keys():
                if stack == [] or stack.pop() != pairs[paren]:
                    return False
            else:
                return False
        return stack == []


if __name__ == "__main__":
    slu = Solution()
    s = "()[]{}"
    print(slu.isValid(s))