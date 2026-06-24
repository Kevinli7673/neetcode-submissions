class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # To not repeat work, use two pointers i and j
        # i = 1st element, j = last element

        i = 0
        j = len(numbers) -1 

        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
        return [i+1, j+1]