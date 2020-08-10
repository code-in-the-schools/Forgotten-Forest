import pygame
class Enemy():

  win = pygame.display.set.mode((500,600))
pygame.display.set__caption("First game")
walkright = [pygame.image('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image'),pygame.image.load('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image')]
walkLeft = [pygame.image.load('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image'), pygame.image.load('enemy.image')]
char = pygame.image.load('Standing.png')
clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = True
        self.right = True
        self.walkCount = 0
        self.standing = True
        if not(self.standing):
            if self.left:
                 win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                 
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))



                class projectile(object):
      def __init__(self,x,y,radius,color,facing):
          self.x = x
          self.y = y
          self.radius = radius
          self.color = color
          self.facing = facing
        





