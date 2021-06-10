import pygame
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    def __init__(self, window, width=10, height=10, length=1):
        self.__snakeX = [height] * length
        self.__snakeY = [height] * length
        self.__length = length
        self.__snakeWidth = width
        self.__snakeHeight = height
        self.__window = window
        self.__direction = Direction.RIGHT

    def draw(self):
        self.__window.fill((0, 0, 0))
        for i in range(self.__length):
            block = pygame.Rect((self.__snakeX[i], self.__snakeY[i]),
                                (self.__snakeWidth, self.__snakeHeight))
            pygame.draw.rect(self.__window, (255, 255, 255), block)
        pygame.display.flip()

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
        for i in range(self.__length-1, 0, -1):
            self.__snakeX[i] = self.__snakeX[i-1]
            self.__snakeY[i] = self.__snakeY[i-1]

        if self.__direction == Direction.LEFT:
            self.__snakeX[0] -= self.__snakeHeight
        elif self.__direction == Direction.RIGHT:
            self.__snakeX[0] += self.__snakeHeight
        elif self.__direction == Direction.UP:
            self.__snakeY[0] -= self.__snakeHeight
        elif self.__direction == Direction.DOWN:
            self.__snakeY[0] += self.__snakeHeight
        self.draw()

    def eat_apple(self):
        print("eat apple")
        self.__length += 1
