class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        # print(prefix)

        postfix = [1] * len(nums)
        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        # print(postfix)
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
        return res
