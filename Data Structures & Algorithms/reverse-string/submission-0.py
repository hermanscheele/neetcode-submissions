class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        left = 0
        right = n-1

        while left < right:
            right_elm = s[right]
            left_elm = s[left]
            
            s[right] = left_elm
            s[left] = right_elm

            left+=1
            right-=1

