class Solution:
    def isValid(self, s: str) -> bool:

        closed = [')', ']', '}']
        stack_open = []

        for i in range(len(s)):
            if i == 0 and s[i] in closed:
                return False
            elif i == len(s)-1 and s[i] not in closed:
                return False


            if s[i] == ')':
                if len(stack_open) == 0:
                    return False
                elif stack_open[-1] != '(':
                    return False
                else:
                    stack_open.pop()

            elif s[i] == ']':
                if len(stack_open) == 0:
                    return False
                elif stack_open[-1] != '[':
                    return False
                else:
                    stack_open.pop()

            elif s[i] == '}':
                if len(stack_open) == 0:
                    return False
                elif stack_open[-1] != '{':
                    return False
                else:
                    stack_open.pop()

            else:
                stack_open.append(s[i])            

        return len(stack_open) == 0
            

        