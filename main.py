import pygame
import pathFinder
import grid

from pygame.locals import *

FPS = 144
WIN_WIDTH = 1500
WIN_HEIGHT = 1000
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (75, 0, 130)
MAG = (255, 0, 255)
pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
Grid = grid.grid(10, WIN_WIDTH, WIN_HEIGHT, sc)
path = pathFinder.pathFinder(Grid)
flag = 1
startNode = 0
endNode = 0
while 1:
    sc.fill(WHITE)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN & i.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] == 1:
                Grid.setObsticle(pygame.mouse.get_pos())
            elif pygame.mouse.get_pressed()[2] == 1:
                Grid.setNode(pygame.mouse.get_pos())
        if (i.type == pygame.MOUSEBUTTONDOWN) | (i.type == pygame.KEYDOWN):
            if (pygame.mouse.get_pressed()[1] == 1) | (pygame.key.get_pressed()[K_SPACE]):
                if flag == 1:
                    startNode = Grid.getNode(pygame.mouse.get_pos())
                    flag = ~flag
                else:
                    endNode = Grid.getNode(pygame.mouse.get_pos())
                    flag = ~flag

    Grid.drawNodes()
    if startNode != 0:
        Grid.drawNodeDifColor(startNode, GREEN)
        Grid.getNeighbours(startNode)
    if endNode != 0:
        Grid.drawNodeDifColor(endNode, BLUE)

    pygame.display.update()
    if endNode != 0:
        path.findPath(startNode, endNode)
    clock.tick(FPS)
