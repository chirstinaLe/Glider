import pygame
import random

pygame.init()

xPosGlider = 10
yPosGlider = 10

gliderDown = True
horizontalGlider = "right"

gliderImg = pygame.image.load('gliderright.png')
testerImg = pygame.image.load('gliderleft.png')


#colors
black = (0, 0, 0)
white = (255, 255, 255)
beige = (225, 198, 153)
lightBlue = (215, 229, 240)
darkerBlue = (156, 195, 226)
darkBeige = (148, 107, 69)
green = (52,231,24)

colorSRect = (225, 198, 153)

#fonts
fontOne = pygame.font.Font('freesansbold.ttf', 18)
smallerFont = pygame.font.Font('freesansbold.ttf', 14)

# Screen
x = 600
y = 400
size = (x, y)
screen = pygame.display.set_mode(size) 

# Loop
start = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# start screen
while not start:

  screen.fill(white)

  # text

  startText = fontOne.render("   Start! (hover over button)", True, black)
  startRect = pygame.draw.rect(screen, colorSRect, [150, 150, 250, 40])
  screen.blit(startText, startRect)

  instText = smallerFont.render("      dark blue areas are updrafts", True, black)
  instRect = pygame.draw.rect(screen, beige, [150, 250, 250, 20])
  screen.blit(instText, instRect)
  instrText = smallerFont.render("          don't touch the ground!", True, black)
  instrRect = pygame.draw.rect(screen, beige, [150, 270, 250, 20])
  screen.blit(instrText, instrRect)

 # mouse position + pressing detection
  for event in pygame.event.get():
    mouse = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if startRect.collidepoint(pos[0], pos[1]):
      colorSRect = darkBeige
      start = True
    else:
      colorSRect = beige
  
  pygame.display.flip()
  clock.tick(20)

# main game
updraftPos = 500
elapsedTime = 0

while start:

  elapsedTime +=1
  if (elapsedTime == 150):
     elapsedTime = 0
     updraftPos = random.randint(0, 500)

 # Y position code
  if gliderDown:
    yPosGlider += 1
  else:
    yPosGlider -= 1

  # X position code
  if horizontalGlider == "right":
    xPosGlider += 3
  else:
    xPosGlider -= 3


 # Display and sprite
  screen.fill(lightBlue)
  ground = pygame.draw.rect(screen, green, [0, 350, 600, 50])
  updraft = pygame.draw.rect(screen, darkerBlue, [updraftPos, 0, 100, 350])
  
  screen.blit(gliderImg, [xPosGlider, yPosGlider])
  glider = gliderImg.get_rect(topleft = (0+xPosGlider,0+yPosGlider))

  # collision
  if glider.colliderect(updraft):
    gliderDown = False
  else:
    gliderDown = True

  if (xPosGlider == 590): 
      print("You crashed going out of bounds :(")
      pygame.quit()
  if (xPosGlider == -50): 
    print("You crashed going out of bounds :(")
    pygame.quit()

  if glider.colliderect(ground):
    screen.fill(white)
    endText = fontOne.render("                You landed!", True, white)
    endRect = pygame.draw.rect(screen, black, [150, 150, 250, 40])
    screen.blit(endText, endRect)
    print("You landed!")
    pygame.quit()

  # detecting pressed keys
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      start = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          horizontalGlider = "left"
        elif event.key == pygame.K_RIGHT:
          horizontalGlider = "right"
    


  pygame.display.flip()
  clock.tick(40)


pygame.quit()