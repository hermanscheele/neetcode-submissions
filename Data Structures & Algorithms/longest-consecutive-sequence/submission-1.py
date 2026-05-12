class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        n = len(nums)
        seqs = []

        for i in range(n):
            seq = 1
            num1 = nums[i]

            for j in range(n):
                if i == j: continue
                num2 = nums[j]

                if num2 == num1 + 1:
                    seq += 1
                    num1 = num2
            
            seqs.append(seq)

        if seqs:
            return max(seqs)
        else: return 0
