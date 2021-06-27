import pygame
from enum import Enum


class Direction(Enum):
    NONE = -1
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    def __init__(self, window, size=10, length=1):
        self.__snakeX = [0] * length
        self.__snakeY = [0] * length
        self.__length = length
        self.__blockSize = size
        self.__window = window
        self.__direction = Direction.NONE
        self.__prev_tail_pos = (self.__snakeX[-1], self.__snakeY[-1])

    def get_coordinates(self):
        return self.__snakeX[0]//self.__blockSize, self.__snakeY[0]//self.__blockSize

    def get_block_size(self):
        return self.__blockSize

    def draw(self):
        self.__window.fill((0, 0, 0))
        for i in range(self.__length):
            block = pygame.Rect((self.__snakeX[i], self.__snakeY[i]),
                                (self.__blockSize, self.__blockSize))
            if i == 0:
                pygame.draw.rect(self.__window, (0, 255, 0), block)
            else:
                pygame.draw.rect(self.__window, (0, 255, 0), block, 1)

    def move_left(self):
        if self.__direction != Direction.RIGHT:
            print("move left")
            self.__direction = Direction.LEFT
        else:
            self.opposite_direction()

    def move_right(self):
        if self.__direction != Direction.LEFT:
            print("move right")
            self.__direction = Direction.RIGHT
        else:
            self.opposite_direction()

    def move_up(self):
        if self.__direction != Direction.DOWN:
            print("move up")
            self.__direction = Direction.UP
        else:
            self.opposite_direction()

    def move_down(self):
        if self.__direction != Direction.UP:
            print("move down")
            self.__direction = Direction.DOWN
        else:
            self.opposite_direction()

    def opposite_direction(self):
        # pass
        if self.__direction == Direction.RIGHT or self.__direction == Direction.LEFT:
            if self.get_coordinates()[1] > self.__window.get_height()//2:
                self.__direction = Direction.UP
            else:
                self.__direction = Direction.DOWN
        else:
            if self.get_coordinates()[0] > self.__window.get_width()//2:
                self.__direction = Direction.LEFT
            else:
                self.__direction = Direction.RIGHT

    def walk(self):
        for i in range(self.__length-1, 0, -1):
            self.__snakeX[i] = self.__snakeX[i-1]
            self.__snakeY[i] = self.__snakeY[i-1]

        current_direction = self.__direction

        if current_direction == Direction.LEFT:
            self.__snakeX[0] -= self.__blockSize
        elif current_direction == Direction.RIGHT:
            self.__snakeX[0] += self.__blockSize
        elif current_direction == Direction.UP:
            self.__snakeY[0] -= self.__blockSize
        elif current_direction == Direction.DOWN:
            self.__snakeY[0] += self.__blockSize
        self.__prev_tail_pos = (self.__snakeX[-1] // self.__blockSize, self.__snakeY[-1]//self.__blockSize)
        self.draw()

    def eat_apple(self):
        print("eat apple")
        self.__length += 1
        self.__snakeX.append(1)
        self.__snakeY.append(1)

    def get_length(self):
        return self.__length

    def get_body(self):
        return self.__snakeX, self.__snakeY

    def get_previous_tail_position(self):
        return self.__prev_tail_pos

    def get_current_direction(self):
        return self.__direction

    def get_second_block(self):
        if self.__length > 1:
            return self.__snakeX[1]//self.__blockSize, self.__snakeY[1]//self.__blockSize
        else:
            return None
