class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        temparr = []

        def checkPalidrome(substring):
            l, r = 0, len(substring)-1

            while l <= r:
                if substring[l] != substring[r]:
                    return False
                
                l += 1
                r -= 1
                
            return True

        def recursion(i, tempstring):

            if i >= len(s):
                if tempstring == "":
                    res.append(temparr.copy())
                return
            
            tempstring += s[i]

            if checkPalidrome(tempstring):
                temparr.append(tempstring)
                recursion(i+1, "")
                temparr.pop()
            
            recursion(i+1, tempstring)

        
        recursion(0, "")
        return res
            


            