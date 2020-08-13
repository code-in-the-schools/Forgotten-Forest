
import pygame
import os


win = pygame.display.set_mode((500,500))

class Character():
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Character.image = pygame.image.load("Character.png")
    self.image = Character.image
    self.image = pygame.transform.scale(self.image,(200,200))
#Character sprite   
    self.x = 50 
    self.y = 50
#Calls object to exist within the grid
  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))
#Will draw the sprite on the background
  def movement(self, width, height):
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN] == True:
      self.y += 3
    if key[pygame.K_UP] == True:
      self.y -= 3 
    if key[pygame.K_RIGHT] == True:
      self.x += 3
    if key[pygame.K_LEFT] == True:
      self.x -= 3
#Movement script
  def Gravity(self, height):
    if self.y < height - 50 and pygame.key.get_focused():
      self.y += 1
#Gives player gravity
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
        self.screen = Screen
        # Create
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height], 0)

pygame.display.set_caption('Test')
all_sprite_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

#player = Player(50, 50)
#player.walls = wall_list 

#all_sprite_list.add(player)


bigwall = Wall()


Sprite = Character()
pygame.init()
screen_width = 800
screen_height = 800
Screen = pygame.display.set_mode((screen_height,screen_width))
screen = (screen_width,screen_height)
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
  
  
  Screen.fill((255,255,255))
  Sprite.movement(screen_width,screen_height)
  Sprite.Gravity(screen_width)
  Sprite.draw(win)
  enemy.move(screen_width, screen_height)       
  enemy.draw(win)
  bigwall.draw(win) 
pygame.display.update()  
  
clock.tick(60)
#While loop to repeat continuously
