class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_box(board_data):
            cleaned_data = [x for x in board_data if x!="."]
            return len(cleaned_data)!=len(set(cleaned_data))
        rows = [board[x] for x in range(9)]
        columns = [[board[x][y] for x in range(9)] for y in range(9)]
        boxes = []
        for r in range(0,9,3):
            for c in range(0,9,3):
                box = [board[r+x][c+y] for x in range(3) for y in range(3)]
                boxes.append(box)
        for x in range(9):
            if  is_valid_box(rows[x]) | is_valid_box(columns[x]) | is_valid_box(boxes[x]):
                return False
        return True



        