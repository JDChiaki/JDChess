import pygame
import os

pygame.init()

WIDTH = HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JDChess')
ICON = pygame.image.load(os.path.join('assets', 'icon.svg')).convert_alpha()
pygame.display.set_icon(ICON)

ROWS = COLS = 8
SQ_SIZE = WIDTH // ROWS

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

WINNER_FONT = pygame.font.Font(os.path.join('assets', 'LHANDW.TTF'), 100)

W_PAWN = pygame.image.load(os.path.join('assets', 'white', 'pawn_w.svg'))
W_ROOK = pygame.image.load(os.path.join('assets', 'white', 'rook_w.svg'))
W_KNIGHT = pygame.image.load(os.path.join('assets', 'white', 'knight_w.svg'))
W_BISHOP = pygame.image.load(os.path.join('assets', 'white', 'bishop_w.svg'))
W_QUEEN = pygame.image.load(os.path.join('assets', 'white', 'queen_w.svg'))
W_KING = pygame.image.load(os.path.join('assets', 'white', 'king_w.svg'))

B_PAWN = pygame.image.load(os.path.join('assets', 'black', 'pawn_b.svg'))
B_ROOK = pygame.image.load(os.path.join('assets', 'black', 'rook_b.svg'))
B_KNIGHT = pygame.image.load(os.path.join('assets', 'black', 'knight_b.svg'))
B_BISHOP = pygame.image.load(os.path.join('assets', 'black', 'bishop_b.svg'))
B_QUEEN = pygame.image.load(os.path.join('assets', 'black', 'queen_b.svg'))
B_KING = pygame.image.load(os.path.join('assets', 'black', 'king_b.svg'))

PIECE_SIZE = (50, 70)
