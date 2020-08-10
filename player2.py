import pygame
import os
img_path = os.path.join('charcter2.png')
#Second player 
class player2(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    player2.image = pygame.image.load("character2.png")
    self.image = player2.image
    self.image = pygame.transform.scale(self.image,(200,400))

    self.x = 700
    self.y = 60
    self.hitbox = (self.x,self.y,25, 150)

  def draw(self, surface):
    surface.blit(self.image,(self.x,self.y))
#PLayer2 uses wasd
  def movementP2(self, width, height):
    if event.key == pygame.KEYDOWN:
      #
      if event.key == ord('s'):
        self.y += 3
      if event.key == ord('w'):
        self.y -= 3 
      if event.key == ord('d'):
        self.x += 3
      if event.key == ord('a'):
        self.x -= 3

sprite2 = player2()
running = True

pygame.init()
screen_width =800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

while running == True:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      running= False
    
  sprite2.movementP2()
  sprite2.draw(screen)
  pygame.display.update()
