class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]!=i+1):
                return nums[i]