class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_seen = 0
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                max_seen = arr[i]
                arr[i] = -1
            else:
                original = arr[i]
                arr[i] = max_seen
                if max_seen < original:
                    max_seen = original

        return arr
                