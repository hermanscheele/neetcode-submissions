class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashmap = dict()
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            elif n in hashmap:
                return True
        return False
