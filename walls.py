import pygame


BLUE= ((0, 255, 255))

class Wall(object):
  def __init__(self):
    super().__init__()
    
    self.rect = pygame.image.load("brickwall.png")
    self.rect.y = 0
    self.rect.x = 0

  def draw(self,surface, x, y, width, height):
    self.image = pygame.transform.scale(self.image,(width, height))
    self.rect.y = y
    self.rect.x = x
    surface.blit(self.image, (self.rect.x, self.rect.y))

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Test')
all_sprite_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

wall = Wall(0,0,0,0)
wall_list.add(wall)
all_sprite_list.add(wall)

#player = Player(50, 50)
#player.walls = wall_list 

#all_sprite_list.add(player)

clock = pygame.time.Clock()

done = False

