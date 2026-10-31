""""
Return an array which each element is a n pairs of parentheses
that are well-formed

What if each recursion call, we store the amt of open and 
closing parentheses. We check amt of opening compared to close
, we can only add closing if its less than opening amt. And we
also have to make sure that our opening parenthesis is less
than or equal to n
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def recursion(n, curr, opening, closing):

            if opening + closing == n * 2:
                string = ""
                for i in curr:
                    string += i
                res.append(string)
                return

            if(opening < n):
                curr.append("(")
                recursion(n, curr, opening+1, closing)
                curr.pop()
            if(closing < opening):
                curr.append(")")
                recursion(n, curr, opening, closing+1)
                curr.pop()

        recursion(n, [], 0, 0)
        return res

            
