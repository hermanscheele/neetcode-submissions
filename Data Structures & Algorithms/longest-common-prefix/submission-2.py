class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pfx = ''
        ref = strs[0]
        for i in range(len(ref)):
            p = ref[i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != p:
                    return pfx

            pfx += p
        
        return pfx



        



                