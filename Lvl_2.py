import random
import sys
import pygame
import Database
import Player, Enemy, Map

# initializing
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(64)

# Window
WINDOW_SIZE = (800, 500)
TILE_SIZE = 16

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Lost in the Abyss")
display = pygame.Surface((300,  230))

# variables
clock = pygame.time.Clock()
current_time = 0

enemy_ani_db = [['run', 7], ['attack', 7], ['hit', 1], ['death', 4]]
enemy_pos = [[224, 208], [480, 160], [928, 208], [1680, 208]]
enemy_dist = [288, 544, 990, 1744]

# font
font = pygame.font.Font("myfont/Stacked pixel.ttf", 10)

# sound
slash_sound = [pygame.mixer.Sound('sound/slashkut.wav'), pygame.mixer.Sound('sound/sword-sound.wav'), pygame.mixer.Sound('sound/sword-hit.wav')]
jump_grunt = pygame.mixer.Sound('sound/Grunting.wav')
attack_grunt = pygame.mixer.Sound('sound/ough2.wav')
level_complete_sound = pygame.mixer.Sound('sound/level_complete.wav')
diamond_found = pygame.mixer.Sound('sound/video-game-treasure.wav')

# image
diamond = pygame.image.load('level_2/img/icons/diamond.png')
diamond.set_colorkey((255, 255, 255))

three_star_icon = pygame.image.load('level_1/img/icons/star/Stars.png')
three_star_icon.set_colorkey((255, 255, 255))

one_star_icon = pygame.image.load('level_1/img/icons/star/Star1.png')
one_star_icon.set_colorkey((255, 255, 255))

empty_star_icon = pygame.image.load('level_1/img/icons/star/Star2.png')
empty_star_icon.set_colorkey((255, 255, 255))

forest_back = pygame.image.load('img/parallax-forest-back-trees.png')
forest_back = pygame.transform.scale(forest_back, (600, 300))
mid_tree = pygame.image.load('img/parallax-forest-middle-trees.png')
mid_tree = pygame.transform.scale(mid_tree, (600, 300))

jump_pad = pygame.image.load('level_2/img/map/assets/jumper.png')
jump_pad.set_colorkey((255, 255, 255))

sq1 = pygame.image.load('level_2/img/map/floating_square/jungle_00.png')
sq2 = pygame.image.load('level_2/img/map/floating_square/jungle_01.png')
sq3 = pygame.image.load('level_2/img/map/floating_square/jungle_02.png')
sq4 = pygame.image.load('level_2/img/map/floating_square/jungle_03.png')
sq5 = pygame.image.load('level_2/img/map/floating_square/jungle_04.png')
sq6 = pygame.image.load('level_2/img/map/floating_square/jungle_06.png')
sq7 = pygame.image.load('level_2/img/map/floating_square/jungle_07.png')
sq8 = pygame.image.load('level_2/img/map/floating_square/jungle_08.png')
sq9 = pygame.image.load('level_2/img/map/floating_square/jungle_09.png')
sq10 = pygame.image.load('level_2/img/map/floating_square/jungle_10.png')
sq11 = pygame.image.load('level_2/img/map/floating_square/jungle_12.png')
sq12 = pygame.image.load('level_2/img/map/floating_square/jungle_13.png')
sq13 = pygame.image.load('level_2/img/map/floating_square/jungle_14.png')
sq14 = pygame.image.load('level_2/img/map/floating_square/jungle_15.png')
sq15 = pygame.image.load('level_2/img/map/floating_square/jungle_16.png')
sq16 = pygame.image.load('level_2/img/map/floating_square/jungle_18.png')
sq17 = pygame.image.load('level_2/img/map/floating_square/jungle_19.png')
sq18 = pygame.image.load('level_2/img/map/floating_square/jungle_20.png')
sq19 = pygame.image.load('level_2/img/map/floating_square/jungle_21.png')
sq20 = pygame.image.load('level_2/img/map/floating_square/jungle_22.png')
sq21 = pygame.image.load('level_2/img/map/floating_square/jungle_24.png')
sq22 = pygame.image.load('level_2/img/map/floating_square/jungle_25.png')
sq23 = pygame.image.load('level_2/img/map/floating_square/jungle_26.png')
sq24 = pygame.image.load('level_2/img/map/floating_square/jungle_27.png')
sq25 = pygame.image.load('level_2/img/map/floating_square/jungle_28.png')

# ground images
gd1 = pygame.image.load('level_2/img/map/ground/jungle_32.png')
gd2 = pygame.image.load('level_2/img/map/ground/jungle_33.png')
gd3 = pygame.image.load('level_2/img/map/ground/jungle_34.png')
gd4 = pygame.image.load('level_2/img/map/ground/jungle_35.png')
gd5 = pygame.image.load('level_2/img/map/ground/jungle_36.png')
gd6 = pygame.image.load('level_2/img/map/ground/jungle_37.png')
gd7 = pygame.image.load('level_2/img/map/ground/jungle_38.png')
gd8 = pygame.image.load('level_2/img/map/ground/jungle_39.png')
gd9 = pygame.image.load('level_2/img/map/ground/jungle_40.png')
gd10 = pygame.image.load('level_2/img/map/ground/jungle_41.png')
gd13 = pygame.image.load('level_2/img/map/ground/jungle_44.png')
gd14 = pygame.image.load('level_2/img/map/ground/jungle_45.png')
gd15 = pygame.image.load('level_2/img/map/ground/jungle_46.png')
gd16 = pygame.image.load('level_2/img/map/ground/jungle_47.png')
gd17 = pygame.image.load('level_2/img/map/ground/jungle_48.png')
gd18 = pygame.image.load('level_2/img/map/ground/jungle_49.png')
gd19 = pygame.image.load('level_2/img/map/ground/jungle_50.png')
gd20 = pygame.image.load('level_2/img/map/ground/jungle_51.png')
gd21 = pygame.image.load('level_2/img/map/ground/jungle_52.png')
gd22 = pygame.image.load('level_2/img/map/ground/jungle_53.png')

# leaves images
leaves1 = pygame.image.load('level_2/img/map/leaves/jungle_08.png')
leaves2 = pygame.image.load('level_2/img/map/leaves/jungle_09.png')
leaves3 = pygame.image.load('level_2/img/map/leaves/jungle_10.png')
leaves4 = pygame.image.load('level_2/img/map/leaves/jungle_12.png')
leaves5 = pygame.image.load('level_2/img/map/leaves/jungle_13.png')
leaves6 = pygame.image.load('level_2/img/map/leaves/jungle_14.png')
leaves7 = pygame.image.load('level_2/img/map/leaves/jungle_16.png')
leaves8 = pygame.image.load('level_2/img/map/leaves/jungle_17.png')
leaves9 = pygame.image.load('level_2/img/map/leaves/jungle_18.png')

# floating floor
floating_floor1 = pygame.image.load('level_2/img/map/floating_ground/jungle_00.png')
floating_floor2 = pygame.image.load('level_2/img/map/floating_ground/jungle_01.png')
floating_floor3 = pygame.image.load('level_2/img/map/floating_ground/jungle_02.png')
floating_floor4 = pygame.image.load('level_2/img/map/floating_ground/jungle_03.png')
floating_floor5 = pygame.image.load('level_2/img/map/floating_ground/jungle_04.png')
floating_floor6 = pygame.image.load('level_2/img/map/floating_ground/jungle_05.png')
floating_floor7 = pygame.image.load('level_2/img/map/floating_ground/jungle_06.png')

# map
level = 2
map, background_objects = Map.load_map(level)

enemies = []
enemy_dist_counter = [32,32,32,16,32]
enemy_rect = []
enemy_data = []
enemy_start_loc = []
scroll = [0, 0]
count = 0
enemy_animation_database = {}
enemy_action = 'run'
enemy_frame = 0
enemy_flip = False

# loading map data
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

trap_time = 0

class Level_2():
    def __init__(self):
        self.true_scroll = [0, 0]
        self.scroll = [0, 0]
        self.animation_frames = {}
        self.player_rect = pygame.Rect(80, 208, Player.player_img.get_width(), Player.player_img.get_height())
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
        self.jump_pad_time = 0
        self.jump_pad_rect =  (1, 1, 1, 1)

    # main loop
    def level_2_loop(self):
        run = True
        while run:
            display.fill((100, 255, 100))
            current_time = pygame.time.get_ticks()

            # camera scroll
            if self.scroll[0] < 0:
                self.true_scroll[0] = (self.player_rect.x - self.true_scroll[0] - 152) / 20
            else:
                self.true_scroll[0] += (self.player_rect.x - self.true_scroll[0] - 152) / 20

            self.true_scroll[1] += (self.player_rect.y - self.true_scroll[1] - 140)/20

            self.scroll = self.true_scroll.copy()
            self.scroll[0] = int(self.scroll[0])
            self.scroll[1] = int(self.scroll[1])

            # background images
            for i in background_objects:
                display.blit(i, (0, 0))

            # Update scroll value
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
                    if tile == 100:
                        display.blit(sq1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 101:
                        display.blit(sq2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 102:
                        display.blit(sq3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 103:
                        display.blit(sq4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 104:
                        display.blit(sq5, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 148:
                        display.blit(sq6, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 149:
                        display.blit(sq7, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 150:
                        display.blit(sq8, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 151:
                        display.blit(sq9, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 152:
                        display.blit(sq10, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 196:
                        display.blit(sq11, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 197:
                        display.blit(sq12, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 198:
                        display.blit(sq13, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 199:
                        display.blit(sq14, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 200:
                        display.blit(sq15, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 244:
                        display.blit(sq16, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 245:
                        display.blit(sq17, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 246:
                        display.blit(sq18, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 247:
                        display.blit(sq19, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 248:
                        display.blit(sq20, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 292:
                        display.blit(sq21, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 293:
                        display.blit(sq22, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 294:
                        display.blit(sq23, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 295:
                        display.blit(sq24, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 296:
                        display.blit(sq25, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # ground tiles
                    elif tile == 673:
                        display.blit(gd1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 674:
                        display.blit(gd2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 675:
                        display.blit(gd3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 676:
                        display.blit(gd4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 677:
                        display.blit(gd5, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 678:
                        display.blit(gd6, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 679:
                        display.blit(gd7, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 680:
                        display.blit(gd8, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 681:
                        display.blit(gd9, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 682:
                        display.blit(gd10, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 721:
                        display.blit(gd13, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 722:
                        display.blit(gd14, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 723:
                        display.blit(gd15, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 724:
                        display.blit(gd16, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 725:
                        display.blit(gd17, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 726:
                        display.blit(gd18, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 727:
                        display.blit(gd19, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 728:
                        display.blit(gd20, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 729:
                        display.blit(gd21, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 730:
                        display.blit(gd22, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # leaves tiles
                    elif tile == 646:
                        display.blit(leaves1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 647:
                        display.blit(leaves2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 648:
                        display.blit(leaves3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 694:
                        display.blit(leaves4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 695:
                        display.blit(leaves5, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 696:
                        display.blit(leaves6, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 742:
                        display.blit(leaves7, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 743:
                        display.blit(leaves8, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 744:
                        display.blit(leaves9, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # floating floor
                    elif tile == 452:
                        display.blit(floating_floor1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 453:
                        display.blit(floating_floor2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 454:
                        display.blit(floating_floor3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 455:
                        display.blit(floating_floor4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 456:
                        display.blit(floating_floor5, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 457:
                        display.blit(floating_floor6, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 458:
                        display.blit(floating_floor7, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))

                    if tile == 7:
                        self.jump_pad_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                        display.blit(jump_pad, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))

                    if tile != -1 and tile != 3 and tile != 7 and tile != 9 and tile != 646 and tile != 647 and tile != 648 and tile != 694 \
                            and tile != 695 and tile != 696 and tile !=742 and tile != 743 and tile != 744:
                        tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    x += 1
                y += 1

                # Level end point
                end_rect = pygame.Rect(2330, 192, 64, 16)
                # pygame.draw.rect(display, (255, 0, 0), (end_rect.x - self.scroll[0], end_rect.y - self.scroll[1], 64, 16))
                if not self.player_rect.colliderect(end_rect):
                    pygame.draw.rect(display, (42, 86, 84, 255), (2330 - self.scroll[0], 170 - self.scroll[1], 32, 16))
                    exit_text = font.render("Exit", True, (255, 255, 255))
                    display.blit(exit_text, (2336 - self.scroll[0], 176 - self.scroll[1]))
                else:
                    pygame.draw.rect(display, (42, 86, 84, 255), (2330 - self.scroll[0], 170 - self.scroll[1], 55, 16))
                    press_enter_text = font.render("Press Enter", True, ((255, 255, 255)))
                    display.blit(press_enter_text, (2330 - self.scroll[0], 176 - self.scroll[1]))

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

                # Check key pressed
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
                            self.inAir = True
                            self.player_vertical = -5
                    else:
                        self.inAir = False
                    if event.key == pygame.K_SPACE:
                        self.attack = True

                # Check key released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.move_right = False
                    if event.key == pygame.K_a:
                        self.move_left = False

            # player horizontal movement
            player_movement = [0,0]
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

            # Check jump pad collision
            if pygame.time.get_ticks() - self.jump_pad_time > 2000:
                if self.player_rect.colliderect(self.jump_pad_rect):
                    self.player_vertical -= 8
                    self.jump_pad_time = pygame.time.get_ticks()

            # player vertical movement
            player_movement[1] += self.player_vertical
            self.player_vertical += 0.2
            if self.player_vertical > 3:
                self.player_vertical = 3

            # Change player action
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
                            self.player.health -= 2
                    else:
                        self.player.health -= 2
                        trap_time = current_time
                        self.first_hit = 0

            # treasure rendering
            if not self.has_diamond:
                y = 0
                for row in map:
                    x = 0
                    for tile in row:
                        if tile == 9:
                            display.blit(diamond,(x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
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
        animation_database['idle'] = player.update_animation('img/player/blue_cloak/idle', [7, 7, 7, 7])
        animation_database['run'] = player.update_animation('img/player/blue_cloak/run', [7, 7, 7, 7, 7, 7])
        animation_database['attack'] = player.update_animation('img/player/blue_cloak/light_attack',[2, 2, 4, 4, 4, 2, 2, 2, 2, 2])
        animation_database['jump'] = player.update_animation('img/player/blue_cloak/jump',[2, 2, 2, 2, 7, 7, 7, 7, 7, 7])
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