import pygame
import os
import walls
import enemy
import player2

class Character():
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Character.image = pygame.image.load("Character.png")
    self.image = Character.image
    self.image = pygame.transform.scale(self.image,(150,100))
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

Sprite = Character()
pygame.init()
screen_width = 800
screen_height = 800
Screen = pygame.display.set_mode((screen_height,screen_width))
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
  Sprite.draw(Screen)

  pygame.display.update()
  
  clock.tick(60)
#While loop to repeat continuously