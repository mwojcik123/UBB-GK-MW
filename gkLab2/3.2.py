import pygame
import math

pygame.init()
width = 600
height = 600
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("ex 1 i 2")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)

win.fill(CZARNY)
r = 150
middle = (width // 2, height // 2)

def draw_angle(angle_degrees):
    size = 100
    center = (width // 2, height // 2)
    angle = 360 / angle_degrees
    points = []

    for i in range(angle_degrees):
        x = center[0] + size * math.cos(math.radians(i * angle))
        y = center[1] + size * math.sin(math.radians(i * angle))
        points.append((x, y))

    return pygame.draw.polygon(win, ZOLTY, points, 6)

def handle_key_event(event):
    win.fill(CZARNY)
    draw_angle(6)  # czternastokąt
    changed = None

    if event.key == pygame.K_1:
        changed = pygame.transform.scale(win, (int(width * 0.35), int(height * 0.35)))
    elif event.key == pygame.K_2:
        changed = pygame.transform.rotate(win, 45)
    elif event.key == pygame.K_3:
        changed = pygame.transform.flip(win, 0, 1)
    elif event.key == pygame.K_4:
        changed = pygame.transform.scale_by(win, (0.35, 1))
        changed = pygame.transform.rotozoom(changed, 45, 1)
    elif event.key == pygame.K_5:
        changed = pygame.transform.scale(win, (width, int(height * 0.35)))
    elif event.key == pygame.K_6:
        changed = pygame.transform.scale_by(win, (0.35, 1))
        changed = pygame.transform.rotozoom(changed, 180, 1)
    elif event.key == pygame.K_7:
        changed = pygame.transform.scale_by(win, (0.5, 1))
        changed = pygame.transform.flip(changed, 1, 0)
    elif event.key == pygame.K_8:
        changed = pygame.transform.scale_by(win, (1, 0.4))
        changed = pygame.transform.rotate(changed, -20)
    elif event.key == pygame.K_9:
        changed = pygame.transform.scale_by(win, (0.35, 1))
        changed = pygame.transform.rotozoom(changed, 90, 1)

    if changed:
        win.blit(changed, ((width - changed.get_width()) // 2, (height - changed.get_height()) // 2))
        pygame.display.flip()

def start():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                handle_key_event(event)

        pygame.display.update()

start()
