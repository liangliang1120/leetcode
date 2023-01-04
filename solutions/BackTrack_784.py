class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(i, strr):
            if len(strr) == len(s):
                res.append(strr)
                return res # 

            if s[i + 1].isdigit():
                backtrack(i + 1, strr +s[i + 1])
            else:
                for next_ch in [s[i+1].lower(), s[i+1].upper()]:
                    backtrack(i + 1,strr+next_ch)

        res = []
        backtrack(-1, '')
        return res
