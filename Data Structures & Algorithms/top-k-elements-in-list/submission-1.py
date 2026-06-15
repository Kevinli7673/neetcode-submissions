class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []
        counter = 0
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        for key in hashmap.keys():
            if(counter == k):
                break
            output.append(key)
            counter += 1;

        return output