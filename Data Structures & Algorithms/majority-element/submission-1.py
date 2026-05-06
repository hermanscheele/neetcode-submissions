class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
                continue
            
            d[num] += 1
        
        #max_num = -1
        #max_count = -1
        #for num, count in d.items():
        #    if count > max_count:
        #        max_count = count
        #        max_num = num
        

        max_num = max(d, key=d.get) 
        return max_num
        
