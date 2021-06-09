import pygame


class Snake:
    def __init__(self, window, x=100, y=100, width=10, height=10):
        self.__snakeX = x
        self.__snakeY = y
        self.__snakeWidth = width
        self.__snakeHeight = height
        self.__window = window

    def draw_snake(self):
        snake = pygame.Rect((self.__snakeX, self.__snakeY), (self.__snakeWidth, self.__snakeHeight))
        pygame.draw.rect(self.__window, (255, 255, 255), snake)
        pygame.display.flip()

    def move_left(self):
        self.__window.fill((0, 0, 0))
        print("move left")
        self.__snakeX -= 10

    def move_right(self):
        self.__window.fill((0, 0, 0))
        print("move right")
        self.__snakeX += 10

    def move_up(self):
        self.__window.fill((0, 0, 0))
        print("move up")
        self.__snakeY -= 10

    def move_down(self):
        self.__window.fill((0, 0, 0))
        print("move down")
        self.__snakeY += 10

    def eat_apple(self):
        print("eat apple")
        self.__snakeWidth += 10
