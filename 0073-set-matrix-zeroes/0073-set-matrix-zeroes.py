class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=[0]*m
        col=[0]*n
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    row[i]=1
                    col[j]=1
        for k in range(m):
            for l in range(n):
                if(row[k]==1 or col[l]==1):
                    matrix[k][l]=0            
        