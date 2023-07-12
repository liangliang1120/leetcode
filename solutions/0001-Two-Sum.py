class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


# java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hash = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int value_i = nums[i];
            if (hash.containsKey(target - value_i)) {
                return new int[] { i, hash.get(target - value_i) };
            } 
            hash.put(value_i, i);
        }
        return new int[0];
    }
}
