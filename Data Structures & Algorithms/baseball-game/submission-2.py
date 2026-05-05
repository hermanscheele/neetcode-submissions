class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        scores = []
        for op in operations:

            if op == "+":
                new_score = scores[len(scores)-1] + scores[len(scores)-2]
                scores.append(new_score)
            
            elif op == "D":
                new_score = 2 * scores[len(scores)-1]
                scores.append(new_score)

            elif op == "C":
                scores.pop()

            else: # garunteed integer
                scores.append(int(op))
        
        return sum(scores)
            
