from board import Board
import pygame
from random import choice
import sys
from math import floor

# colours
R = (255, 0, 0)
O = (255, 127, 0)
Y = (255, 255, 0)
G = (0, 255, 0)
B = (0, 0, 255)
I = (75, 0, 130)
V = (148, 0, 211)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self, grid_size = 10, fps=30, play=False):
        self.size = grid_size
        self.fps = fps
        self.play = play
        self.board = Board(grid_size)
    
    def next(self) -> None:
        self.board.next_state()
    
    def play_game(self) -> None:    
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.size ** 2, self.size ** 2))
        pygame.display.set_caption("John Conway's game of life: Press Enter to start/pause simulation")
        game_mode = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_mode = not game_mode
                    if event.key == pygame.K_RETURN:
                        if self.play:
                            self.play = False
                            pygame.display.set_caption(
                                "Conway's Game Of Life - Press ENTER to start/pause simulation (stopped)"
                            )
                        else:
                            self.play = True
                            pygame.display.set_caption(
                                "Conway's Game Of Life - Press ENTER to start/pause simulation (running)"
                            )
                if event.type == pygame.MOUSEBUTTONUP:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    row = floor(pos_x / self.size)
                    col = floor(pos_y / self.size)
                    if self.board.state[row, col]:
                        self.board.state[row, col] = 0
                    else:
                        self.board.state[row, col] = 1

            self.next()

            for row in range(0, self.size):
                for col in range(0, self.size):
                    if self.board.state[row, col]:
                        if game_mode:
                            pygame.draw.rect(
                                screen, choice([R, O, Y, G, B, I, V]), (row * self.size, col * self.size, self.size, self.size), 0
                            )
                        else:
                            pygame.draw.rect(screen, BLACK, (row * self.size, col * self.size, self.size, self.size), 0)
                    else:
                        pygame.draw.rect(screen, WHITE, (row * self.size, col * self.size, self.size, self.size), 0)

            pygame.display.update()
            clock.tick(self.fps)


