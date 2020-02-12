class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if len(nums) ==1: 
            return 0 if nums[0]>= target else 1
        start = 0
        end = len(nums)
        while start <end:
            mid = (start+end)//2
            if nums[mid]< target:
                start = mid+1
            else:
                end = mid
        return end
