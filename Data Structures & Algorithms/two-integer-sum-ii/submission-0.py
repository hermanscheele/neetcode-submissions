class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        p1 = 0
        p2 = len(numbers)-1

        for i in range(len(numbers)):
            s = numbers[p2] + numbers[p1]
            
            if s < target:
                p1+=1
            
            elif s > target:
                p2-=1
            
            elif s == target:
                return [p1+1, p2+1]