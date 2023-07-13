import pygame, random, sys
import Player, Enemy, Map, Database

# initializing
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(64)

# Window
WINDOW_SIZE = (800, 500)
TILE_SIZE = 16

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Lost in the Abyss")
display = pygame.Surface((300, 230))

# clock
clock = pygame.time.Clock()
current_time = 0

# map
level = 1
map, background_objects = Map.load_map(level)

# level variables
trap_time = 0
first_hit = 1
scroll = [0, 0]

# font
font = pygame.font.Font("myfont/Stacked pixel.ttf", 10)

# images
diamond = pygame.image.load('level_1/img/icons/diamond.png')
diamond.set_colorkey((255, 255, 255))

three_star_icon = pygame.image.load('level_1/img/icons/star/Stars.png')
three_star_icon.set_colorkey((255, 255, 255))

one_star_icon = pygame.image.load('level_1/img/icons/star/Star1.png')
one_star_icon.set_colorkey((255, 255, 255))

empty_star_icon = pygame.image.load('level_1/img/icons/star/Star2.png')
empty_star_icon.set_colorkey((255, 255, 255))

# floating floor
floating_floor1 = pygame.image.load('level_1/img/map/floating_floor/morning_adv_00.png')
floating_floor2 = pygame.image.load('level_1/img/map/floating_floor/morning_adv_01.png')
floating_floor3 = pygame.image.load('level_1/img/map/floating_floor/morning_adv_02.png')
floating_floor4 = pygame.image.load('level_1/img/map/floating_floor/morning_adv_10.png')
floating_floor5 = pygame.image.load('level_1/img/map/floating_floor/morning_adv_11.png')
floating_floor6 = pygame.image.load('level_1/img/map/floating_floor/morning_adv_12.png')
floating_floor7 = pygame.image.load('level_1/img/map/floating_floor/morning_adv_20.png')
floating_floor8 = pygame.image.load('level_1/img/map/floating_floor/morning_adv_21.png')
floating_floor9 = pygame.image.load('level_1/img/map/floating_floor/morning_adv_22.png')

# floor
floor1 = pygame.image.load('level_1/img/map/floor/morning_adv_42.png')
floor2 = pygame.image.load('level_1/img/map/floor/morning_adv_43.png')
floor3 = pygame.image.load('level_1/img/map/floor/morning_adv_44.png')
floor4 = pygame.image.load('level_1/img/map/floor/morning_adv_52.png')
floor5 = pygame.image.load('level_1/img/map/floor/morning_adv_53.png')
floor6 = pygame.image.load('level_1/img/map/floor/morning_adv_54.png')

# floating single floor
floating_single_floor = pygame.image.load('level_1/img/map/floating_single_floor/morning_adv_31.png')

# spike
spike = pygame.image.load('level_1/img/map/spike/morning_adv_55.png')

# sound
slash_sound = [pygame.mixer.Sound('sound/slashkut.wav'), pygame.mixer.Sound('sound/sword-sound.wav'), pygame.mixer.Sound('sound/sword-hit.wav')]
jump_grunt = pygame.mixer.Sound('sound/Grunting.wav')
attack_grunt = pygame.mixer.Sound('sound/ough2.wav')
level_complete_sound = pygame.mixer.Sound('sound/level_complete.wav')
diamond_found = pygame.mixer.Sound('sound/video-game-treasure.wav')

# enemy data
enemies = []
enemy_dist_counter = [32, 32, 32, 16, 32, 32]
enemy_ani_db = [['run', 7], ['attack', 7], ['hit', 1], ['death', 4]]
enemy_dist = [288, 544, 990, 1744]
enemy_rect = []
enemy_data = []
enemy_start_loc = []
count = 0
enemy_animation_database = {}
enemy_action = 'run'
enemy_frame = 0
enemy_flip = False

# loading enemy data
y = 0
for row in map:
    x = 0
    for tile in row:
        if tile == 3:
            enemy_rect.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            enemy_data.append([enemy_rect[count].x, enemy_rect[count].y, Enemy.enemy_img, enemy_dist_counter[count]])
            count = count + 1
        x += 1
    y +=1


# loading enemies in list
for i in range(len(enemy_data)):
    enemies.append(Enemy.Enemy(enemy_data[i][0], enemy_data[i][1], enemy_data[i][0] + 64))

for i in range(len(enemy_data)):
    enemy_animation_database = {}
    enemy_animation_database = enemies[i].get_ani_db(level)
    enemies[i].load_animation_db(enemy_animation_database)
    enemies[i].change_action('run')

# Level class
class Level_1():
    def __init__(self):
        self.true_scroll = [0, 0]
        self.scroll = [0, 0]
        self.animation_frames = {}
        self.player_rect = pygame.Rect(32, 112, Player.player_img.get_width(), Player.player_img.get_height())
        self.player = Player.Player(Player.player_img, self.player_rect, self.animation_frames)
        self.player_animation_db = self.player_ani_db(self.player)
        self.move_right = False
        self.move_left = False
        self.player_vertical = 0
        self.air_timer = 0
        self.player_action = 'idle'
        self.player_frame = 0
        self.player_flip = False
        self.inAir = False
        self.attack = False
        self.first_hit = 1
        self.has_diamond = False
        self.star_count = 0

    # Level loop
    def level_1_loop(self):
        run = True
        while run:
            display.fill((100,255,100))
            current_time = pygame.time.get_ticks()

            # camera scroll
            if self.scroll[0] < 0:
                self.true_scroll[0] = (self.player_rect.x - self.true_scroll[0] - 152)/20
            else:
                self.true_scroll[0] += (self.player_rect.x - self.true_scroll[0] - 152)/20

            self.true_scroll[1] += (self.player_rect.y - self.true_scroll[1] - 230)/20
            if self.true_scroll[1] > 200:
                self.true_scroll[1] = self.true_scroll[1]
            else:
                self.true_scroll[1] += (self.player_rect.y - self.true_scroll[1] - 50) / 20
            self.scroll = self.true_scroll.copy()
            self.scroll[0] = int(self.scroll[0])
            self.scroll[1] = int(self.scroll[1])

            # background images
            for i in background_objects:
                display.blit(i, (0, 0))

            if self.player_rect.x - self.scroll[0] != display.get_width()/2:
                self.scroll[0] += (self.player_rect.x - (self.scroll[0] + display.get_width()/2))/12
            if self.player_rect.y - self.scroll[1] != display.get_height()/2:
                self.scroll[1] += (self.player_rect.y - (self.scroll[1] + display.get_height()/2))/12

            # create and load tile rect
            tile_rects = []
            traps = []

            y = 0
            for row in map:
                x = 0
                for tile in row:
                    # floating floor
                    if tile == 0:
                        display.blit(floating_floor1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 1:
                        display.blit(floating_floor2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 2:
                        display.blit(floating_floor3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 10:
                        display.blit(floating_floor4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 11:
                        display.blit(floating_floor5, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 12:
                        display.blit(floating_floor6, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 20:
                        display.blit(floating_floor7, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 21:
                        display.blit(floating_floor8, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 22:
                        display.blit(floating_floor9, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # floor
                    elif tile == 42:
                        display.blit(floor1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 43:
                        display.blit(floor2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 44:
                        display.blit(floor3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 52:
                        display.blit(floor4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 53:
                        display.blit(floor5, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 54:
                        display.blit(floor6, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # floating single floor
                    elif tile == 31:
                        display.blit(floating_single_floor, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    #spike
                    if tile == 55:
                        display.blit(spike, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                        traps.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE + 8, 12, 16))
                    if tile != 3 and tile != -1 and tile != 55 and tile != 9:
                        tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    x += 1
                y += 1

            # Level end point
            end_rect = pygame.Rect(2336, 176, 64, 16)
            if not self.player_rect.colliderect(end_rect):
                exit_text = font.render("Exit", True, (255, 255, 0))
                display.blit(exit_text, (2336 - self.scroll[0], 176 - self.scroll[1]))
            else:
                press_enter_text = font.render("Press Enter", True, (255, 255, 0))
                display.blit(press_enter_text, (2330 - self.scroll[0], 160 - self.scroll[1]))

            # Fall damage
            if self.player_rect.y > (y * TILE_SIZE) + 200:
                self.player.health -= 100

            # If player dies
            if self.player.health <= 0:
                sum = 0
                for i in range(len(enemies)):
                    sum += enemies[i].health
                if sum == 0:
                    self.star_count += 1
                self.end(self.player)
                run = False

            # input check
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # check pressed keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.player_rect.colliderect(end_rect):
                            sum = 0
                            for i in range(len(enemies)):
                                sum += enemies[i].health
                            if sum == 0:
                                self.star_count += 1
                            self.star_count += 1
                            level_complete_sound.play()
                            self.end(self.player)
                            run = False

                    if event.key == pygame.K_d:
                        self.move_right = True
                    if event.key == pygame.K_a:
                        self.move_left = True
                    if event.key == pygame.K_w:
                        if self.air_timer < 6:
                            jump_grunt.play(0)
                            self.inAir = True
                            self.player_vertical = -5
                    else:
                        self.inAir = False
                    if event.key == pygame.K_SPACE:
                        self.attack = True

                # check released keys
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.move_right = False
                    if event.key == pygame.K_a:
                        self.move_left = False

            # player horizontal movement
            player_movement = [0, 0]
            if self.move_right:
                if self.player_rect.x > 2380 - scroll[0]:
                    player_movement[0] = 0
                else:
                    player_movement[0] += 2
            if self.move_left:
                if self.player_rect.x < 0:
                    player_movement[0] = 0
                else:
                    player_movement[0] -= 2

            # player vertical movement
            player_movement[1] += self.player_vertical
            self.player_vertical += 0.2
            if self.player_vertical > 3:
                self.player_vertical = 3

            #Change player action
            if player_movement[1] == 0:
                self.inAir = False
            if self.inAir:
                self.player_action, self.player_frame = self.player.change_action(self.player_action, self.player_frame,'jump')
            elif self.attack:
                self.player_action, self.player_frame = self.player.change_action(self.player_action, self.player_frame,'attack')
            elif player_movement[0] > 0:
                self.player_action, self.player_frame = self.player.change_action(self.player_action, self.player_frame,'run')
                self.player_flip = False
            elif player_movement[0] < 0:
                self.player_action, self.player_frame = self.player.change_action(self.player_action, self.player_frame,'run')
                self.player_flip = True
            else:
                self.player_action, self.player_frame = self.player.change_action(self.player_action, self.player_frame,'idle')

            # storing player object
            self.player_rect, collisions = self.player.move(self.player_rect, player_movement, tile_rects)

            # air time alter
            if collisions['bottom']:
                self.player_vertical = 0  # change to alter the air time after falling from a surface
                self.air_timer = 0
            else:
                self.air_timer += 1

            if collisions['top']:
                self.player_vertical = 3  # change to alter air time after colliding with bottom of a tile

            # rendering enemy
            for i in range(len(enemy_data)):
                img, player_health = enemies[i].update_ani(self.player.health)
                if enemies[i].health <= 0:
                    if enemies[i].alive:
                        self.player.score += random.randint(30, 50)
                        enemies[i].alive = False
                else:
                    enemies[i].draw(display, self.scroll, img, self.player_rect)
                self.player.health = player_health

            # trap
            for i in range(len(traps)):
                if self.player_rect.colliderect(traps[i]):
                    if self.first_hit == 0:
                        if current_time - trap_time > 2000:
                            trap_time = current_time
                            self.player.health -= 200
                    else:
                        self.player.health -= 200
                        trap_time = current_time
                        self.first_hit = 0

            # treasure rendering
            if not self.has_diamond:
                y = 0
                for row in map:
                    x = 0
                    for tile in row:
                        if tile == 9:
                            display.blit(diamond, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                            diamond_rect = pygame.Rect((x * TILE_SIZE, y * TILE_SIZE, 8, 8))
                            self.check_diamond(self.player, diamond_rect)
                        x += 1
                    y += 1

            # rendering player image
            self.player_frame += 1
            if self.player_frame >= len(self.player_animation_db[self.player_action]):
                if self.player_action == 'attack':
                    s = random.randint(0, 2)
                    slash_sound[s].play(0)
                    attack_grunt.play(0)
                    self.player_action, self.player_frame = self.player.change_action(self.player_action, self.player_frame, 'idle')
                    for i in range(len(enemy_data)):
                        if self.player_rect.colliderect(enemies[i].rect):
                            enemies[i].health -= random.randint(7, 10)
                    self.attack = False
                self.player_frame = 0
            player_img_id = self.player_animation_db[self.player_action][self.player_frame]
            player_img = self.animation_frames[player_img_id]
            # pygame.draw.rect(display, (0,0,0), (player_rect.x - scroll[0], player_rect.y - scroll[1], 16,16))
            display.blit(pygame.transform.flip(player_img, self.player_flip, False), (self.player_rect.x - self.scroll[0], self.player_rect.y - self.scroll[1]))
            self.player.draw_health(display)

            # Updating display
            new_surface = pygame.transform.scale(display, WINDOW_SIZE)
            screen.blit(new_surface, (0, 0))
            pygame.display.update()
            clock.tick(60)

    def player_ani_db(self, player):
        animation_database = {}
        animation_database['idle'] = player.update_animation('img/player/blue_cloak/idle', [7, 7, 7, 7]) #[7, 7, 7, 7, 7, 7]
        animation_database['run'] = player.update_animation('img/player/blue_cloak/run', [7, 7, 7, 7, 7, 7]) #[7, 7, 7, 7, 7, 7]
        animation_database['attack'] = player.update_animation('img/player/blue_cloak/light_attack', [2, 2, 4, 4, 4, 2, 2, 2, 2, 2]) #[2, 2, 4, 4, 2, 2, 2, 2]
        animation_database['jump'] = player.update_animation('img/player/blue_cloak/jump', [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) #[7, 7, 7, 7, 7]
        return animation_database

    def check_diamond(self, player, diamond_rect):
        if player.player_rect.colliderect(diamond_rect):
            diamond_found.play(0)
            self.has_diamond = True
            player.score += 50
            self.star_count += 1

    def end(self, player):
        display.fill((0, 0, 0))

        # Render appropriate text
        if self.player.health <= 0:
            new_font = pygame.font.Font("myfont/Stacked pixel.ttf", 15)
            text = new_font.render("Game over", True, (255, 255, 255))
            display.blit(text, (display.get_width() / 2 - 50, display.get_height() / 2 - 40))
            score = new_font.render(f"Your Score : {player.score}", True, (255, 255, 255))
            display.blit(score, (display.get_width() / 2 - 60, display.get_height() / 2))
        else:
            new_font = pygame.font.Font("myfont/Stacked pixel.ttf", 15)
            text = new_font.render("Level Complete", True, (255, 255, 255))
            display.blit(text, (display.get_width() / 2 - 60, display.get_height() / 2 - 40))
            score = new_font.render(f"Your Score : {player.score}", True, (255, 255, 255))
            display.blit(score, (display.get_width() / 2 - 55, display.get_height() / 2 + 20))

        # Render stars
        if self.star_count == 1:
            display.blit(one_star_icon, (display.get_width() / 2 - 40, display.get_height() / 2 - 20))
            display.blit(empty_star_icon, (display.get_width() / 2 - 20, display.get_height() / 2 - 15))
            display.blit(empty_star_icon, (display.get_width() / 2, display.get_height() / 2 - 20))
        elif self.star_count == 2:
            display.blit(one_star_icon, (display.get_width() / 2 - 40, display.get_height() / 2 - 20))
            display.blit(one_star_icon, (display.get_width() / 2 - 20, display.get_height() / 2 - 15))
            display.blit(empty_star_icon, (display.get_width() / 2, display.get_height() / 2 - 20))
        elif self.star_count == 3:
            display.blit(one_star_icon, (display.get_width() / 2 - 40, display.get_height() / 2 - 20))
            display.blit(one_star_icon, (display.get_width() / 2 - 20, display.get_height() / 2 - 15))
            display.blit(one_star_icon, (display.get_width() / 2, display.get_height() / 2 - 20))

        # database queries
        Database.create_table()
        Database.update_data(self.player.score)

        # Updating display
        new_surface = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(new_surface, (0, 0))
        pygame.display.update()
        pygame.time.wait(4000)
