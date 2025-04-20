from collections import defaultdict
from typing import List


class Solution:
    def dfs(self,letters,word,visited,let):
        if len(word) == 1:
            return True
        else:
            next_letter = word[1]
            for child in letters[let]:
                if child not in visited and child[0] == next_letter:
                    visited.append(child)
                    if self.dfs(letters, word[1:], visited, child):
                        return True
                    else:
                        visited.remove(child)
                        continue


            return False
    def exist(self, board: List[List[str]], word: str) :
        if len(word) <=1 and word[0]==board[0][0]:
            return True
        letters = defaultdict(list)
        for row in range(len(board)):
            for letter in range(len(board[row])):
                if row > 0:
                    letters[f'{board[row ][letter]}{letter}{row}'].append(f'{board[row -1 ][letter]}{letter}{row-1}')
                if row < len(board) - 1 :
                    letters[f'{board[row ][letter]}{letter}{row}'].append(f'{board[row +1 ][letter]}{letter}{row+1}')
                if letter < len(board[row]) - 1:
                    letters[f'{board[row ][letter]}{letter}{row}'].append(f'{board[row ][letter+1]}{letter+1}{row}')
                if letter > 0 :
                    letters[f'{board[row ][letter]}{letter}{row}'].append(f'{board[row ][letter-1]}{letter-1}{row}')
        for i in letters.keys():
            if i[0] == word[0]:
                if self.dfs(letters,word,visited=[i],let=i):
                    return True
        return False
print(Solution().exist(board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS"))