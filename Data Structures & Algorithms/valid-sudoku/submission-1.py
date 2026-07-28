class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows  = defaultdict(set)
        cols  = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                current = board[r][c]
                
                if current == ".":
                    continue
                
                if current in rows[r] or current in cols[c] or current in boxes[(r//3, c//3)]:
                    return False
                
                rows[r].add(current)
                cols[c].add(current)
                boxes[(r//3, c//3)].add(current)
        
        return True