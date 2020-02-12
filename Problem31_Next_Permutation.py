class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        i = n-2
        while i >= 0:
            if nums[i]<nums[i+1]:
                break
            else:
                i -=1
        if i<0:
            nums.reverse()
            return
        j = i+1
        l = n-1
        while j<=l:
            nums[j], nums[l]=nums[l],nums[j]
            j +=1
            l -=1
        for k in range(i+1,n):
            if nums[k]> nums[i]:
                replace =k
                break
        nums[i], nums[replace] = nums[replace],nums[i]
        return
