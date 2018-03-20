import pygame
import random
import os
from os import path

# initiating pygame & sound mixer
pygame.init()
pygame.mixer.init()

# Declaring global variables
WIDTH = 1000
HEIGHT = 600
FPS = 60
SPRITESHEET = "spritesheet.png"

# defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# creating the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Miguel Madness")

# setting the game clock
clock = pygame.time.Clock()

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# Load all the game graphics
background = pygame.image.load(path.join(img_folder, "background.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_folder, "stand_1.png")).convert()

# spritesheet utility class for loading and parsing spritesheet
class Spritesheet:
    def __innit__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = pygameSurace((width, height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        return image

# sprite for the Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        # this sets the image to load a certain image by using os to join and then convert
        self.image = self.game.spritesheet.get_image(19, 17, 10, 15)
        # this makes this object ignore certain colors
        self.image.set_colorkey((157, 142, 135))
        # automatically generates a collision/management rectangle for sprite
        self.rect = self.image.get_rect()
        # places the player at center of screen
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.speedx = 0

    # def load_iamges():
    #     self.standing_frames = [self.game.spritesheet.get_image()
    #                             self.game.spritesheet.get_image()
    #                             self.game.spritesheet.get_image()
    #                             self.game.spritesheet.get_image()]

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# sprite for the enemies
# class Mob(pygame.sprite.Sprite):
#     def __init__ (self):
#         pygame.sprite.Sprite.__init__(self)

# creating our sprite group
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# game loop
running = True
while running:
    # keep the clock running at the right speed
    clock.tick(FPS)

    # Process Input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Render
    screen.fill(WHITE)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
