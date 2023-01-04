from collections import Counter
'''
hashtable
O(n)
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt_dic = Counter(s)
        for i in range(len(s)):
            if cnt_dic[s[i]] == 1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        nums = list(s)
        for i in range(len(nums)):
            if nums[i] not in frequency:
                frequency[nums[i]] = 1
            else:
                frequency[nums[i]] += 1

        for i in range(len(nums)):
            if frequency[nums[i]] == 1:
                return i
        return -1
