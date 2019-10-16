class node:
    def __init__(self, walkable, worldPosition, gridX, gridY):
        self.walkable = walkable
        self.worldPosition = worldPosition
        self.gridX = gridX
        self.gridY = gridY
        self.gCost = 0
        self.hCost = 0
        self.parent = 0
        self.fCost = self.gCost+self.hCost

    def getFCost(self):
        self.fCost = self.gCost + self.hCost
        return self.gCost+self.hCost


