class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        count =0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while True:
                nex = (current+k)%len(nums)
                temp = nums[nex]
                nums[nex] = prev
                prev = temp
                current = nex
                count +=1
                if current==start:
                    break
            start+=1
