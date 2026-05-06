class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        l = []
        for i in range(len(strs)):
            wi = strs[i]
            anagram = [wi]
            for j in range(len(strs)):
                if i == j: continue

                wj = strs[j]
                if sorted(wi) == sorted(wj):
                    anagram.append(wj) 

            anagram.sort()
            if anagram not in l:
                l.append(anagram)
    
        return l

        

                