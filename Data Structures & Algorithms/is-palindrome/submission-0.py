class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        cleaned=''.join(char.lower() for char in s if char.isalnum()) 

        
        left, right = 0, len(cleaned)-1
        while left<right:
            if cleaned[left]!=cleaned[right]:
                return False
            left=left+1
            right=right-1
        return True


        