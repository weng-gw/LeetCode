class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n<1:
            return 0
        if n==1:
            return 0 if nums[0]==val else 1
        length = 0
        for j in range(n):
            if nums[length]!=val:
                length+=1
            else:
                nums[length],nums[j] = nums[j],nums[length]
                length += 1 if nums[length]!= val else 0
        return length
