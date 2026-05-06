class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False

        n = len(nums)
        d = {}
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = i
            
            else: # duplicate
                j = d[nums[i]]
                if j == i: 
                    continue
                if abs(i-j) <= k:
                    return True
                else: # update index in d
                    d[nums[i]] = i
        
        return False


