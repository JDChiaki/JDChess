from .constants import *


class Piece:
    def __init__(self, row, col, color, w, b):
        self.row = row
        self.col = col
        self.color = color
        self.w = w
        self.b = b
        self.x = self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * SQ_SIZE + SQ_SIZE // 2
        self.y = self.row * SQ_SIZE + SQ_SIZE // 2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self):
        if self.color == WHITE:
            WIN.blit(self.w, (self.x - self.w.get_width() // 2, self.y - self.w.get_height() // 2))
        if self.color == BLACK:
            WIN.blit(self.b, (self.x - self.b.get_width() // 2, self.y - self.b.get_height() // 2))

    def get_valid_moves(self, board):
        pass


class Pawn(Piece):
    W_PAWN = pygame.transform.scale(W_PAWN, PIECE_SIZE).convert_alpha()
    B_PAWN = pygame.transform.scale(B_PAWN, PIECE_SIZE).convert_alpha()

    def __init__(self, row, col, color):
        super().__init__(row, col, color, self.W_PAWN, self.B_PAWN)

    def get_valid_moves(self, board):
        moves = []
        if self.color == WHITE:
            if board.board[self.row - 1][self.col] == -1:
                moves.append((self.row - 1, self.col))
                if self.row == ROWS - 2 and board.board[self.row - 2][self.col] == -1:
                    moves.append((self.row - 2, self.col))
            if board.board[self.row - 1][self.col + 1] != -1:
                piece = board.get_piece(self.row - 1, self.col + 1)
                if piece.color != self.color:
                    moves.append((self.row - 1, self.col + 1))
            if board.board[self.row - 1][self.col - 1] != -1:
                piece = board.get_piece(self.row - 1, self.col - 1)
                if piece.color != self.color:
                    moves.append((self.row - 1, self.col - 1))
        elif self.color == BLACK:
            if board.board[self.row + 1][self.col] == -1:
                moves.append((self.row + 1, self.col))
                if self.row == 1 and board.board[self.row + 2][self.col] == -1:
                    moves.append((self.row + 2, self.col))
            if board.board[self.row + 1][self.col - 1] != -1:
                piece = board.get_piece(self.row + 1, self.col - 1)
                if piece.color != self.color:
                    moves.append((self.row + 1, self.col - 1))
            if board.board[self.row + 1][self.col + 1] != -1:
                piece = board.get_piece(self.row + 1, self.col + 1)
                if piece.color != self.color:
                    moves.append((self.row + 1, self.col + 1))
        return moves


class Rook(Piece):
    W_ROOK = pygame.transform.scale(W_ROOK, PIECE_SIZE).convert_alpha()
    B_ROOK = pygame.transform.scale(B_ROOK, PIECE_SIZE).convert_alpha()

    def __init__(self, row, col, color):
        super().__init__(row, col, color, self.W_ROOK, self.B_ROOK)

    def get_valid_moves(self, board):
        moves = []
        for row in range(self.row - 1, -1, -1):
            if board.board[row][self.col] == -1:
                moves.append((row, self.col))
            else:
                piece = board.get_piece(row, self.col)
                if self.color != piece.color:
                    moves.append((row, self.col))
                break
        for row in range(self.row + 1, ROWS):
            if board.board[row][self.col] == -1:
                moves.append((row, self.col))
            else:
                piece = board.get_piece(row, self.col)
                if self.color != piece.color:
                    moves.append((row, self.col))
                break
        for col in range(self.col + 1, COLS):
            if board.board[self.row][col] == -1:
                moves.append((self.row, col))
            else:
                piece = board.get_piece(self.row, col)
                if self.color != piece.color:
                    moves.append((self.row, col))
                break
        for col in range(self.col - 1, -1, -1):
            if board.board[self.row][col] == -1:
                moves.append((self.row, col))
            else:
                piece = board.get_piece(self.row, col)
                if self.color != piece.color:
                    moves.append((self.row, col))
                break
        return moves


class Knight(Piece):
    W_KNIGHT = pygame.transform.scale(W_KNIGHT, PIECE_SIZE).convert_alpha()
    B_KNIGHT = pygame.transform.scale(B_KNIGHT, PIECE_SIZE).convert_alpha()

    def __init__(self, row, col, color):
        super().__init__(row, col, color, self.W_KNIGHT, self.B_KNIGHT)

    def get_valid_moves(self, board):
        moves = []
        possible_moves = [(self.row - 2, self.col - 1), (self.row - 2, self.col + 1), (self.row + 2, self.col - 1),
                          (self.row + 2, self.col + 1), (self.row - 1, self.col - 2), (self.row + 1, self.col - 2),
                          (self.row - 1, self.col + 2), (self.row + 1, self.col + 2)]
        for move in possible_moves:
            try:
                piece = board.get_piece(*move)
            except IndexError:
                continue
            if piece == -1 or piece.color != self.color:
                moves.append(move)
        return moves


class Bishop(Piece):
    W_BISHOP = pygame.transform.scale(W_BISHOP, PIECE_SIZE).convert_alpha()
    B_BISHOP = pygame.transform.scale(B_BISHOP, PIECE_SIZE).convert_alpha()

    def __init__(self, row, col, color):
        super().__init__(row, col, color, self.W_BISHOP, self.B_BISHOP)

    def get_valid_moves(self, board):
        moves = []
        for i in range(1, min(COLS - self.col, ROWS - self.row)):  # right down
            if board.board[self.row + i][self.col + i] == -1:
                moves.append((self.row + i, self.col + i))
            else:
                piece = board.get_piece(self.row + i, self.col + i)
                if piece.color != self.color:
                    moves.append((self.row + i, self.col + i))
                break
        for i in range(1, min(self.col + 1, ROWS - self.row)):  # left down
            if board.board[self.row + i][self.col - i] == -1:
                moves.append((self.row + i, self.col - i))
            else:
                piece = board.get_piece(self.row + i, self.col - i)
                if piece.color != self.color:
                    moves.append((self.row + i, self.col - i))
                break
        for i in range(1, min(COLS - self.col, self.row + 1)):  # right up
            if board.board[self.row - i][self.col + i] == -1:
                moves.append((self.row - i, self.col + i))
            else:
                piece = board.get_piece(self.row - i, self.col + i)
                if piece.color != self.color:
                    moves.append((self.row - i, self.col + i))
                break
        for i in range(1, min(self.col + 1, self.row + 1)):  # left up
            if board.board[self.row - i][self.col - i] == -1:
                moves.append((self.row - i, self.col - i))
            else:
                piece = board.get_piece(self.row - i, self.col - i)
                if piece.color != self.color:
                    moves.append((self.row - i, self.col - i))
                break
        return moves


class Queen(Piece):
    W_QUEEN = pygame.transform.scale(W_QUEEN, PIECE_SIZE).convert_alpha()
    B_QUEEN = pygame.transform.scale(B_QUEEN, PIECE_SIZE).convert_alpha()

    def __init__(self, row, col, color):
        super().__init__(row, col, color, self.W_QUEEN, self.B_QUEEN)

    def get_valid_moves(self, board):
        bishop = Bishop(self.row, self.col, self.color)
        rook = Rook(self.row, self.col, self.color)
        moves = bishop.get_valid_moves(board) + rook.get_valid_moves(board)
        return moves


class King(Piece):
    W_KING = pygame.transform.scale(W_KING, PIECE_SIZE).convert_alpha()
    B_KING = pygame.transform.scale(B_KING, PIECE_SIZE).convert_alpha()

    def __init__(self, row, col, color):
        super().__init__(row, col, color, self.W_KING, self.B_KING)

    def get_valid_moves(self, board):
        moves = []
        possible_moves = [(self.row - 1, self.col + 1), (self.row, self.col + 1), (self.row + 1, self.col + 1),
                          (self.row + 1, self.col), (self.row + 1, self.col - 1), (self.row, self.col - 1),
                          (self.row - 1, self.col - 1), (self.row - 1, self.col)]
        for move in possible_moves:
            try:
                piece = board.get_piece(*move)
            except IndexError:
                continue
            if piece == -1 or piece.color != self.color:
                moves.append(move)
        return moves
