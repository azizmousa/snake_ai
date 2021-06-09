import pygame
from pygame.locals import *
from Snake import Snake
from Apple import Apple
import time


class Game:
    def __init__(self):
        pygame.init()
        self.__main_window = pygame.display.set_mode((1000, 500))
        self.__snake = Snake(self.__main_window)
        self.__apple = Apple(self.__main_window)
        self.__snake.draw()

    def start(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
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
                    running = False
                    continue

            self.__snake.walk()
            self.__apple.draw()
            time.sleep(0.1)
