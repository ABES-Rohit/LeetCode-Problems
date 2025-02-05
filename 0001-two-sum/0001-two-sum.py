class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j=0
        for i in range(len(nums)):
            if(target-nums[i]) in nums[i+1:]:
                x=nums[i]
                nums.remove(x)
                j=nums.index(target-x)
                break
        l=list()
        l.append(i)
        l.append(j+1)  
        return l          