
'''
time O(nklogk) n字符串的数量 k字符串最大长度
klogk排序 需要遍历 n 个字符串
space O(nk)

排序后，加进字典
{aet:[],
ant:[],
abt:[]
}

如果单个word非常长并且只有几个不同的字母

如果是一段连续的很大量的数据 hash function

大写字母怎么处理？
'''
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        word_dict = dict()
        for word in strs:
            sorted_word = "".join(sorted(list(word)))
            if sorted_word not in word_dict.keys():
                word_dict[sorted_word] = [word]
            else:
                word_dict[sorted_word].append(word)
        
        for key, value in word_dict.items():
            res.append(value)
        return res
    
s = Solution()
res = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat", "Ate", "Aet", "Bat"])
print(res)

# x= 'A'
# m = x.lower()
# print(m)


'''
解法2:count
time O(n(k+26)) n字符串的数量 k字符串最大长度
klogk排序 需要遍历 n 个字符串
time O(n(k+26))
{(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], 
(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'],
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']})

'''    
    
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         mp = collections.defaultdict(list)

#         for st in strs:
#             counts = [0] * 26
#             for ch in st:
#                 counts[ord(ch) - ord("a")] += 1
#             # 需要将 list 转换成 tuple 才能进行哈希
#             mp[tuple(counts)].append(st)
        
#         return list(mp.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for w in strs:
            sorted_w = sorted(w)
            # print("".join(sorted_w))
            hashmap["".join(sorted_w)].append(w)
        return list(hashmap.values())

