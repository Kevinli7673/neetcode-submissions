class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        for char in s:
            if(not char.isalnum()):
                s = s.replace(char, "")
        s = s.lower()
        print(s)
        l, r = 0, len(s)-1

        for i in range(int((len(s))/2)):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True