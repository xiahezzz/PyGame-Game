import pygame
from pygame.locals import *
import os
import random
import sys
import CalCards

SCREENSIZE = (500, 500)
IMAGEDIR = 'E:\杂项\IMAGEDIR'
SUPPORTEXTS = ['png', 'jpg']
GRAY = (192, 192, 192)
WHITE = (255, 255, 255, 27)

is_end = False
card_names = ['亲亲', '抱抱', '爱爱', '哄哄', '闹闹', '听话', '恐怖', '心愿']
finished_card = [0, 0, 0, 0, 0, 0, 0, 0]    #亲亲，抱抱，爱爱，哄哄，闹闹，听话，恐怖

def read_image_randomly():
    file_names = os.listdir(IMAGEDIR)
    file_names = [f for f in file_names if f.split('.')[-1] in SUPPORTEXTS]
    image_path = os.path.join(IMAGEDIR, random.choice(file_names))
    return [pygame.transform.scale(pygame.image.load(image_path), SCREENSIZE), image_path[-6:-4]]

def lucky_card(reward_num, kiss_num, score):
    global is_end, finished_card
    pygame.init()
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption('周周牌刮刮乐')
    surface = pygame.Surface(SCREENSIZE).convert_alpha()
    surface.fill(GRAY)
    image_used = read_image_randomly()
    screen.blit(image_used[0], (0, 0))
    screen.blit(surface, (0, 0))
    while reward_num > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)
            if event.type == KEYDOWN:
                if event.key == K_o:
                    reward_num -= 1
                    for i in range(len(card_names)):
                        if image_used[1] == card_names[i]:
                            finished_card[i] += 1
                            break
                    image_used = read_image_randomly()
                    surface.fill(GRAY)

        mouse_event_flags = pygame.mouse.get_pressed()
        if mouse_event_flags[0]:
            pygame.draw.circle(surface, WHITE, pygame.mouse.get_pos(), 40)
        screen.blit(image_used[0], (0, 0))
        screen.blit(surface, (0, 0))
        pygame.display.update()

    while reward_num == 0:
        CalCards.cal_cards(finished_card, kiss_num, score)

if __name__ == '__main__':
    lucky_card(6, 0, 0)


