class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        obstacleGrid[0][0]=1
        for i in range(1,len(obstacleGrid)):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0]==1 else obstacleGrid[i-1][0]
        for j in range(1,len(obstacleGrid[0])):
            obstacleGrid[0][j] = 0 if obstacleGrid[0][j]==1 else obstacleGrid[0][j-1]
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j]==1 else obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
