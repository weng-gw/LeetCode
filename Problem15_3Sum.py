class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <3:
            return []
        out = set()
        nums.sort()
        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                if nums[i]+nums[j]+nums[k]==0:
                    out.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k -=1
                else: 
                    j += 1
        return out
        
