from globs import *
from map_breadth_first import *
from map import *

win = pygame.display.set_mode((WIDTH+200, HEIGHT+50))
done = False
mouse_rect = pygame.Rect(-1, -1, 1, 1)
my_map = Map()
clock = pygame.time.Clock()

algo_type = "A-star"    # current algorithm type selected

while not done:
    #UPDATE
    deltaTime = clock.tick(20) / 1000.0
    #INPUT
    evt = pygame.event.poll()
    mouse_rect[0], mouse_rect[1] = pygame.mouse.get_pos()
    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True
        elif evt.key == pygame.K_SPACE and not my_map.path_found:
            if not my_map.use_breadth or not my_map.use_a_star: #only run if not running either alogrithm
                if algo_type == "A-star":
                    my_map.use_a_star = True
                else:
                    my_map.use_breadth = True
    elif evt.type == pygame.MOUSEBUTTONDOWN:
        if evt.button == 1:
            if mouse_rect.colliderect(reset_rect):
                my_map = Map()
            elif mouse_rect.colliderect(a_star_select_rect):
                algo_type = "A-star"
            elif mouse_rect.colliderect(breadth_select_rect):
                algo_type = "Breadth"
                for tile in my_map.map: # gets rid of all the barrier walls
                    tile.tile_cost = 0



    if algo_type == "A-star":
        mbuttons = pygame.mouse.get_pressed()
        if mbuttons[0]:
            for tile in my_map.map:
                if tile.tile_rect.colliderect(mouse_rect):
                    tile.tile_cost = 100000000
        if mbuttons[2]:
            for tile in my_map.map:
                if tile.tile_rect.colliderect(mouse_rect):
                    tile.tile_cost = 0

    #DRAW
    win.fill(GRAY)

    my_map.draw(win)
    # DRAWING CODE FOR ALL THE SIDE BAR ITEMS
    pygame.draw.rect(win, BLACK, reset_rect, 2)
    win.blit(reset_text, (reset_rect[0]+7, reset_rect[1]))

    if algo_type == "A-star":
        pygame.draw.rect(win, RED, a_star_select_rect, )
    else:
        pygame.draw.rect(win, RED, breadth_select_rect, )

    pygame.draw.rect(win, BLACK, a_star_select_rect, 2)
    win.blit(a_star_text, (a_star_select_rect[0] + a_star_select_rect[2]+5, a_star_select_rect[1]))

    pygame.draw.rect(win, BLACK, breadth_select_rect, 2)
    win.blit(breadth_text, (breadth_select_rect[0] + breadth_select_rect[2] + 5, breadth_select_rect[1]))

    win.blit(notetext, (0, HEIGHT+5))

    pygame.display.flip()

pygame.quit()
