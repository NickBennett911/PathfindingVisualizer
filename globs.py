import pygame
pygame.init()

HEIGHT = 600
WIDTH = 800
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 0, 100)
TILEWIDTH = 40
TILEHEIGHT = 40
ROWS = int(HEIGHT / TILEHEIGHT)
COLS = int(WIDTH / TILEWIDTH)

textfont = pygame.font.SysFont("Times New Roman", 30)
smallfont = pygame.font.SysFont("Times New Roman", 25)
reset_text = textfont.render("Reset Board", True, BLACK)
reset_rect = pygame.Rect(WIDTH+20, 200, 160, 40)

a_star_select_rect = pygame.Rect(WIDTH+20, 280, 40, 40)
a_star_text = textfont.render("A-Star", True, BLACK)

breadth_select_rect = pygame.Rect(WIDTH+20, 340, 40, 40)
breadth_text = smallfont.render("Breadth First", True, BLACK)

notetext = smallfont.render("Notes: With A-Star selected you may draw barriers to path-find around/SPACE to run algorithm.", True, BLACK)

def get(array):             #pops the first element off the array and returns both within a tuple
    temp = array[0][0]
    del array[0]
    return (array, temp)