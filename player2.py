import pygame
import os
#img_path = os.path.join('charcter2.png')
#Second player 
class player2():
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    player2.image = pygame.image.load("character2.png")
    self.image = player2.image
    self.image = pygame.transform.scale(self.image,(200,200))

    self.x = 50
    self.y = 50
    self.hitbox = (self.x,self.y,25, 150)

  def draw(self, surface):
    surface.blit(self.image,(self.x,self.y))
#PLayer2 uses wasd
  def movementP2(self, width, height):
    key = pygame.key.get_pressed()
    if key[pygame.K_s]:
      self.y += 3
    if key[pygame.K_w]:
      self.y -= 3 
    if key[pygame.K_d]:
      self.x += 3
    if key[pygame.K_a]:
      self.x -= 3
      
  def Gravity(self, height):
    if self.y < height - 50 and pygame.key.get_focused():
      self.y += 1

sprite2 = player2()
running = True

pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

while running == True:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      running= False
  screen.fill((255,255,255))
  sprite2.movementP2(screen_width, screen_height)
  sprite2.draw(screen)
  sprite2.Gravity(screen_width)
  pygame.display.update()
  clock.tick(60)

