import pygame
class Wall(pygame.sprite.Sprite):
 def __init__(self, x, y, width, height):
   super().__init__()
   self.image = pygame.Surface([width, height])
   self.image.fill(BLUE)
   self.rect = self.image.get_rect()
   self.rect.y = y
   self.rect.x = x

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Test')
all_sprite_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 0, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

player = Player(50, 50)
player.walls = wall_list 

all_sprite_list.add(player)

clock = pygame.time.Clock()

done = False

