class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Each indice stores a number, which represents the maximum jump i can do at that indice
        This means that we have to make sure that our pointer doesn't land on a zero
        If so, that means we can't reach the last indice

        This means we have to make sure that our jump doesn't land on a zero
        But what if we don't need to check that we landed on a zero
        We can have a variable that stores the jump amount and each time we land on a indice
        We check if that value is bigger than our current jump amt, if so we change our jump
        amnt to that if not we continue
        """

        jumpamt = nums[0]
        i = 0

        while(jumpamt >= 0):
            if(i >= len(nums)-1):
                return True
            
            if(jumpamt < nums[i]):
                jumpamt = nums[i]
            
            i += 1
            jumpamt -= 1
        
        return False