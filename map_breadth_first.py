from globs import *
from tile_obj import *
import random


class Map():
    def __init__(self):
        self.map = []
        for row in range(ROWS):
            for col in range(COLS):
                self.map.append(Tile(col * TILEWIDTH, row * TILEHEIGHT, False, False, False, False, False))

        self.start_index = random.randint(0, ROWS * COLS - 1)
        self.end_index = random.randint(0, ROWS * COLS - 1)
        self.map[self.end_index].start_tile = True  # just use random.randint to give a random start
        self.map[self.start_index].end = True

        self.frontier = []
        self.priority = 0

        self.frontier.append([self.get_start(), self.priority])
        self.priority += 1
        self.came_from = {}
        self.came_from[self.get_start()] = None
        self.path = []
        self.path_found = False
        self.current = None
        self.finding_path = False

    def heuristic(self, a, b):
        # Manhattan distance on a square grid
        return abs(a.x - b.x) + abs(a.y - b.y)

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
        if len(self.frontier) > 0:
            for tile in self.frontier:
                if not tile[0].best_path:
                    tile[0].visited = False
                    tile[0].frontier = True

        if len(self.frontier) > 0 and self.finding_path:
            self.find_path(win)

        if self.path_found:
            self.current = self.get_end()
            while self.current != self.get_start():
                self.path.append(self.current)
                self.current = self.came_from[self.current]
            self.path.reverse()

        for tile in self.map:
            #tile.get_state()
            tile.draw(win)

    def find_path(self, win):

        # for i in range(1 ):
        #while len(self.frontier) > 0:  # while the frontier is still expanding
        self.frontier, self.current, priority = get(self.frontier, self.priority)

        if self.current == self.get_end():
            self.path_found = True
            self.finding_path = False
            return

        for next in self.getneighbors(self.current):
            if next not in self.came_from:
                self.frontier.append([next, priority])
                priority += 1
                self.came_from[next] = self.current





    def getneighbors(self, current_tile):
        neighbors = []
        index = self.map.index(current_tile)
        row_index = index % COLS
        # add/sub cols form index to get below/above row
        if row_index + 1 < COLS:
            neighbors.append(self.map[index + 1])
        if row_index - 1 > -1:
            neighbors.append(self.map[index - 1])
        if index - COLS > -1:
            neighbors.append(self.map[index - COLS])
        if index + COLS < len(self.map):
            neighbors.append(self.map[index + COLS])

        return neighbors



