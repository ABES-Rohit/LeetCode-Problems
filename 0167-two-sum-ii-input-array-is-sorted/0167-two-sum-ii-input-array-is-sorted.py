class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[0]*2
        for i in range(len(numbers)):
            rem=target-numbers[i]
            if(rem in numbers[i+1:]):
                ans[0]=i+1
                ans[1]=numbers[i+1:].index(rem)+i+2
                break  
        return ans        