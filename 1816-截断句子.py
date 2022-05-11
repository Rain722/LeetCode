class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # return " ".join((s.split(" "))[:k])
        idx = None
        for i, c in enumerate(s):
            if c == " ":
                k -= 1
            if not k:
                idx = i
                break
        return s[:idx] if idx is not None else s


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    slu = Solution();
    print(slu.truncateSentence("ni hao a", 2))
