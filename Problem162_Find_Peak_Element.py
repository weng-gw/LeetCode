class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bin_search(start,end,nums):
            while start<end:
                mid = (start+end)//2
                mid_left = nums[mid - 1] if mid>0 else -float("Inf")
                mid_right = nums[mid+1]
                if mid_left < nums[mid] and mid_right<nums[mid]:
                    return mid
                elif mid_left< nums[mid] and mid_right>nums[mid]:
                    start = mid+1
                else:
                    end = mid
            return start
        return bin_search(0,len(nums)-1,nums)
