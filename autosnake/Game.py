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
        self.__snake = Snake(self.__main_window, length=1, size=10)
        self.__apple = self.create_apple()
        self.__snake.draw()
        self.__running = True
        self.__pause = False
        self.__graph = Graph(game_width, game_height, self.__snake.get_block_size())
        self.__graph.initiate_graph()
        print("Apple At:", self.__apple.get_coordinates())

    def play(self):
        self.__snake.walk()

        if self.snake_crashed():
            self.__pause = True
        # print(self.__graph.get_graph())

        self.__apple.draw()
        self.display_score()
        co = self.__snake.get_coordinates()
        prev = self.__snake.get_previous_tail_position()
        self.disconnect_node(co[0], co[1])
        self.__graph.insert_node(prev[0], prev[1])
        if self.is_collision(self.__snake.get_coordinates(), self.__apple.get_coordinates()):
            self.__snake.eat_apple()
            self.__apple = self.create_apple()
            print("Apple At:", self.__apple.get_coordinates())

    @staticmethod
    def is_collision(coord1, coord2):
        if coord2[0] == coord1[0]:
            if coord2[1] == coord1[1]:
                return True
        return False

    def snake_crashed(self):
        coord1 = self.__snake.get_coordinates()
        if coord1[0] >= self.__main_window.get_width()//self.__snake.get_block_size() \
                or coord1[1] >= self.__main_window.get_height()//self.__snake.get_block_size():
            return True
        if coord1[0] < 0 or coord1[1] < 0:
            return True
        body = self.__snake.get_body()
        for i in range(3, self.__snake.get_length()):
            if self.is_collision(self.__snake.get_coordinates(), (body[0][i]//self.__snake.get_block_size(),
                                                                  body[1][i]//self.__snake.get_block_size())):
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 40)
        score = font.render(f"Score: {self.__snake.get_length() - 1}", True, (255, 255, 255))
        self.__main_window.blit(score, score.get_rect())

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
            time.sleep(0.05)
            pygame.display.update()

    def create_apple(self):
        x = random.randint(1,
                           (self.__main_window.get_width()) // self.__snake.get_block_size() - 1)

        y = random.randint(1,
                           (self.__main_window.get_height()) // self.__snake.get_block_size() - 1)

        # print("Apple x,y:", x, ",", y)
        return Apple(self.__main_window, x, y, scale=self.__snake.get_block_size())

    def disconnect_node(self, x, y):
        self.__graph.remove_node(x, y)
