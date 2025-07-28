class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        top,botm=0,m-1
        while(top<=botm):
            mid=(top+botm)//2
            if(matrix[mid][0] < target and matrix[mid][-1] > target):
                break
            elif(matrix[mid][0] > target):
                botm=mid-1
            else:
                top=mid+1
        row = (top+botm)//2
        left,right=0,n-1
        while(left<=right):
            mid=(left+right)//2
            if(matrix[row][mid] == target):
                return True
            elif(matrix[row][mid] > target):
                right=mid-1
            else:
                left=mid+1
        return False            