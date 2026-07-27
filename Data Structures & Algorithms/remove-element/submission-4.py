class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = len(nums);
        i = 0
        length = len(nums)

        while(i < length):
            length = len(nums)
            if nums[i] == val:
                nums.pop(i)
                counter -= 1
                length = len(nums)
                nums.append(51)
                if(i != 0):
                    i -= 1
            if nums[i] != val:
                i += 1
        
        return counter