import pygame
from pygame.locals import *
from Snake import Snake
from Apple import Apple
from Graph import Graph
import time
import random


class Game:
    def __init__(self, game_width=500, game_height=500):
        pygame.init()
        self.__main_window = pygame.display.set_mode((game_width, game_height))
        self.__snake = Snake(self.__main_window, length=1)
        self.__apple = self.create_apple()
        self.__snake.draw()
        self.__running = True
        self.__pause = False
        self.__graph = Graph(game_width, game_height, self.__snake.get_block_size())
        self.__graph.initiate_graph()

    def play(self):
        self.__snake.walk()
        self.__apple.draw()
        self.display_score()
        # print(self.create_graph())
        co = self.__snake.get_coordinates()
        prev = self.__snake.get_previous_tail_position()
        self.disconnect_node(co[0], co[1])
        self.__graph.insert_node(prev[0]//self.__snake.get_block_size(), prev[1]//self.__snake.get_block_size())
        print(self.__graph.get_graph_size())
        if self.is_collision(self.__snake.get_coordinates(), self.__apple.get_coordinates()):
            self.__snake.eat_apple()
            self.__apple = self.create_apple()

        if self.snake_crashed():
            self.__pause = True

    def is_collision(self, coord1, coord2):
        if coord2[0] <= coord1[0] < coord2[0] + self.__snake.get_block_size():
            if coord2[1] <= coord1[1] < coord2[1] + self.__snake.get_block_size():
                return True
        return False

    def snake_crashed(self):
        body = self.__snake.get_body()
        for i in range(1, self.__snake.get_length()):
            if self.is_collision(self.__snake.get_coordinates(), (body[0][i], body[1][i])):
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 40)
        score = font.render(f"Score: {self.__snake.get_length() - 1}", True, (0, 255, 0))
        self.__main_window.blit(score, (800, 10))
        pygame.display.flip()

    def start(self):
        while self.__running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.__running = False
                        continue
                    elif event.key == K_LEFT:
                        self.__snake.move_left()
                    elif event.key == K_RIGHT:
                        self.__snake.move_right()
                    elif event.key == K_DOWN:
                        self.__snake.move_down()
                    elif event.key == K_UP:
                        self.__snake.move_up()
                elif event.type == QUIT:
                    self.__running = False
                    continue

            if not self.__pause:
                self.play()
            time.sleep(0.09)

    def create_apple(self):
        x = random.randint(1,
                           (self.__main_window.get_width()) // self.__snake.get_block_size() - 1) \
            * self.__snake.get_block_size()
        y = random.randint(1,
                           (self.__main_window.get_height()) // self.__snake.get_block_size() - 1) \
            * self.__snake.get_block_size()
        print(x, ",", y)
        return Apple(self.__main_window, x, y)

    def disconnect_node(self, x, y):
        self.__graph.remove_node(x, y)
