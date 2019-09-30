import pygame
from pygame.locals import *
from math import ceil
from src import numbers_gen
from src import find_median
import time


def start(numbers, user_steps, machine_steps):

    median = machine_steps[-1]
    machine_palpites = []
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
    card_skin_selected = pygame.Surface((35, 50))
    card_skin_selected.fill((0, 0, 255))
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

    i = 0
    for p in card_pos:
        dict[p] = numbers[i]
        i += 1
    # machine_steps = min(binary_search_result, index_search_result)
    user_steps = 0
    result = ''
    print('machine')
    print(machine_steps)
    while True:
        if machine_palpites == []:
            tips_text = tips_font.render("Minha vez..", False, (255, 255, 255))
            screen.blit(tips_text, (235, 250))

        if machine_steps!=[]:
            machine_palpites.append(machine_steps[0])
            machine_steps = machine_steps[1:]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        time.sleep(3)
        screen.fill((0, 0, 0))
        """
        if result:
            result_screen.begin(result, machine_steps, user_steps)
        """
        for pos in card_pos:
            show = card_skin
            if dict[pos] in machine_palpites:
                if dict[pos] == median:
                    print('achou')
                    show = card_found
                else:
                    show = card_skin_selected

            if machine_palpites[-1] > median:
                tips_text = tips_font.render("A mediana é menor que " + str(machine_palpites[-1]), False, (255, 255, 255))
            elif machine_palpites[-1] < median:
                tips_text = tips_font.render("A mediana é maior que " + str(machine_palpites[-1]), False, (255, 255, 255))
            else:
                tips_text = tips_font.render("Encontrei a mediana: " + str(machine_palpites[-1]), False, (255, 255, 255))

            textsurface = myfont.render(str(dict[pos]), False, (255, 255, 255))
            screen.blit(show, pos)
            screen.blit(tips_text, (50, 475))
            screen.blit(textsurface, (pos[0], pos[1] + 18))