import pygame
from constants import INITIAL_SPEED
from notes.example import EntityFactory
from game_state import GameState

class GamePlayState(GameState):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.player = EntityFactory.create_entity('player')
        self.obstacles = []
        self.clouds = []
        self.ground = EntityFactory.create_entity('ground', speed=INITIAL_SPEED)
        self.game_speed = INITIAL_SPEED
        self.score = 0
        self.game_over = False

        self.obstacle_timer = 0
        self.last_obstacle_time = pygame.time.get_ticks()

        self.font = pygame.font.SysFont("Arial", 20)