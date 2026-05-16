class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1        
            elif n in d:
                d[n] += 1
            
        for num, count in d.items():
            if count == 1:
                return num


        return 0