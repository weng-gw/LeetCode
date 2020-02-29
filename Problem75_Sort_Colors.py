class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        n0 = 0
        n2 = 0
        i = 0
        while i < n-n2:
            if nums[i]==2:
                nums[n-n2-1],nums[i] = nums[i],nums[n-n2-1]
                n2+=1
            elif nums[i]==0:
                if i==n0:
                    n0+=1
                else:
                    nums[n0],nums[i] = nums[i],nums[n0]
                    n0+=1
                i+=1
            else:
                i+=1
        return nums
