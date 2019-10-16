class pathFinder:

    def __init__(self, grid):
        self.grid = grid

    def getNodeDistance(self, nodeA, nodeB):
        distX = abs(nodeA.gridX - nodeB.gridX)
        distY = abs(nodeA.gridY - nodeB.gridY)
        if distX > distY:
            return 14 * distY + 10 * (distX - distY)
        return 14 * distX + 10 * (distY - distX)

    def findPath(self, startNode, endNode):
        openSet = []
        closedSet = []
        openSet.append(startNode)
        while len(openSet) > 0:
            currentNode = openSet[0]
            for i in range(1, len(openSet)):
                if (openSet[i].getFCost() < currentNode.getFCost()) | (openSet[i].getFCost() == currentNode.getFCost()):
                    if openSet[i].hCost < currentNode.hCost:
                        currentNode = openSet[i]
            openSet.remove(currentNode)
            if currentNode not in closedSet:
                closedSet.append(currentNode)

            if currentNode == endNode:
                self.retracePath(startNode, endNode)
                return
            neighbours = self.grid.getNeighbours(currentNode)
            for neighbour in neighbours:
                if neighbour.walkable == 0 | (neighbour in closedSet):
                    continue
                updateCost = currentNode.gCost + self.getNodeDistance(currentNode, neighbour)
                if (updateCost < neighbour.gCost) | (neighbour not in openSet):
                    neighbour.gCost = updateCost
                    neighbour.hCost = self.getNodeDistance(neighbour, endNode)
                    neighbour.parent = currentNode

                    if neighbour not in openSet:
                        openSet.append(neighbour)

    def retracePath(self, startNode, endNode):
        path = []
        currentNode = endNode
        while currentNode != startNode:
            path.append(currentNode)
            currentNode = currentNode.parent
        path.reverse()
        self.grid.path = path
