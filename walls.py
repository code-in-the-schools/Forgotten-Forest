import pygame
import os

win = pygame.display.set_mode((500,500))

BLUE= ((0, 255, 255))

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        # Init.
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.height = screen_height
        self.width = screen_width
        self.color = BLUE
        self.screen = screen
        # Create
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height], 0)

pygame.init()

screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Test')
all_sprite_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

#player = Player(50, 50)
#player.walls = wall_list 

#all_sprite_list.add(player)

clock = pygame.time.Clock()
Sprite = Wall()
done = False

running = True
while running:
  for event in pygame.event.get():
    if event.type ==  pygame.QUIT:
      pygame.quit()
      running = False
  Sprite.draw(win)
  pygame.display.update()
  win.fill((480,480,500))

