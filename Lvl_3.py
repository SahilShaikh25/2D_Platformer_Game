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

# font
font = pygame.font.Font("myfont/Stacked pixel.ttf", 10)

# sound
slash_sound = [pygame.mixer.Sound('sound/slashkut.wav'), pygame.mixer.Sound('sound/sword-sound.wav'), pygame.mixer.Sound('sound/sword-hit.wav')]
jump_grunt = pygame.mixer.Sound('sound/Grunting.wav')
attack_grunt = pygame.mixer.Sound('sound/ough2.wav')
level_complete_sound = pygame.mixer.Sound('sound/level_complete.wav')
diamond_found = pygame.mixer.Sound('sound/video-game-treasure.wav')

# image
forest_back = pygame.image.load('img/parallax-forest-back-trees.png')
forest_back = pygame.transform.scale(forest_back, (600, 300))
mid_tree = pygame.image.load('img/parallax-forest-middle-trees.png')
mid_tree = pygame.transform.scale(mid_tree, (600, 300))

jump_pad = pygame.image.load('level_2/img/map/assets/jumper.png')
jump_pad.set_colorkey((255, 255, 255))

diamond = pygame.image.load('level_1/img/icons/diamond.png')
diamond.set_colorkey((255, 255, 255))

three_star_icon = pygame.image.load('level_1/img/icons/star/Stars.png')
three_star_icon.set_colorkey((255, 255, 255))

one_star_icon = pygame.image.load('level_1/img/icons/star/Star1.png')
one_star_icon.set_colorkey((255, 255, 255))

empty_star_icon = pygame.image.load('level_1/img/icons/star/Star2.png')
empty_star_icon.set_colorkey((255, 255, 255))

# floor
floor1 = pygame.image.load('level_3/img/map/purple_dungeon/floor/dungeon_065.png')
floor2 = pygame.image.load('level_3/img/map/purple_dungeon/floor/dungeon_066.png')
floor3 = pygame.image.load('level_3/img/map/purple_dungeon/floor/dungeon_084.png')
floor4 = pygame.image.load('level_3/img/map/purple_dungeon/floor/dungeon_085.png')

# floating stones
ft_stones1 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_068.png')
ft_stones2 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_069.png')
ft_stones3 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_070.png')
ft_stones4 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_071.png')
ft_stones5 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_087.png')
ft_stones6 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_088.png')
ft_stones7 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_089.png')
ft_stones8 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_090.png')
ft_stones9 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_097.png')
ft_stones10 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_098.png')
ft_stones11 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_099.png')
ft_stones12 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_100.png')
ft_stones13 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_101.png')
ft_stones14 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_102.png')
ft_stones15 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_119.png')
ft_stones16 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_120.png')
ft_stones17 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_121.png')
ft_stones18 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_122.png')
ft_stones19 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_140.png')
ft_stones20 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_141.png')
ft_stones21 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_142.png')
ft_stones22 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_143.png')
ft_stones23 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_148.png')
ft_stones24 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_149.png')
ft_stones25 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_150.png')
ft_stones26 = pygame.image.load('level_3/img/map/purple_dungeon/floating_stones/dungeon_151.png')

# face left
left_face1 = pygame.image.load('level_3/img/map/purple_dungeon/face/left/dungeon_017.png')
left_face2 = pygame.image.load('level_3/img/map/purple_dungeon/face/left/dungeon_018.png')
left_face3 = pygame.image.load('level_3/img/map/purple_dungeon/face/left/dungeon_039.png')
left_face4 = pygame.image.load('level_3/img/map/purple_dungeon/face/left/dungeon_040.png')

# face right
right_face1 = pygame.image.load('level_3/img/map/purple_dungeon/face/right/dungeon_020.png')
right_face2 = pygame.image.load('level_3/img/map/purple_dungeon/face/right/dungeon_021.png')
right_face3 = pygame.image.load('level_3/img/map/purple_dungeon/face/right/dungeon_042.png')
right_face4 = pygame.image.load('level_3/img/map/purple_dungeon/face/right/dungeon_043.png')

# pillar
pillar1 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_092.png')
pillar2 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_093.png')
pillar3 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_103.png')
pillar4 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_104.png')
pillar5 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_124.png')
pillar6 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_125.png')
pillar7 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_145.png')
pillar8 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_146.png')
pillar9 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_073.png')
pillar10 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_106.png')
pillar11 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_107.png')
pillar12 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_127.png')
pillar13 = pygame.image.load('level_3/img/map/purple_dungeon/pillar/dungeon_128.png')

# floating pipes
ft_pipe1 = pygame.image.load('level_3/img/map/purple_dungeon/floating_pipes/dungeon_006.png')
ft_pipe2 = pygame.image.load('level_3/img/map/purple_dungeon/floating_pipes/dungeon_008.png')
ft_pipe3 = pygame.image.load('level_3/img/map/purple_dungeon/floating_pipes/dungeon_009.png')
ft_pipe4 = pygame.image.load('level_3/img/map/purple_dungeon/floating_pipes/dungeon_010.png')
ft_pipe5 = pygame.image.load('level_3/img/map/purple_dungeon/floating_pipes/dungeon_011.png')
ft_pipe6 = pygame.image.load('level_3/img/map/purple_dungeon/floating_pipes/dungeon_013.png')
ft_pipe7 = pygame.image.load('level_3/img/map/purple_dungeon/floating_pipes/dungeon_014.png')
ft_pipe8 = pygame.image.load('level_3/img/map/purple_dungeon/floating_pipes/dungeon_015.png')

# spikes
ver_spike1 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/vertical_spike/dungeon_025.png')
ver_spike2 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/vertical_spike/dungeon_047.png')

dia_spike1 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/diagonal_single_spike/dungeon_027.png')
dia_spike2 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/diagonal_single_spike/dungeon_029.png')

tri_spike1 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/triple_spikes/dungeon_031.png')
tri_spike2 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/triple_spikes/dungeon_032.png')
tri_spike3 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/triple_spikes/dungeon_034.png')
tri_spike4 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/triple_spikes/dungeon_035.png')
tri_spike5 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/triple_spikes/dungeon_049.png')
tri_spike6 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/triple_spikes/dungeon_050.png')
tri_spike7 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/triple_spikes/dungeon_052.png')
tri_spike8 = pygame.image.load('level_3/img/map/purple_dungeon/spikes/triple_spikes/dungeon_053.png')

spike_trap = pygame.image.load('level_3/img/map/purple_dungeon/spikes/spike.png')
inverted_spike_trap = pygame.transform.rotate(spike_trap, 180)

# plant
usd_plant1 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_023.png')
usd_plant2 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_045.png')

algae1 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_061.png')
algae2 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_063.png')
algae3 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_080.png')
algae4 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_082.png')

mushrooms1 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_058.png')
mushrooms2 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_059.png')
mushrooms3 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_077.png')
mushrooms4 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_078.png')

flower1 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_056.png')
flower2 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_075.png')
flower3 = pygame.image.load('level_3/img/map/purple_dungeon/plant/dungeon_095.png')

# water
water1 = pygame.image.load('level_3/img/map/purple_dungeon/water/dungeon_037.png')
water2 = pygame.image.load('level_3/img/map/purple_dungeon/water/dungeon_054.png')

# map
level = 3
map, background_objects = Map.load_map(level)

enemies = []
enemy_ani_db = [['run', 7], ['attack', 7], ['hit', 1], ['death', 4]]
enemy_dist = [288, 544, 990, 1744]
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

water_tiles = []
# loading map data
y = 0
for row in map:
    x = 0
    for tile in row:
        if tile == 3:
            enemy_rect.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            enemy_data.append([enemy_rect[count].x, enemy_rect[count].y, Enemy.enemy_img, enemy_dist_counter[count]])
            count = count + 1
        if tile == 94:
            water_tiles.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
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

class Level_3():
    def __init__(self):
        self.true_scroll = [0, 0]
        self.scroll = [0, 0]
        self.animation_frames = {}
        self.player_rect = pygame.Rect(112, 176, Player.player_img.get_width(), Player.player_img.get_height())
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
        self.water_first_hit = 1
        self.first_hit = 1
        self.has_diamond = False
        self.jump_pad_time = 0
        self.star_count = 0


    # main loop
    def level_3_loop(self):
        run = True
        while run:
            display.fill((100,255,100))
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

            if self.player_rect.x - self.scroll[0] != display.get_width()/2:
                self.scroll[0] += (self.player_rect.x - (self.scroll[0] + display.get_width()/2))/12
            if self.player_rect.y - self.scroll[1] != display.get_height()/2:
                self.scroll[1] += (self.player_rect.y - (self.scroll[1] + display.get_height()/2))/12

            # create and load tile rect
            tile_rects = []
            spike_traps = []
            inv_spike_traps = []

            y = 0
            for row in map:
                x = 0
                for tile in row:
                    if tile == 35:
                        display.blit(ft_pipe2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 36:
                        display.blit(ft_pipe3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 37:
                        display.blit(ft_pipe4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 41:
                        display.blit(ft_pipe7, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 42:
                        display.blit(ft_pipe8, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    #left facing statue
                    elif tile == 74:
                        display.blit(left_face1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 75:
                        display.blit(left_face2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 98:
                        display.blit(left_face3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 99:
                        display.blit(left_face4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # right facing statue
                    elif tile == 77:
                        display.blit(right_face1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 78:
                        display.blit(right_face2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 101:
                        display.blit(right_face3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 102:
                        display.blit(right_face4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # upside down plant
                    elif tile == 80:
                        display.blit(usd_plant1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 104:
                        display.blit(usd_plant2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # algae
                    elif tile == 150:
                        display.blit(algae1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 152:
                        display.blit(algae2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 174:
                        display.blit(algae3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 176:
                        display.blit(algae4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # mushrooms
                    elif tile == 147:
                        display.blit(mushrooms1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 148:
                        display.blit(mushrooms2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 171:
                        display.blit(mushrooms3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 172:
                        display.blit(mushrooms4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # flowers
                    elif tile == 145:
                        display.blit(flower1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 169:
                        display.blit(flower2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 193:
                        display.blit(flower3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # vertical spike
                    elif tile == 82:
                        display.blit(ver_spike1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 106:
                        display.blit(ver_spike2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # diagonal spike
                    elif tile == 84:
                        display.blit(dia_spike1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 86:
                        display.blit(dia_spike2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # triangular spikes
                    elif tile == 88:
                        display.blit(tri_spike1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 89:
                        display.blit(tri_spike2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 91:
                        display.blit(tri_spike3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 92:
                        display.blit(tri_spike4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 112:
                        display.blit(tri_spike5, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 113:
                        display.blit(tri_spike6, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 115:
                        display.blit(tri_spike7, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 116:
                        display.blit(tri_spike8, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    #floor
                    elif tile == 154:
                        display.blit(floor1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 155:
                        display.blit(floor2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 178:
                        display.blit(floor3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 179:
                        display.blit(floor4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # floating stones
                    elif tile == 157:
                        display.blit(ft_stones1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 158:
                        display.blit(ft_stones2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 159:
                        display.blit(ft_stones3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 160:
                        display.blit(ft_stones4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 181:
                        display.blit(ft_stones5, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 182:
                        display.blit(ft_stones6, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 183:
                        display.blit(ft_stones7, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 184:
                        display.blit(ft_stones8, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 204:
                        display.blit(ft_stones9, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 205:
                        display.blit(ft_stones10, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 206:
                        display.blit(ft_stones11, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 207:
                        display.blit(ft_stones12, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 208:
                        display.blit(ft_stones13, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 209:
                        display.blit(ft_stones14, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 229:
                        display.blit(ft_stones15, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 230:
                        display.blit(ft_stones16, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 231:
                        display.blit(ft_stones17, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 232:
                        display.blit(ft_stones18, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 253:
                        display.blit(ft_stones19, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 254:
                        display.blit(ft_stones20, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 255:
                        display.blit(ft_stones21, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 256:
                        display.blit(ft_stones22, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 277:
                        display.blit(ft_stones23, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 278:
                        display.blit(ft_stones24, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 279:
                        display.blit(ft_stones25, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 280:
                        display.blit(ft_stones26, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # pillar
                    elif tile == 165:
                        display.blit(pillar9, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 186:
                        display.blit(pillar1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 187:
                        display.blit(pillar2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 210:
                        display.blit(pillar3, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 211:
                        display.blit(pillar4, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 234:
                        display.blit(pillar5, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 235:
                        display.blit(pillar6, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 258:
                        display.blit(pillar7, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 259:
                        display.blit(pillar8, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 213:
                        display.blit(pillar10, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 214:
                        display.blit(pillar11, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 237:
                        display.blit(pillar12, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 238:
                        display.blit(pillar13, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    # water
                    elif tile == 94:
                        display.blit(water1, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                    elif tile == 118:
                        display.blit(water2, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))

                    # spike traps
                    if tile == 12:
                        display.blit(spike_trap, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                        spike_traps.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE + 8, 12, 16))
                    elif tile == 11:
                        display.blit(inverted_spike_trap, (x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                        inv_spike_traps.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE - 8, 12, 16))

                    # create rect list
                    if tile != -1 and tile != 84 and tile != 86 and tile != 94 and tile != 104 and tile != 106 and tile != 112 and tile != 113 and tile != 115 \
                            and tile != 116 and tile != 145 and tile != 147 and tile != 148 and tile != 150 and tile != 152 and tile != 154 and tile != 155 \
                            and tile != 157 and tile != 158 and tile != 159 and tile != 160 and tile != 204 and tile != 209 and tile != 277 and tile != 278 \
                            and tile != 279 and tile != 280 and tile != 3 and tile != 10 and tile != 11 and tile != 12:
                        tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    x += 1
                y += 1

            end_rect = pygame.Rect(2304, 144, 64, 16)
            # pygame.draw.rect(display, (255, 0, 0), (end_rect.x - self.scroll[0], end_rect.y - self.scroll[1], 64, 16))
            if not self.player_rect.colliderect(end_rect):
                exit_text = font.render("Exit", True, (255, 255, 255))
                display.blit(exit_text, (2320 - self.scroll[0], 128 - self.scroll[1]))
            else:
                press_enter_text = font.render("Press Enter", True, (255, 255, 255))
                display.blit(press_enter_text, (2310 - self.scroll[0], 128 - self.scroll[1]))

            if self.player_rect.y > (y * TILE_SIZE) + 200:
                self.player.health -= 100

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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.player_rect.colliderect(end_rect):
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

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.move_right = False
                    if event.key == pygame.K_a:
                        self.move_left = False

            # player horizontal movement
            player_movement = [0,0]
            if self.move_right:
                    player_movement[0] += 2
            if self.move_left:
                if self.player_rect.x < 0:
                    player_movement[0] = 0
                else:
                    player_movement[0] -= 2

            player_movement[1] += self.player_vertical
            self.player_vertical += 0.2
            if self.player_vertical > 3:
                self.player_vertical = 3

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
            for i in range(len(spike_traps)):
                if self.player_rect.colliderect(spike_traps[i]):
                    if self.first_hit == 0:
                        if current_time - trap_time > 2000:
                            trap_time = current_time
                            self.player.health -= 200
                    else:
                        self.player.health -= 200
                        trap_time = current_time
                        self.first_hit = 0

            # inverted spike trap
            for i in range(len(inv_spike_traps)):
                if self.player_rect.colliderect(inv_spike_traps[i]):
                    if self.first_hit == 0:
                        if current_time - trap_time > 2000:
                            trap_time = current_time
                            self.player.health -= 200
                    else:
                        self.player.health -= 200
                        trap_time = current_time
                        self.first_hit = 0

            # Tresure rendering
            if not self.has_diamond:
                y = 0
                for row in map:
                    x = 0
                    for tile in row:
                        if tile == 10:
                            display.blit(diamond,(x * TILE_SIZE - self.scroll[0], y * TILE_SIZE - self.scroll[1]))
                            diamond_rect = pygame.Rect((x * TILE_SIZE, y * TILE_SIZE, 10, 10))
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

            for i in range(len(water_tiles)):
                if self.player_rect.colliderect(water_tiles[i]):
                    if not self.player.health < 0:
                        if self.water_first_hit == 0:
                            if current_time - trap_time > 1000:
                                trap_time = current_time
                                self.player.health -= 200
                        else:
                            self.player.health -= 200
                            trap_time = current_time
                            self.water_first_hit = 0
                    else:
                            self.end(self.player_rect)
                            run = False

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
        animation_database['hit'] = player.update_animation('img/player/blue_cloak/hit',[7, 7, 7])
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
