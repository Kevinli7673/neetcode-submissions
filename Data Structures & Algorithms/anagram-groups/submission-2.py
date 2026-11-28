"""
Given a array of strings, group anagrams together and return a list of the groups
Idea: for each string - we have a while array 0 - 26 for the alphabet, update each indice base on count of char and make that a hashmap, check if its in seen, if not
we create a new key with value of the string, if seen add string to hashmap
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        seen = set()
        mp = defaultdict(list)

        for word in strs:
            alphabet = [0] * 26
            for char in word:
                alphabet[ord(char)-ord('a')] += 1
            mp[tuple(alphabet)].append(word)

        for sublist in mp:
                res.append(mp[sublist])
        
        return res