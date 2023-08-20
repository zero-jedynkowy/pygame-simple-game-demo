import pygame

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Simple game demo!")

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/background.png").convert()
        self.image = pygame.transform.scale(self.image, (800, 800))
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.step = 5
        self.viewKeys = ["left", "right", "front", "back"]
        self.view = {a:pygame.image.load("img/{}.png".format(a)).convert() for a in self.viewKeys}
        self.view = {a:pygame.transform.scale(self.view[a], (75, 75)).convert() for a in self.viewKeys}
        self.image = self.view["front"]
        self.rect = self.image.get_rect()

    def update(self, side):
        if side == "left":
            self.image = self.view[side]
            self.rect.centerx -= self.step
        if side == "right":
            self.image = self.view[side]
            self.rect.centerx += self.step
        if side == "front":
            self.image = self.view["back"]
            self.rect.centery -= self.step
        if side == "back":
            self.image = self.view["front"]
            self.rect.centery += self.step

player = Player()
background = Background()
board = pygame.sprite.RenderPlain()

board.add(background)
board.add(player)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.update("front")
    if keys[pygame.K_a]:
        player.update("left")
    if keys[pygame.K_s]:
        player.update("back")
    if keys[pygame.K_d]:
        player.update("right")
    board.draw(screen)
    pygame.display.flip()
