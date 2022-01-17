import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = (900, 500)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (60, 45)
ENEMY_WIDTH, ENEMY_HEIGHT = (55, 40)
LS1_WIDTH, LS1_HEIGHT = (10, 10)
LS2_WIDTH, LS2_HEIGHT = (10, 10)
LS3_WIDTH, LS3_HEIGHT = (10, 10)

FPS = 30
PLAYER_VEL = 7
ENEMY_VEL = 4
LASER_VEL = 10
PLAYER1_LIVE = 9.0
LEVEL = 0
SCORE = 0
enemies = []
new_enemies_list = enemies[:]
enemy_min = 10
enemy_max = 15

lost = False

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
SF_FONT = pygame.font.Font('FONTS/SpaceMission.otf', 20)
LOST_FONT = pygame.font.Font('FONTS/SpaceMission.otf', 40)
pygame.display.set_caption('Protect Planet Earth')

# Load BG
BACKGROUND = pygame.image.load("BG/bd_space_seamless_fl1.png").convert_alpha()

# Player Spaceship
SPACESHIP_PLAYER1 = pygame.image.load("GFX/SF00.png").convert_alpha()

# Enemy Spaceship
ENEMY_SHIP1 = pygame.image.load("GFX/EF01.png").convert_alpha()
ENEMY_SHIP2 = pygame.image.load("GFX/EF02.png").convert_alpha()

# Lasers
LS01_BLUE_STAR = pygame.image.load("GFX/LS04.png").convert_alpha()
LS02_EARTH = pygame.image.load("GFX/LS02.png").convert_alpha()
LS03_YELLOW_STAR = pygame.image.load("GFX/LS03.png").convert_alpha()

# Rotate and Scale image
PLAYER_1 = pygame.transform.rotate(
    pygame.transform.scale(SPACESHIP_PLAYER1, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
ENEMY_1 = pygame.transform.rotate(
    pygame.transform.scale(ENEMY_SHIP1, (ENEMY_WIDTH, ENEMY_HEIGHT)), 90)
ENEMY_2 = pygame.transform.rotate(
    pygame.transform.scale(ENEMY_SHIP2, (ENEMY_WIDTH, ENEMY_HEIGHT)), 90)
LS01 = pygame.transform.rotate(
    pygame.transform.scale(LS01_BLUE_STAR, (ENEMY_WIDTH, ENEMY_HEIGHT)), 23)
LS02 = pygame.transform.rotate(
    pygame.transform.scale(LS02_EARTH, (ENEMY_WIDTH, ENEMY_HEIGHT)), 90)
LS03 = pygame.transform.rotate(
    pygame.transform.scale(LS03_YELLOW_STAR, (ENEMY_WIDTH, ENEMY_HEIGHT)), 90)


# Load Background music
BG_MUSIC = pygame.mixer.Sound("BGM/Spaceship_Shooter.mp3")
BG_MUSIC.set_volume(0.2)
BG_MUSIC.play(loops=-1)
BG_LASER = pygame.mixer.Sound("BGM/Laser_2.mp3")
BG_LASER.set_volume(0.2)


class Ship:
    COOL_DOWN = 15

    # Define the ship
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

# Draw the ship and laser
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

# Movement for laser and collision of laser
    def move_lasers(self, vel, obj):
        global PLAYER1_LIVE
        self.cool_down()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(WIDTH):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                self.lasers.remove(laser)
                PLAYER1_LIVE -= 1

# How fast/often you can shoot laser
    def cool_down(self):
        if self.cool_down_counter >= self.COOL_DOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

# add lasers to a list, and af
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
            BG_LASER.play()


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.x += vel

    def off_screen(self, width):
        return not (0 <= self.x <= width)

    def collision(self, obj):
        return collide(self, obj)


class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = PLAYER_1
        self.laser_img = LS01
        self.mask = pygame.mask.from_surface(self.ship_img)

    def collision(self, objs):
        return collide(self, objs)

    def move_lasers(self, vel, objs):
        global SCORE
        self.cool_down()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(WIDTH):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        SCORE += 1
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)


player1 = Player(100, (HEIGHT - 45) / 2)


class Enemy(Ship):
    ENEMY_SHIPS = {
        "enemy1": (ENEMY_1, LS02),
        "enemy2": (ENEMY_2, LS03)
    }

    def __init__(self, x, y, enemy_ships):
        super().__init__(x, y)
        self.ship_img, self.laser_img = self.ENEMY_SHIPS[enemy_ships]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.x -= vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


# when game end, reset all variable to start
def endgame():
    global PLAYER1_LIVE, LEVEL, SCORE, enemies, enemy_max, enemy_min, lost
    draw_window()
    pygame.time.delay(5000)
    PLAYER1_LIVE = 9.0
    LEVEL = 0
    SCORE = 0
    enemy_min = 10
    enemy_max = 15
    enemies = []
    lost = False


# Control for player
def player1_movement(keys_pressed):
    if keys_pressed[pygame.K_a] and player1.x - PLAYER_VEL > 0:  # Left
        player1.x -= PLAYER_VEL
    if keys_pressed[pygame.K_d] and player1.x + PLAYER_VEL + player1.get_width() < WIDTH:  # Right
        player1.x += PLAYER_VEL
    if keys_pressed[pygame.K_w] and player1.y - PLAYER_VEL > 45:  # UP
        player1.y -= PLAYER_VEL
    if keys_pressed[pygame.K_s] and player1.y + PLAYER_VEL + player1.get_height() < HEIGHT:  # Down
        player1.y += PLAYER_VEL
    if keys_pressed[pygame.K_SPACE]:
        player1.shoot()


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def draw_window():
    WINDOW.fill(BLACK)
    # Draw player Level and lives as text.
    player1_label = SF_FONT.render(f"Player 1:", True, (255, 255, 255))
    player1_level = SF_FONT.render(f"LIVE: {PLAYER1_LIVE} LEVEL: {LEVEL} SCORE: {SCORE}", True, (255, 255, 255))
    WINDOW.blit(player1_label, (10, 10))
    WINDOW.blit(player1_level, (10, 30))
    # Draw BG, player and enemies.
    WINDOW.blit(BACKGROUND, (0, 0))
    # WINDOW.blit(PLAYER_1, (player1.x, player1.y))

    # WINDOW.blit(ENEMY_1, (WIDTH - ENEMY_1.get_width() - 10, 200))
    # WINDOW.blit(ENEMY_2, (WIDTH - ENEMY_2.get_width() - 10, 300))

    for enemy in enemies:
        enemy.draw(WINDOW)

    player1.draw(WINDOW)
    if lost:
        lost_label = LOST_FONT.render("You fail to protect the Earth", True, (255, 255, 255))
        WINDOW.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, HEIGHT / 2 - 20))

    pygame.display.update()
