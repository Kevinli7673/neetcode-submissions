class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        dict2 = {}  
        innerlist = []
        outerlist = []

        for i in range(len(strs)):
            dict1.clear()
            dict2.clear()
            innerlist.clear()
            for char in strs[i]:
                dict1[char] = 1 + dict1.get(char, 0)
            if any(strs[i] in sublist for sublist in outerlist):
                continue
            else:
                innerlist.append(strs[i])
            for x in range(len(strs)):
                dict2.clear()
                for chars in strs[x]:
                    dict2[chars] = 1 + dict2.get(chars, 0)
                if(dict1 == dict2 and x != i):
                    innerlist.append(strs[x])
            outerlist.append(innerlist.copy())

        return outerlist