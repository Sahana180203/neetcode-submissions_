class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={')':'(','}':'{',']':'['}

        for char in s:
            if char in match:
                top = stack.pop() if stack else "#"
                if match[char]!=top:
                    return False
            else:
                    stack.append(char)
        return not stack
            
        