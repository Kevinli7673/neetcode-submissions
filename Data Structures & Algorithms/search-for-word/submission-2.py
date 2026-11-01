"""
So we're trying to find a word in a 2d array, where the word
is connected horizontally and vertically
So like num islands, when the current element is the first
character of the string, we call dfs top, right, bottom, down
each recursively, holding a local array of the current string
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(board, r, c, mr, mc, indexamt):

            if indexamt == len(word):
                return True

            if r < 0 or r == mr or c < 0 or c == mc or word[indexamt] != board[r][c]:
                return 
            
            temp = board[r][c]
            board[r][c] = "#"

            for d in direction:
                if dfs(board, r+d[0], c+d[1], mr, mc, indexamt + 1):
                    return True
                
            board[r][c] = temp
            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == word[0]):
                    result = dfs(board, i, j, len(board), len(board[0]), 0)
                    if result == True:
                        return result
        
        return False
