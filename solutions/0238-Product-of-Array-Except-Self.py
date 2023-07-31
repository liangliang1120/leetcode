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


# java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] prefix = new int[len];
        prefix[0] = nums[0];
        for (int i = 1; i < len; i++) {
            prefix[i] = nums[i] * prefix[i - 1];
        }
        

        int[] postfix = new int[len];
        postfix[len - 1] = nums[len - 1];
        for (int i = len - 2; i >= 0; i--) {
            postfix[i] = nums[i] * postfix[i + 1];
        }

        int[] res = new int[len];
        for (int i = 0; i < len; i++) {
            if (i == 0) {
                res[i] = postfix[i + 1];
            } else if (i == len - 1) {
                res[i] = prefix[i - 1];
            } else {
                res[i] = postfix[i + 1] * prefix[i - 1];
            }
        }
        return res;
    }
}
