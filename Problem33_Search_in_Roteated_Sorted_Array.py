class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        def bin_search(nums,start,end,target):
            if start == end:
                return start if nums[start]==target else -1
            mid = (start+end)//2
            if nums[start] <= nums[mid] and nums[start]<=target and target<=nums[mid]:
                return bin_search(nums,start,mid,target)
            if nums[start] > nums[mid] and (nums[start]<=target or nums[mid]>=target):
                return bin_search(nums,start,mid,target)
            if nums[mid+1] <= nums[end] and nums[mid+1]<=target and target<=nums[end]:
                return bin_search(nums,mid+1,end,target)
            if nums[mid+1] > nums[end] and (nums[start]<=target or nums[mid+1]>=target):
                return bin_search(nums,mid+1,end,target)
            return -1
        return bin_search(nums,0,len(nums)-1,target)
