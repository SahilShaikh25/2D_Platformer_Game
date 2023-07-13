import pygame

# variables
player_img = pygame.image.load("img/player/test_player/idle/idle_0.png")

# classes and methods
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

class Player():
    def __init__(self, img, player_rect, animation_frames):
        self.img = img
        self.player_rect = player_rect
        self.animation_list = []
        self.action = 0
        self.frame_index = 0
        self.health = 200
        self.attack = False
        self.isAlive = True
        self.animation_frames = animation_frames
        self.score = 0

    def draw_health(self, surf):
        font = pygame.font.Font("myfont/Stacked pixel.ttf", 10)
        text = font.render("Health : " + str(self.health), True, (255,255,255))
        surf.blit(text, (200, 10))

    def update_animation(self, path, frame_durations):
        animation_name = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_durations:
            animation_frame_id = animation_name + '_' + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            animation_image = pygame.image.load(img_loc).convert_alpha()
            animation_image.set_colorkey((0, 0, 0))
            img_rect = animation_image.get_rect()
            animation_image = pygame.transform.scale(animation_image, (img_rect.width * 0.5, img_rect.height * 0.5))
            self.animation_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def change_action(self, action_var, frame, new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var, frame

    #update action
    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    # move player
    def move(self, rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False, 'left': False, 'right': False}
        rect.x += movement[0]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True

        rect.y += movement[1]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            if movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types
