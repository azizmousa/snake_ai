import pygame
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    def __init__(self, window, x=100, y=100, width=10, height=10):
        self.__snakeX = x
        self.__snakeY = y
        self.__snakeWidth = width
        self.__snakeHeight = height
        self.__window = window
        self.__direction = Direction.RIGHT

    def draw(self):
        self.__window.fill((0, 0, 0))
        snake = pygame.Rect((self.__snakeX, self.__snakeY), (self.__snakeWidth, self.__snakeHeight))
        pygame.draw.rect(self.__window, (255, 255, 255), snake)
        pygame.display.update()

    def move_left(self):
        if self.__direction != Direction.RIGHT:
            print("move left")
            self.__direction = Direction.LEFT

    def move_right(self):
        if self.__direction != Direction.LEFT:
            print("move right")
            self.__direction = Direction.RIGHT

    def move_up(self):
        if self.__direction != Direction.DOWN:
            print("move up")
            self.__direction = Direction.UP

    def move_down(self):
        if self.__direction != Direction.UP:
            print("move down")
            self.__direction = Direction.DOWN

    def walk(self):
        if self.__direction == Direction.LEFT:
            self.__snakeX -= 10
        elif self.__direction == Direction.RIGHT:
            self.__snakeX += 10
        elif self.__direction == Direction.UP:
            self.__snakeY -= 10
        elif self.__direction == Direction.DOWN:
            self.__snakeY += 10
        self.draw()

    def eat_apple(self):
        print("eat apple")
        self.__snakeWidth += 10
