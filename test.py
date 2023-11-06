
import pygame
 
 
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
 
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()
 
 
def on_click():
    color = (255, 0, 0) if sprite.image.get_at(
        (0, 0)) != (255, 0, 0) else (0, 255, 0)
    sprite.image.fill(color)
 
 
pygame.init()
screen = pygame.display.set_mode((400, 300))
 
sprite = ClickableSprite(pygame.Surface((100, 100)), 50, 50, on_click)
group = pygame.sprite.GroupSingle(sprite)
 
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
 
    group.update(events)
    screen.fill((255, 255, 255))
    group.draw(screen)
    pygame.display.update()
 
pygame.quit()
