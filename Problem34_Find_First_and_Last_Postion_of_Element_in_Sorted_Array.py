class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<1:
            return [-1,-1]
        if len(nums)==1:
            myid = -1 if nums[0]!=target else 0
            return [myid,myid]
        start1 = 0
        start2 = 0
        end1 = len(nums)-1
        end2 = len(nums)-1
        
        while start1 < end1:
            mid1 = (start1+end1)//2
            if nums[mid1] >= target:
                end1 = mid1
            else:
                start1 = mid1+1
        while start2 < end2:
            mid2 = (start2+end2)//2+1
            if nums[mid2] <= target:
                start2 = mid2
            else:
                end2 = mid2-1

        if nums[start1]==target and nums[start2]==target:
            return [start1,start2]
        else:
            id1 = start1 if nums[start1]== target else -1
            id2 = start2 if nums[start2]== target else -1
            return 2*[max(id1,id2)]
