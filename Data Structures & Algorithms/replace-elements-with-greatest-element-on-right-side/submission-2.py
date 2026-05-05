class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    
        max_seen = -1
        for i in range(len(arr)-1,-1,-1):
            new_max = max(max_seen, arr[i])
            arr[i] = max_seen
            max_seen = new_max
        return arr
                