class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0: return []

        res = []
        for i in range(k):
            
            d = {}
            for num in nums:
                if num in res:
                    continue
                
                if num not in d:
                    d[num] = 1
                else:
                    d[num] += 1
            
            
            m_num = None
            m_count = 0
            for num, count in d.items():
                if count > m_count:
                    m_count = count
                    m_num = num
            
            res.append(m_num)

        return res
