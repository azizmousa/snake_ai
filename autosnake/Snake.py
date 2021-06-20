import pygame
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    def __init__(self, window, size=10, length=1):
        self.__snakeX = [size] * length
        self.__snakeY = [size] * length
        self.__length = length
        self.__blockSize = size
        self.__window = window
        self.__direction = [Direction.RIGHT]
        self.__prev_tail_pos = (self.__snakeX[-1], self.__snakeY[-1])

    def get_coordinates(self):
        return self.__snakeX[0], self.__snakeY[0]

    def get_block_size(self):
        return self.__blockSize

    def draw(self):
        self.__window.fill((0, 0, 0))
        for i in range(self.__length):
            block = pygame.Rect((self.__snakeX[i], self.__snakeY[i]),
                                (self.__blockSize, self.__blockSize))
            pygame.draw.rect(self.__window, (0, 255, 0), block, 2)
        # pygame.display.flip()

    def move_left(self):
        if self.__direction[len(self.__direction)-1] != Direction.RIGHT:
            print("move left")
            self.__direction.append(Direction.LEFT)

    def move_right(self):
        if self.__direction[len(self.__direction)-1] != Direction.LEFT:
            print("move right")
            self.__direction.append(Direction.RIGHT)

    def move_up(self):
        if self.__direction[len(self.__direction)-1] != Direction.DOWN:
            print("move up")
            self.__direction.append(Direction.UP)

    def move_down(self):
        if self.__direction[len(self.__direction)-1] != Direction.UP:
            print("move down")
            self.__direction.append(Direction.DOWN)

    def walk(self):
        for i in range(self.__length-1, 0, -1):
            self.__snakeX[i] = self.__snakeX[i-1]
            self.__snakeY[i] = self.__snakeY[i-1]
        current_direction = self.__direction[0]

        if current_direction == Direction.LEFT:
            self.__snakeX[0] -= self.__blockSize
        elif current_direction == Direction.RIGHT:
            self.__snakeX[0] += self.__blockSize
        elif current_direction == Direction.UP:
            self.__snakeY[0] -= self.__blockSize
        elif current_direction == Direction.DOWN:
            self.__snakeY[0] += self.__blockSize
        if len(self.__direction) > 1:
            del self.__direction[0]
        self.__prev_tail_pos = (self.__snakeX[-1], self.__snakeY[-1])
        self.draw()

    def eat_apple(self):
        print("eat apple")
        self.__length += 1
        self.__snakeX.append(self.__blockSize)
        self.__snakeY.append(self.__blockSize)

    def get_length(self):
        return self.__length

    def get_body(self):
        return self.__snakeX, self.__snakeY

    def get_previous_tail_position(self):
        return self.__prev_tail_pos
