# คลาสพื้นฐานสำหรับหมากตัวใดๆ
class Piece:
    def __init__(self, position):
        # pos = (row, column)
        self.position = position

    def can_attack(self, king_pos, board):
        # Default Can't attack
        return False


class Pawn(Piece):
    def can_attack(self, king_pos, board):
        r, c = self.position
        # left top attack (-1 , -1) , right top attack (-1 , 1)
        for dr, dc in [(-1, -1), (-1, 1)]:
            if (r + dr, c + dc) == king_pos:
                return True
        return False


class Bishop(Piece):
    def can_attack(self, king_pos, board):
        # 4 slide directions: (-1, -1), (-1, 1), (1, -1), (1, 1
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        r, c = self.position
        return any(self._can_attack_recursive(r, c, dr, dc, king_pos, board) for dr, dc in directions)

    def _can_attack_recursive(self, r, c, dr, dc, king_pos, board):
        r += dr
        c += dc
        # out of bounds check
        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            return False
        # found the king
        if (r, c) == king_pos:
            return True
        # found piece then stop checking
        if board[r][c] != '.':
            return False

        return self._can_attack_recursive(r, c, dr, dc, king_pos, board)



# คลาสเรือ (Rook)
class Rook(Piece):
    def can_attack(self, king_pos, board):
        # 4 slide directions: (-1, 0), (1, 0), (0, -1), (0, 1)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        r, c = self.position
        return any(self._can_attack_recursive(r, c, dr, dc, king_pos, board) for dr, dc in directions)

    def _can_attack_recursive(self, r, c, dr, dc, king_pos, board):
        r += dr
        c += dc
        # out of bounds check
        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            return False
        # found the king
        if (r, c) == king_pos:
            return True
        # found piece then stop checking
        if board[r][c] != '.':
            return False

        return self._can_attack_recursive(r, c, dr, dc, king_pos, board)



# คลาสราชินี (Queen) รวมการโจมตีแบบ Bishop และ Rook
class Queen(Piece):
    def can_attack(self, king_pos, board):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
        r, c = self.position  # ตั้งค่าเริ่มต้นของ r, c จากตำแหน่งของหมาก
        return any(self._can_attack_recursive(r, c, dr, dc, king_pos, board) for dr, dc in directions)

    def _can_attack_recursive(self, r, c, dr, dc, king_pos, board):
        r += dr
        c += dc
        # out of bounds check
        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            return False
        # found the king
        if (r, c) == king_pos:
            return True
        # found piece then stop checking
        if board[r][c] != '.':
            return False

        return self._can_attack_recursive(r, c, dr, dc, king_pos, board)

# Configuration for the board
class Board:
    def __init__(self, grid):
        self.grid = grid
        self.king_pos = self._find_king()

    def from_string(self, board_str):
        # Split Str board to list board
        rows = board_str.strip().split('\n')
        self.grid = [list(row) for row in rows]
        self.king_pos = self._find_king()

    def _find_king(self):
        # find the position of the king
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == 'K':
                    return (i, j)
        return None

    def is_in_check(self):
        if not self.king_pos:
            return "Fail"

        # Map of pieces to piece classes
        piece_map = {
            'P': Pawn,
            'B': Bishop,
            'R': Rook,
            'Q': Queen
        }

        # Check each piece if it can attack the king
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell in piece_map:
                    piece = piece_map[cell]((i, j))
                    if piece.can_attack(self.king_pos, self.grid):
                        return "Success"
        return "Fail"

def checkmate(board_str):
    try:
        board = Board([])
        board.from_string(board_str)
        print(board.is_in_check())
    except Exception as e:
        print(f"Error")

