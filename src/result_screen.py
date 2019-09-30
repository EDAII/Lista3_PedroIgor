import pygame
import time
from src import start_game
from pygame.locals import *

def begin(machine_palpites, user_palpites):
    time.sleep(1)
    screen_size = (500, 150)
    screen = pygame.display.set_mode(screen_size)
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    my_font = pygame.font.SysFont('bold', 80)
    result_font = pygame.font.SysFont('bold', 22)
    steps_font = pygame.font.SysFont('bold', 50)

    start_button_skin = pygame.Surface((100, 35))
    start_button_skin.fill((255, 255, 255))
    start_count = 0
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 286 and pygame.mouse.get_pos()[1]>=124:
                    if pygame.mouse.get_pos()[0] <= 384 and pygame.mouse.get_pos()[1]<=146:
                        start_game.start()
        pygame.display.update()
        screen.fill((150, 65, 200))
        if machine_palpites == 1:
            text2_surface = steps_font.render('Encontrei em ' + str(machine_palpites) + ' palpite,', False, (255, 255, 255))
        else:
            text2_surface = steps_font.render('Encontrei em ' + str(machine_palpites) + ' palpites,', False, (255, 255, 255))
        text3_surface = steps_font.render('você encontrou em ' + str(user_palpites) + '.', False, (255, 255, 255))
        screen.blit(text2_surface, (30, 20))
        screen.blit(text3_surface, (30, 65))
        start_text_surface = result_font.render("PLAY AGAIN", False, (255, 0, 0))
        screen.blit(start_button_skin, (286, 125))

        if start_count > 100:
            screen.blit(start_text_surface, (290, 130))
        if start_count > 200:
            start_count = 0
        start_count+=1

        clock.tick(120)