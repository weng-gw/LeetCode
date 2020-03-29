class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n==1:
            return triangle[0][0]
        triangle[1][0]+=triangle[0][0]
        triangle[1][1]+=triangle[0][0]
        if n==2:
            return min(triangle[1])
        for i in range(2,n):
            triangle[i][0]+=triangle[i-1][0]
            triangle[i][-1]+=triangle[i-1][-1]
            for j in range(1,i):
                triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])
