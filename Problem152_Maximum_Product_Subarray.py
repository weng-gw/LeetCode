class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cum_max = nums[0]
        cum_min = nums[0]
        final_max = nums[0]
        
        for i in range(1,len(nums)):
            temp = cum_max
            cum_max = max(cum_max*nums[i],cum_min*nums[i],nums[i])
            cum_min = min(temp*nums[i],cum_min*nums[i],nums[i])
            if cum_max>final_max:
                final_max = cum_max
        return final_max
        
