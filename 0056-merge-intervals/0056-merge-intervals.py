class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        pre,j=0,1
        while(j<len(intervals)):
            if(ans[pre][1]>=intervals[j][0]):
                if(ans[pre][1]<intervals[j][1]):
                    ans[pre][1]=intervals[j][1]    
            else:
                ans.append(intervals[j])
                pre=pre+1
            j=j+1
        return ans        
