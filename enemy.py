import pygame
import os
 
win = pygame.display.set_mode((500,500))#screen

class enemy(object):
  walkRight = [pygame.image.load('enemy.png')]
  walkLeft = [pygame.image.load('enemy.png')]
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    enemy.image = pygame.image.load("enemy.png")
    self.image = enemy.image
    self.image = pygame.transform.scale(self.image,(200,200))
  def __init__(self, x, y, width, height, end):
      self.x = 50
      self.y = 50
      self.width = 500
      self.height = 500
      self.path = [x, end]
      #self.walkCount = 0
      self.vel = 3

#def draw####
  def draw(self, surface):
    self.move(self.width, self.height)
             
  def move(self, width, height):
    if self.vel > 0:
      if self.x < self.path[1] + self.vel:
        self.x += self.vel
      else:
        self.vel = self.vel * -1
        self.x += self.vel
        #self.walkCount = 0
    else:
      if self.x > self.path[0] - self.vel:
        self.x += self.vel
      else:
        self.vel = self.vel * -1
        self.x += self.vel
        #self.walkCount = 0

pygame.init()
enemy = enemy(100, 410, 64, 64, 300)
clock = pygame.time.Clock()
screen_width = 500
screen_height = 500
running = True
Screen = pygame.display.set_mode((screen_height,screen_width))

while running: #
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      running = False

  win.fill((255,255,255))
  enemy.draw(win)
  pygame.display.update()
  enemy.move(screen_width, screen_height)

  clock.tick(60)
  