class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        s = ' ' + s
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1,n + 1):
            # a : 代表「当前位置」单独形成 item
            # b : 代表「当前位置」与「前一位置」共同形成 item
            a = ord(s[i]) - ord('0')
            b = ( ord(s[i - 1]) - ord('0') ) * 10 + ord(s[i]) - ord('0')
            
            # 如果 a 属于有效值，那么 f[i] 可以由 f[i - 1] 转移过来
            if 1 <= a <= 9:
                f[i] = f[i - 1]
            # 如果 b 属于有效值，那么 f[i] 可以由 f[i - 2] 或者 f[i - 1] & f[i - 2] 转移过来
            if 10 <= b <= 26:
                f[i] += f[i - 2]
        return f[n]
