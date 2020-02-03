class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        out = None
        for i in range(n):
            j = i+1
            k = n-1
            while j< k:
                s = nums[i]+nums[j]+nums[k]
                if out is None:
                    out = s
                elif s==target:
                    return s
                elif abs(s-target)< abs(out-target):
                    out = s
                if s > target:
                    k-=1
                else:
                    j+=1
        return out
