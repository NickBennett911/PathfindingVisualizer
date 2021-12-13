from globs import *
from vector import *

class Tile():
    def __init__(self, x, y, frontier_tile, start_tile, visited_tile, end_tile, block_tile, tile_cost=0,):
        self.mPos = [x, y]
        self.tile_rect = pygame.Rect(x, y, TILEWIDTH, TILEHEIGHT)

        self.frontier = frontier_tile
        self.start_tile = start_tile
        self.visited = visited_tile
        self.end = end_tile
        self.barrier = block_tile
        self.best_path = False
        self.tile_cost = tile_cost

    def get_state(self):
        if self.frontier:
            print("frontier tile")
        elif self.start_tile:
            print("start tile")
        elif self.visited:
            print("visited tile")
        elif self.end:
            print("end tile")
        elif self.barrier:
            print("barrier tile")
        elif self.best_path:
            print("best path tile")

    def draw(self, win):
        if self.tile_cost <=0 and not self.start_tile and not self.frontier and not self.visited and not self.end and not self.barrier and not self.best_path:

            pygame.draw.rect(win, BLACK, self.tile_rect, 2)
        elif self.tile_cost > 0:
            pygame.draw.rect(win, BLACK, self.tile_rect, )
        elif self.start_tile:
            pygame.draw.rect(win, RED, self.tile_rect)
            pygame.draw.rect(win, BLACK, self.tile_rect, 2)
        elif self.end:
            pygame.draw.rect(win, GREEN, self.tile_rect)
            pygame.draw.rect(win, BLACK, self.tile_rect, 2)
        elif self.frontier:
            pygame.draw.rect(win, LIGHT_BLUE, self.tile_rect)
            pygame.draw.rect(win, BLACK, self.tile_rect, 2)
        elif self.visited:
            pygame.draw.rect(win, LIGHT_GRAY, self.tile_rect)
            pygame.draw.rect(win, BLACK, self.tile_rect, 2)
        elif self.best_path:
            pygame.draw.rect(win, BLUE, self.tile_rect)
            pygame.draw.rect(win, BLACK, self.tile_rect, 2)
