class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return n
        length = 1
        j = 1
        for j in range(1,n):
            if nums[j]!=nums[length-1]:
                nums[length],nums[j] = nums[j],nums[length]
                length+=1
        return length
            
