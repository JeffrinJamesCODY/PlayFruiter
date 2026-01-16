import pygame
from logic import spin, START_CREDITS

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PlayFruiter")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

credits = START_CREDITS

reels = ["?","?","?"]

def draw_reels(reels):
    for i, symbol in enumerate(reels):
        text = font.render(symbol, True, (255, 255, 255))
        screen.blit(text, (200 + i * 110, 200))

spinning = False
spin_timer = 0
SPIN_DURATION = 60

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not spinning:
                spinning = True
                spin_timer = 0

if spinning:
    spin_timer = 1

    reels = ["?", "?", "?"]

    if spin_timer >= SPIN_DURATION:
        credits, reels, results, payout = spin(credits)
        spinning = False

credits_text = font.render(f"Credits: {credits}p", True, (255, 255, 0))
screen.blit(credits_text, (15, 15))

running = True

while running:
    clock.tick(60)
    screen.fill((20, 20, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not spinning:
                spinning = True
                spin_timer = 0

    if spinning:
        spin_timer += 1
        reels = ["?", "?", "?"]

        if spin_timer >= SPIN_DURATION:
            credits, reels, result, payout = spin(credits)
            spinning = False

    draw_reels(reels)

    credits_text = font.render(f"Credits: {credits}p", True, (255, 255, 0))
    screen.blit(credits_text, (20, 20))

    pygame.display.flip()

pygame.quit()
