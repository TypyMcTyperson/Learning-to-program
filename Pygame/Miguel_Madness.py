import random
import pygame
from pygame.locals import *
from os import path

# Initializing Game
pygame.init()

# Initializing Music
pygame.mixer.init()

# Screen Settings
WIDTH = 800
HEIGHT = 600
DW_HALF = WIDTH / 2
DH_HALF = HEIGHT / 2
DISPLAY_AREA = WIDTH * HEIGHT
FPS = 60

# Initializing Screen
DS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Miguel Madness!')

# setting up resource directories
img_dir = path.join(path.dirname(__file__), 'img')
music_dir = path.join(path.dirname(__file__), 'music')
sound_dir = path.join(path.dirname(__file__), 'sound')

# Font Settings
pygame.font.init()
FONT = pygame.font.Font(None, 15)

# Color Settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# CLASSES-------------------------------------------------------------------------------CLASSES


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = meteor_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


# Load all game graphics
background = pygame.image.load(path.join(img_dir, "dragonbackground.jpg")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "flyingmiguel.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "meteor.jpg")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laser.png")).convert()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Clock Settings
clock = pygame.time.Clock()


# FUNCTIONS-----------------------------------------------------------------------------FUNCTIONS


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    clock.tick(FPS)


# MAIN LOOP--------------------------------------------------------------------------------MAIN

running = True
while running:
    # processes inputs
    event_handler()

    # Updates objects
    all_sprites.update()

    # check to see if player and mob collide
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    # check to see if a bullet hit a mob
    hit = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # draws and renders objects
    DS.fill(BLACK)
    DS.blit(background, background_rect)
    all_sprites.draw(DS)
    pygame.display.update()
