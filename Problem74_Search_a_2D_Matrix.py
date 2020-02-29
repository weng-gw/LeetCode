class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (not matrix) or (not matrix[0]):
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        rstart = 0
        rend = len(matrix)-1
        while rstart<rend:
            rmid = (rstart+rend)//2+1
            if matrix[rmid][0]>target:
                rend = rmid-1
            else:
                rstart = rmid
        if target <matrix[rstart][0] or target > matrix[rstart][-1]:
            return False
        cstart=0
        cend =len(matrix[0])-1
        while cstart<cend:
            cmid = (cstart+cend)//2+1
            if matrix[rstart][cmid]>target:
                cend = cmid-1
            else:
                cstart=cmid
        return matrix[rstart][cstart]==target
        
