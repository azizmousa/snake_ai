import pygame


class Apple:
    def __init__(self, window, x=0, y=0, width=10, height=10, scale=1):
        self.__x = x
        self.__y = y
        self.__WIDTH = width
        self.__HEIGHT = height
        self.__window = window
        self.__scale = scale

    def get_coordinates(self):
        return self.__x, self.__y

    def draw(self):
        apple = pygame.Rect((self.__x*self.__scale, self.__y*self.__scale), (self.__WIDTH, self.__HEIGHT))
        pygame.draw.rect(self.__window, (255, 0, 0), apple)
        # pygame.display.update()


