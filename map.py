

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

        self.frontier = queue.PriorityQueue()           #priority queue data struct for the frontier
        self.frontierlist = [[self.get_start(), 0]]     #list version of my priority queue to use for drawing
        self.frontier.put((0, self.get_start().mPos))   #insert the start first with priority of 0
        self.came_from = {}                     # dictionary that holds where did the tiles come from
        self.cost_so_far = {}           # dictionary that shows that tiles cost as of so far
        self.cost_so_far[self.get_start()] = 0
        self.came_from[self.get_start()] = None
        self.path = []      # list that will end up holding the best path
        self.path_found = False     # bool to determine if the path is found
        self.current = None         # the current tile
        # bools to determine if supposed to be using an algorithm
        self.use_a_star = False
        self.use_breadth = False

        # attributes used for the breadth first search
        self.priority = 0

        self.breadth_frontier = []
        self.priority = 0

        self.breadth_frontier.append([self.get_start(), self.priority])
        self.priority += 1

    def heuristic(self, a, b):
        # Manhattan distance on a square grid between points a and b
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_start(self):
        """
        returns the start tile
        :return:
        """
        return self.map[self.start_index]

    def get_end(self):
        """
        returns the end tile
        :return:
        """
        return self.map[self.end_index]

    def draw(self, win):
        # this sets up which tiles should need to be colored a certain way to show them as a frontier tile or visited tile
        if self.use_breadth or self.use_a_star: # only if using an algorithm
            for tile in self.came_from:     # if tile in came from them it gets made into visited tile
                if not tile.best_path and not tile.visited: # dont bother continuing if already visited
                    tile.visited = True
                    tile.frontier = False
            if len(self.frontierlist) > 0:
                for tile in self.frontierlist:  # if tile in frontier then it is a frontier. Note the order of doing
                                                # came from first then frontier
                    if not tile[0].best_path:
                        tile[0].visited = False
                        tile[0].frontier = True

        if not self.frontier.empty() and self.use_a_star:   #using the a star alog method
            self.A_star_algo()

        if len(self.frontierlist) > 0 and self.use_breadth: # using the breadth first algo method
            self.breadth_first_algo()

        for tile in self.map:
            tile.draw(win)

    def A_star_algo(self):
        """ Method respobsible for being called each frame when breadth a star is being used"""
        # frontier is a Priority queue so get gives the item with the current highest priority
        self.current = self.frontier.get()
        # Go through and set our self.current to our actual current tile object
        for tile in self.map:       
            if self.current[1] == tile.mPos:
                self.current = tile
                break

        # removes that same tile from the frontier list so frontier and frontier list match
        for tile in self.frontierlist:
            if tile[0] == self.current:
                self.frontierlist.remove(tile)

        # iterates through all the neighbors to the current tile
        for next in self.getneighbors(self.current):
            # cost represents the cost so far plus what it will take to move to the next tile
            # if next in came from dont continue unless that cost is the best option for the next tile
            new_cost = self.cost_so_far[self.current] + next.tile_cost  
            if next not in self.came_from or new_cost < self.cost_so_far[next]:
                self.cost_so_far[next] = new_cost
                # determins priority of next tile with the cost plus the distance to the end
                # this is the heart of A-star since it will take distance to end into account
                priority = new_cost + self.heuristic(self.get_end().mPos, next.mPos)
                self.frontier.put((priority, next.mPos))
                self.frontierlist.append([next, priority])
                self.came_from[next] = self.current

        # determines if at the end
        if self.current == self.get_end():
            self.path_found = True
            self.use_a_star = False
            self.construct_path()
            return

    def breadth_first_algo(self):
        """ Method responsible for being called each frame when breadth first is being used"""
        # using my own get function it gets the current tile that will be looked at this frame
        self.frontierlist, self.current = get(self.frontierlist)
        # testing if it has already found the end tile, if so no need to go on
        if self.current == self.get_end():
            self.path_found = True
            self.use_breadth = False
            self.construct_path()
            return
        
        # uses my get neighbors to find all the current adjacent neighbors of the current tile
        for next in self.getneighbors(self.current):
            # only continue if the neighbor tile hasnt already been visited
            if next not in self.came_from:
                self.frontierlist.append([next])  #put the tile in the frontier list to be draw
                self.came_from[next] = self.current # put next in camefrom dict as key with it pointing to the current tile

    def construct_path(self):
        """uses came from dict to construct the path used to get there"""
        self.current = self.get_end()   # start from the end tile
        while self.current != self.get_start():
            self.path.append(self.current)
            self.current = self.came_from[self.current] #reverse engineers the path using the keys in camefrom dict

        for tile in self.path:      # adjust the tile types of all tiles in self.path
            tile.best_path = True
            tile.visited = False
            tile.frontier = False

    def getneighbors(self, current_tile):
        """
        finds neighbors of the given tile
        :param current_tile: tile being checked for neighbors
        :return: all tiles adjacent to current tile as long as they are on screen
        """
        neighbors = []
        index = self.map.index(current_tile)    # the current index of tile in self.map
        row_index = index%COLS                  # the current index pertaining to the row the current tile is in
        # add/sub cols form index to get below/above row
        if row_index + 1 < COLS:        # if right is on grid then add to neighbors
            neighbors.append(self.map[index+1])
        if row_index - 1 > -1:          # if left is on grid then add to neighbors
            neighbors.append(self.map[index-1])
        if index - COLS > -1:           # if upobe tile is on grid then add to neighbors
            neighbors.append(self.map[index - COLS])
        if index + COLS < len(self.map):    # if below is on grid then add to the neighbors
            neighbors.append(self.map[index + COLS])

        return neighbors