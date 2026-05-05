class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        best = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else:
                current = 0
            if current > best:
                best = current
        
        return best