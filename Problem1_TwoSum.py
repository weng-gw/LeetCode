class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = {}
        for i in range(len(nums)):
            diff  = target - nums[i]
            if diff in mydic:
                return [i,mydic[diff]]
            mydic[nums[i]] = i

