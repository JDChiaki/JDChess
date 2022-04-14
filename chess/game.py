from .constants import *
from .board import Board
from .piece import King


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = WHITE
        self.selected = None
        self.valid_moves = []
        self.winner = None
        self.white_get = []
        self.black_get = []
        self.get = None

    def reset(self):
        self.__init__()

    def update(self):
        self.board.draw_board()
        self.draw_valid_moves()
        pygame.display.update()
        self._check_winner()

    @staticmethod
    def get_row_col(pos):
        x, y = pos
        r = y // SQ_SIZE
        c = x // SQ_SIZE
        return r, c

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            self.valid_moves = []
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != -1 and self.turn == piece.color:
            self.selected = piece
            self.valid_moves = piece.get_valid_moves(self.board)

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and (row, col) in self.valid_moves:
            if piece != -1:
                if piece.color == WHITE:
                    self.black_get.append(piece)
                else:
                    self.white_get.append(piece)
                self.get = piece
                self.board.board[row][col] = -1
            self.board.move(self.selected, row, col)
            self.change_turn()
            return True
        return False

    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def _check_winner(self):
        if self.get:
            if type(self.get) is King:
                self.winner = 'BLACK' if self.get.color == WHITE else 'WHITE'

    def draw_valid_moves(self):
        if self.turn == WHITE:
            out_color = BLACK
            in_color = WHITE
        else:
            out_color = BLACK
            in_color = RED
        for move in self.valid_moves:
            row, col = move
            pygame.draw.circle(WIN, out_color, (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2),
                               SQ_SIZE // 2 - 30)
            pygame.draw.circle(WIN, in_color, (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2),
                               SQ_SIZE // 2 - 40)

    def draw_winner(self):
        color = BLACK if self.winner == 'BLACK' else GRAY
        winner_txt = WINNER_FONT.render(f'{self.winner} WINS!', True, color)
        WIN.blit(winner_txt, (WIDTH//2-winner_txt.get_width()//2, HEIGHT//2-winner_txt.get_height()//2))
