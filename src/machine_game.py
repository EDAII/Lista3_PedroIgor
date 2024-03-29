import pygame
from pygame.locals import *
from src import result_screen
import time


def start(numbers, user_steps, machine_steps):

    median = machine_steps[-1]
    machine_palpites = []
    pygame.init()
    start_music = pygame.mixer.Sound("snd/start.wav")
    start_music.play(-1)

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


    dict = {}

    i = 0
    found = False
    for p in card_pos:
        dict[p] = numbers[i]
        i += 1

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
        select_sound = pygame.mixer.Sound("snd/button-25.wav")
        select_sound.play()
        pygame.display.update()
        if found:
            time.sleep(3)
            start_music.stop()
            result_screen.begin(len(machine_palpites), user_steps)
        time.sleep(3)
        screen.fill((0, 0, 0))

        for pos in card_pos:
            show = card_skin
            if dict[pos] in machine_palpites:
                if dict[pos] == median:
                    show = card_found
                    found = True
                elif dict[pos] < median:
                    show = card_skin_selected_less
                else:
                    show = card_skin_selected_more

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