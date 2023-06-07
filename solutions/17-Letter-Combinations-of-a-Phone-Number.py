class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        subset = []
        res =[]
        def backtrack(i):
            if i == len(digits):
                res.append("".join(subset))
                return
            for letter in phoneMap[digits[i]]:
                subset.append(letter)
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return res
