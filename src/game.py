import pygame
from pygame import QUIT

from constants import WIDTH, HEIGHT
from game_state import GameState
from score_manager_db import ScoreManagerDB

class Game:
    """
    Main game controller class responsible for managing the game loop and state transitions.

    Attributes:
        screen (Surface): Pygame surface representing the game window
        clock (Clock): Game timing controller
        state (PlaceholderState): Current game state
        username (str): Player's username
        score_manager_db (ScoreManagerDB): Database manager for handling scores
    """
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((int(WIDTH), int(HEIGHT)))
        pygame.display.set_caption("ENDLESS RUNNER")
        self.clock = pygame.time.Clock()
        self.state = GameState()
        self.username = ""
        self.score_manager_db = ScoreManagerDB()

    def change_state(self, new_state) -> None:
        self.state = new_state

    def run(self) -> None:
        running = True
        while running:
            [pygame.quit() for event in pygame.event.get() if event.type == QUIT and (running := False)]
            self.state.handle_events(pygame.event.get())
            self.state.update()
            self.state.render()
            pygame.display.flip()
            self.clock.tick(60)