from chess import *


def _winner_loop(_game):
    while _game.winner:
        CLOCK.tick(FPS)
        _game.draw_winner()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    _game.reset()
                    break
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def main():
    running = True
    _game = Game()
    while running:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if _game.winner:
                _winner_loop(_game)
            if event.type == pygame.MOUSEBUTTONDOWN:
                _game.select(*_game.get_row_col(pygame.mouse.get_pos()))
            if event.type == pygame.QUIT:
                running = False
                break
        _game.update()
    pygame.quit()
    exit()


if __name__ == '__main__':
    main()
