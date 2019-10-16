import node
import pygame


class grid:
    ORANGE = (255, 150, 100)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, nodeRadius, gridWorldSizeX, gridWorldSizeY, sc):
        self.nodeRadius = nodeRadius
        self.gridWorldSizeX = gridWorldSizeX
        self.gridWorldSizeY = gridWorldSizeY
        self.gridSizeX = round(gridWorldSizeX / (2 * nodeRadius))
        self.gridSizeY = round(gridWorldSizeY / (2 * nodeRadius))
        self.gridArr = [[0] * self.gridSizeY for i in range(self.gridSizeX)]
        self.sc = sc
        self.path = []
        self.createGrid()
        self.drawNodes()

    def createGrid(self):
        for i in range(0, self.gridSizeX):
            for j in range(0, self.gridSizeY):
                walkable = 1
                worldPosition = [i * self.nodeRadius * 2 + self.nodeRadius, j * self.nodeRadius * 2 + self.nodeRadius]
                self.gridArr[i][j] = node.node(walkable, worldPosition, i, j)

    def drawNodes(self):
        for i in range(0, self.gridSizeX):
            for j in range(0, self.gridSizeY):
                if self.gridArr[i][j].walkable == 1:
                    pygame.draw.circle(self.sc, self.WHITE,
                                       (self.gridArr[i][j].worldPosition[0],
                                        self.gridArr[i][j].worldPosition[1]),
                                       self.nodeRadius)
                    if len(self.path) != 0:
                        if self.gridArr[i][j] in self.path:
                            pygame.draw.circle(self.sc, self.RED,
                                               (self.gridArr[i][j].worldPosition[0],
                                                self.gridArr[i][j].worldPosition[1]),
                                               self.nodeRadius)
                else:
                    pygame.draw.circle(self.sc, self.BLACK,
                                       (self.gridArr[i][j].worldPosition[0],
                                        self.gridArr[i][j].worldPosition[1]),
                                       self.nodeRadius)

    def getNode(self, position):
        percentX = position[0] / self.gridWorldSizeX
        percentY = position[1] / self.gridWorldSizeY
        x = int(percentX * self.gridSizeX)
        y = int(percentY * self.gridSizeY)
        return self.gridArr[x][y]

    def setObsticle(self, position):
        n = self.getNode(position)
        n.walkable = 0

    def setNode(self, position):
        n = self.getNode(position)
        n.walkable = 1

    def getNeighbours(self, n):
        listOfNeighbours = []
        currentX = n.gridX
        currentY = n.gridY
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0) | (j != 0):
                    checkX = currentX + i
                    checkY = currentY + j
                    if (checkX >= 0) & (checkX <= self.gridSizeX-1) & (checkY >= 0) & (checkY <= self.gridSizeY-1):
                        listOfNeighbours.append(self.gridArr[currentX + i][currentY + j])
        return listOfNeighbours

    def drawNodeDifColor(self, n, color):
        pygame.draw.circle(self.sc, color,
                           (n.worldPosition[0],
                            n.worldPosition[1]),
                           self.nodeRadius)
