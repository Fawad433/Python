import pygame
import random
import math

# to initialize the module
pygame.init()

# create the screen
screen = pygame.display.set_mode((1000, 667))
# background
background = pygame.image.load('space-galaxy-background.jpg')

# title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# robot image and starting position
robotImg = pygame.image.load('robotics.png')
robotX = 500
robotY = 500
robotX_change = 0

# robot enemy image and starting position
robotEnemyImg = pygame.image.load('monster.png')
robotEnemyX = random.randint(0, 950)
robotEnemyY = random.randint(50, 200)
robotEnemyX_Change = 0.3
robotEnemyY_Change = 20

# bullet

bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'


def robot(x, y):
    # for putting the image on the screen
    screen.blit(robotImg, (x, y))


def robot_enemy(x, y):
    # for putting the image on the screen
    screen.blit(robotEnemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 1))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))

    if distance < 20:
        return True
    else:
        return False


# Game loop
running = True

while running:
    # change the screen color

    # screen.fill((0, 50, 0))
    # background image
    screen.blit(background, (0, 0))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

        # for the keyboard keys

        if events.type == pygame.KEYDOWN:
            print("Keystroke is pressed")
            if events.key == pygame.K_LEFT:
                robotX_change = -1  # if the left key is pressed the X should decrease
            if events.key == pygame.K_RIGHT:
                robotX_change = 1  # if the right key is pressed the X should increase
            if events.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = robotX
                    fire_bullet(bulletX, bulletY)

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                print("keystroke released")
                robotX_change = 0  # if the key is not pressed the robot should stop

    # the robot location update
    robotX = robotX + robotX_change

    # robot boundary check
    if robotX < 0:
        robotX = 0
    if robotX > 950:
        robotX = 950

    # enemy boundary check
    robotEnemyX = robotEnemyX + robotEnemyX_Change

    if robotEnemyX < 0:
        robotEnemyX_Change = 0.3
        robotEnemyY = robotEnemyY + robotEnemyY_Change  # for moving the enemy in y direction
        print(robotEnemyY)

    if robotEnemyX > 950:
        robotEnemyX_Change = -0.3
        robotEnemyY = robotEnemyY + robotEnemyY_Change
        print(robotEnemyY)

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY < 0:
        bullet_state = "ready"
        bulletY = 500

    collsion = isCollision(robotEnemyX, robotEnemyY, bulletX, bulletY)

    if collsion:
        bullet_state = "ready"
        bulletY = 500
        robotEnemyX = random.randint(0, 950)
        robotEnemyY = random.randint(50, 200)

    robot(robotX, robotY)
    robot_enemy(robotEnemyX, robotEnemyY)
    # update everything in the game
    pygame.display.update()
