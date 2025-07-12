class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                sm=nums[i]+nums[j]+nums[k]
                if(sm<0):
                    j=j+1
                elif(sm>0):
                    k=k-1
                else:
                    l=[nums[i],nums[j],nums[k]]
                    ans.append(l)
                    j=j+1
                    k=k-1
                    while(j<k and nums[j]==nums[j-1]):
                        j=j+1
                    while(j<k and nums[k]==nums[k+1]):
                        k=k-1                
        return ans            
        