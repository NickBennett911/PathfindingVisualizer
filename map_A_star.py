

from globs import *
from tile_obj2 import *
import random
import queue

class Map():
    def __init__(self):
        self.map = []
        for row in range(ROWS):
            for col in range(COLS):
                self.map.append(Tile(col*TILEWIDTH, row*TILEHEIGHT, False, False, False, False, False))


        self.start_index = random.randint(0, ROWS*COLS-1)
        self.end_index = random.randint(0, ROWS*COLS-1)
        self.map[self.end_index].start_tile = True  # just use random.randint to give a random start
        self.map[self.start_index].end = True

        self.frontier = queue.PriorityQueue()
        self.frontierlist = [[self.get_start(), 0]]
        self.frontier.put((0, self.get_start().mPos))
        self.came_from = {}
        self.cost_so_far = {}
        self.cost_so_far[self.get_start()] = 0
        self.came_from[self.get_start()] = None
        self.path = []
        self.path_found = False
        self.current = None
        self.finding_path = False

    def heuristic(self, a, b):
        # Manhattan distance on a square grid
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_start(self):
        return self.map[self.start_index]

    def get_end(self):
        return self.map[self.end_index]

    def draw(self, win):
        for tile in self.path:
            tile.best_path = True
            tile.visited = False
            tile.frontier = False
        for tile in self.came_from:
            if not tile.best_path:
                tile.visited = True
                tile.frontier = False
        if len(self.frontierlist) > 0:
            for tile in self.frontierlist:
                if not tile[0].best_path:
                    tile[0].visited = False
                    tile[0].frontier = True

        if not self.frontier.empty() and self.finding_path:
            self.find_path(win)

        if self.path_found:
            self.current = self.get_end()
            while self.current != self.get_start():
                self.path.append(self.current)
                self.current = self.came_from[self.current]

        for tile in self.map:
            #tile.get_state()
            tile.draw(win)

    def find_path(self, win):

        #for i in range(1 ):
        #while not self.frontier.empty():   #while the frontier is still expanding
        self.current = self.frontier.get()
        for tile in self.map:
            if self.current[1] == tile.mPos:
                self.current = tile
                break

        for tile in self.frontierlist:
            if tile[0] == self.current:
                print(tile[1])
                self.frontierlist.remove(tile)

        if self.current == self.get_end():
            self.path_found = True
            self.finding_path = False
            return

        for next in self.getneighbors(self.current):
            new_cost = self.cost_so_far[self.current] + next.tile_cost
            if next not in self.came_from or new_cost < self.cost_so_far[next]:
                self.cost_so_far[next] = new_cost
                priority = new_cost + self.heuristic(self.get_end().mPos, next.mPos)
                self.frontier.put((priority, next.mPos))
                self.frontierlist.append([next, priority])
                self.came_from[next] = self.current


    def getneighbors(self, current_tile):
        neighbors = []
        index = self.map.index(current_tile)
        row_index = index%COLS
        # add/sub cols form index to get below/above row
        if row_index + 1 < COLS:
            neighbors.append(self.map[index+1])
        if row_index - 1 > -1:
            neighbors.append(self.map[index-1])
        if index - COLS > -1:
            neighbors.append(self.map[index - COLS])
        if index + COLS < len(self.map):
            neighbors.append(self.map[index + COLS])

        return neighbors