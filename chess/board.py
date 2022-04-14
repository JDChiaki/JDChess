from .constants import *
from .piece import Pawn, Rook, Knight, Bishop, Queen, King


class Board:
    def __init__(self):
        self.board = []

    def _create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 1:
                    self.board[row].append(Pawn(row, col, BLACK))
                elif row == ROWS - 2:
                    self.board[row].append(Pawn(row, col, WHITE))
                elif row == 0:
                    if col == 0 or col == COLS - 1:
                        self.board[row].append(Rook(row, col, BLACK))
                    elif col == 1 or col == COLS - 2:
                        self.board[row].append(Knight(row, col, BLACK))
                    elif col == 2 or col == COLS - 3:
                        self.board[row].append(Bishop(row, col, BLACK))
                    elif col == 3:
                        self.board[row].append(Queen(row, col, BLACK))
                    elif col == 4:
                        self.board[row].append(King(row, col, BLACK))
                elif row == ROWS - 1:
                    if col == 0 or col == COLS - 1:
                        self.board[row].append(Rook(row, col, WHITE))
                    elif col == 1 or col == COLS - 2:
                        self.board[row].append(Knight(row, col, WHITE))
                    elif col == 2 or col == COLS - 3:
                        self.board[row].append(Bishop(row, col, WHITE))
                    elif col == 3:
                        self.board[row].append(Queen(row, col, WHITE))
                    elif col == 4:
                        self.board[row].append(King(row, col, WHITE))
                else:
                    self.board[row].append(-1)

    def _draw_pieces(self):
        self._create_board()
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != -1:
                    piece.draw()

    def draw_board(self):
        WIN.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(WIN, RED, (row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        self._draw_pieces()

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]
