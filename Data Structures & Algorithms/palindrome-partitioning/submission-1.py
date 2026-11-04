"""
We want to return an array of list where each list stores the string, 
however each element is a substring that all create the string and each
element is storing a palidrome substring

Idea: We iterate through each character of the string starting at index 0, we have two options: 
 1. add the next char - the next call will check the palidrome status
 2. Stop and add that as a palidrome substring
 We have to also store an temp arry that stores our current substrings
 Because with my high overview idea, we have to make sure that we adding
 substrings that should be a part of another sub list
 To fix this: Whenever we add a substring to the temp list, we can reset
 the substring and restart
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def checkPalidrome(word):
            l = 0
            r = len(word)-1

            while l <= r:
                if word[l] != word[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        def recursion(substring, temparr, i):
            
            if i >= len(s):
                if substring == "":
                    res.append(temparr.copy())
                return

            substring += s[i]

            if checkPalidrome(substring):
                temparr.append(substring)
                recursion("", temparr, i+1)
                temparr.pop()
            
            recursion(substring, temparr, i+1)

        recursion("", [], 0)
        return res
            




            
            
            
            
            
            

            





