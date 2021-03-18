import pygame
import sys

cards = pygame.image.load("E:\杂项\游戏\\cards.png")

def cal_cards(cards_num, kiss_num, score):
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('周周牌刮刮乐')
    font = pygame.font.SysFont('Times', 30)
    screen.blit(cards, (0, 0))
    for i in range(len(cards_num)):
        text = font.render(str(cards_num[i]), True, (0, 0, 0))
        screen.blit(text, (770, 10 + 50 * i))
    font_score = pygame.font.SysFont('Times', 40)
    text = font_score.render(str(kiss_num), True, (0, 0, 0))
    screen.blit(text, (350, 700))
    text = font_score.render(str(score), True, (0, 0, 0))
    screen.blit(text, (220, 755))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)

        pygame.display.update()

if __name__ == '__main__':
    cal_cards([1,1,1,1,1,1,1,1],0,0)