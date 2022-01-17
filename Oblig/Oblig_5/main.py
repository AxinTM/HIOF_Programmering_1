import game_module as gm
import random


def main():
    clock = gm.pygame.time.Clock()
    running = True

    while running:
        clock.tick(gm.FPS)  # set FPS to 60
        gm.draw_window()

        if gm.PLAYER1_LIVE <= 0:
            gm.lost = True

        if gm.lost:  # if game is lost stop game, reset all variable and restart game after 5 second
            running = False
            gm.endgame()
            main()

        if len(gm.enemies) == 0:
            gm.LEVEL += 1
            gm.enemy_max += 1
            gm.enemy_min += 1
            enemies_amount = random.randrange(gm.enemy_min, gm.enemy_max)
            print(gm.enemy_max, gm.enemy_min, enemies_amount)
            for i in range(enemies_amount):  # choose random which enemy gonna spawn in a random range of x and y axis
                enemy = gm.Enemy(random.randrange(1000, 2500), random.randrange(60, gm.HEIGHT-50),
                                 random.choice(["enemy1", "enemy2"]))
                gm.enemies.append(enemy)

        for event in gm.pygame.event.get():
            if event.type == gm.pygame.QUIT:
                running = False

        keys_pressed = gm.pygame.key.get_pressed()
        gm.player1_movement(keys_pressed)

        # Collision between enemy/laser and player, player remove 1 health, and the object of enemy and laser is removed
        for enemy in gm.enemies:
            enemy.move(gm.ENEMY_VEL)
            enemy.move_lasers(-gm.LASER_VEL, gm.player1)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if gm.collide(enemy, gm.player1):
                gm.PLAYER1_LIVE -= 1
                gm.enemies.remove(enemy)

            elif enemy.x + enemy.get_width() < 0:
                gm.PLAYER1_LIVE -= 1
                gm.enemies.remove(enemy)
        if len(gm.enemies) > 0:
            gm.player1.move_lasers(gm.LASER_VEL, gm.enemies)


if __name__ == "__main__":
    main()
