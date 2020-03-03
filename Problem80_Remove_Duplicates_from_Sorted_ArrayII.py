class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n_nums = -1
        for i in range(len(nums)):
            if n_nums<1:
                n_nums+=1
            elif nums[i]!=nums[n_nums-1]:
                nums[i],nums[n_nums+1] = nums[n_nums+1],nums[i]
                n_nums+=1
        return n_nums+1
