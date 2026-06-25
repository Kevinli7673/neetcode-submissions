class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1
        
        for i in range(int((len(s))/2)):
            while not s[l].isalnum():
                l += 1
                if l == len(s) -1:
                    break
            while not s[r].isalnum():
                r -= 1
                if r == 0:
                    break
            if s[l].lower() != s[r].lower() and s[l].isalnum():
                return False
            l += 1
            r -= 1
        return True