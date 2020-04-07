#!/usr/bin/env python3
class Solution:
    def findConnectedColor(self,grids):
        seen = {}
        maxCount = 0
        for i in range(0, len(grids)):
            for j in range(0,len(grids[i])):
                maxCount = max(maxCount,self.__checkGrid(grids, i, j, seen))
        return maxCount

    def __checkGrid(self, grids, i, j, seen):
        color = grids[i][j]
        stack = []
        sum = 0
        stack.append([i,j])
        while (len(stack) > 0):
            point = stack.pop()
            x = point[0]
            y = point[1]
            key = '{:d}, {:d}'.format(x, y)
            if (seen.get(key) != None): 
                continue
            seen[key] = True
            sum = sum + 1
            points = self.__getNeighbours(grids, x, y)
            print(sum, points)
            for p in points:
                x = p[0]
                y = p[1]
                if color == grid[x][y]:
                  stack.append([x,y])
        return sum

    def __getNeighbours(self, grids, x, y):
        points = [[0,1], [0,-1],[1,0],[-1,0]]
        neighbours = []
        gridsWidth = len(grids)
        for point in points:
            posX  = point[0] + x
            posY  = point[1] + y
            if posX >= 0 and posY >= 0 and posX < gridsWidth and posY < gridsWidth:
                neighbours.append([posX, posY])
        return neighbours

grid = [
['r', 'g', 'b'],
['r', 'r', 'r'],
['g', 'g', 'r']
]
print(grid)
print(Solution().findConnectedColor(grid))