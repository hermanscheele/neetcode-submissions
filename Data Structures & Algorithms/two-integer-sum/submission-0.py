class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i in range(len(nums)):
            n = nums[i]
            c = target - n

            if c in d:
                return [d[c], i]

            d[n] = i

        return -1
