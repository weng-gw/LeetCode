class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if len(nums)==2:
            return nums[0]>=1
        for i in range(1,len(nums)-1):
            if nums[i-1]>=i:
                nums[i] = max(i+nums[i],nums[i-1])
            else:
                nums[i] = nums[i-1]
        return nums[-2]>=len(nums)-1
