import pygame
from pygame.locals import *
from math import ceil
from src import numbers_gen
import copy
from src import find_median
from src import machine_game
import time
def start():
    pygame.init()

    screen_size = (705, 512)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Find the Median')

    w = 7
    h = 7
    card_pos = []
    # criando posições das cartas
    while w < 705:
        while h < 462:
            card_pos.append((w, h))
            h += 67
        h = 7
        w += 47
    # criando superfície das cartas
    card_skin = pygame.Surface((35, 50))
    card_skin.fill((150, 65, 200))
    card_skin_selected_less = pygame.Surface((35, 50))
    card_skin_selected_less.fill((255, 0, 0))
    card_skin_selected_more = pygame.Surface((35, 50))
    card_skin_selected_more.fill((0, 0, 255))
    card_found = pygame.Surface((35, 50))
    card_found.fill((35, 200, 35))

    tips_font = pygame.font.SysFont('bold', 50)
    tips_text = tips_font.render("", False, (255, 255, 255))

    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('bold', 18)
    mouse_position = ()
    card_selected = [()]

    dict = {}
    numbers = numbers_gen.numbers_gen()



    machine_result = find_median.find_median(numbers, ceil(len(numbers)/2), numbers)

    median = machine_result[-1]
    print(machine_result)
    print(median)
    found = False
    i = 0
    for p in card_pos:
        dict[p] = numbers[i]
        i += 1
    #machine_steps = min(binary_search_result, index_search_result)
    user_steps = 0
    result = ''
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = (pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
                if mouse_position[0] <= 462:
                    last = [screen_size[0], screen_size[1]]
                    card_selected_index = (ceil((mouse_position[0]) / 67) - 1, ceil((mouse_position[1]) / 47) - 1)
                    card_selected.append(card_pos[card_selected_index[1] * 7 + card_selected_index[0]])
                    user_steps += 1
        pygame.display.update()
        screen.fill((0, 0, 0))
        if found:
            machine_game.start(numbers, [], machine_result)
        """
        if result:
            result_screen.begin(result, machine_steps, user_steps)
        """
        for pos in card_pos:
            show = card_skin

            if pos in card_selected:

                if dict[pos] == median:
                    print('achou')
                    show = card_found
                    """
                    
                    screen.blit(show, pos)
                    if user_steps > machine_steps:
                        result = 'Você perdeu.'
                    elif user_steps < machine_steps:
                        # time.sleep(3)
                        result = ('Você ganhou.')
                    else:
                        result = ('Empatamos')
                    """

                elif dict[pos] < median:
                    show = card_skin_selected_less
                else:
                    show = card_skin_selected_more

            if card_selected!=[()]:
                if dict[card_selected[-1]] > median:
                    tips_text = tips_font.render("A mediana é menor que "+str(dict[card_selected[-1]]), False, (255, 255, 255))
                elif dict[card_selected[-1]] < median:
                    tips_text = tips_font.render("A mediana é maior que "+str(dict[card_selected[-1]]), False, (255, 255, 255))
                else:
                    tips_text = tips_font.render("Você encontrou a mediana: " + str(dict[card_selected[-1]]), False, (255, 255, 255))
                    found = True

            textsurface = myfont.render(str(dict[pos]), False, (255, 255, 255))
            screen.blit(tips_text, (50, 475))
            screen.blit(show, pos)
            screen.blit(textsurface, (pos[0], pos[1] + 18))