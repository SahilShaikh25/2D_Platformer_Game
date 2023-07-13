import random
import pygame

enemy_img = pygame.image.load("img/enemy/idle/idle_0.png")

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

enemy_ani_db = [['run', 7], ['attack', 7], ['hit', 1], ['death', 4]]

class Enemy():
    def __init__(self, x, y, dest):
        self.rect = self.get_rect(x, y)
        self.path = [x, dest]
        self.pace = 1
        self.health = 50
        self.alive = True
        self.flip = False
        self.frames = []
        self.frame_index = 0
        self.index = 0
        self.action = ''
        self.attack_range = 8
        self.animation_database = {}

    def get_rect(self, x, y):
        return pygame.Rect(x, y, 16, 16)

    def draw(self, surf, scroll, img, player_rect):
        self.move(player_rect, surf, scroll)
        for i in range(7):
            if self.action == 'attack':
                surf.blit(pygame.transform.flip(img, self.flip, False),(self.rect.x - 20 - scroll[0], self.rect.y - scroll[1]))
            else:
                surf.blit(pygame.transform.flip(img, self.flip, False), (self.rect.x - scroll[0], self.rect.y - scroll[1]))

    def move(self, player_rect, surf, scroll):
        if self.rect.colliderect(player_rect):
            self.change_action('attack')
        else:
            self.change_action('run')
            if self.pace > 0: # moving right
                if self.rect.x + self.pace < self.path[1]:
                    self.rect.x += self.pace
                else:
                    self.pace = self.pace * -1
                    self.rect.x += self.pace
                    self.flip = True
            else: # moving left
                if self.rect.x > self.path[0] - self.pace:
                    self.rect.x += self.pace
                else:
                    self.pace = self.pace * -1
                    self.rect.x += self.pace
                    self.flip = False

    def load_ani(self, action, frame_numbers, lvl):
        animation_frame = []
        for n in range(frame_numbers):
            img = pygame.image.load(f'level_{lvl}/img/enemy/{action}/{action}_{n}.png')
            img.convert_alpha()
            width = img.get_rect().width
            height = img.get_rect().height
            img = pygame.transform.scale(img, (width * 0.5, height * 0.5))
            for i in range(5):
                animation_frame.append(img)
        return animation_frame

    def load_animation_db(self, animation_db):
        self.animation_database = animation_db

    def change_action(self, new_action):
        if self.action != new_action:
            self.action = new_action
            self.index = 0
            self.frames = self.animation_database[self.action]

    def update_ani(self, player_health):
        self.index += 1
        if self.action == 'attack':
            if self.index >= len(self.frames):
                self.change_action('run')
                player_health -= random.randint(3, 6)
        else:
            if self.index >= len(self.frames):
                self.index = 0
        return self.frames[self.index], player_health

    def get_ani_db(self, lvl):
        db = {}
        if lvl == 1:
            for x in range(4):
                db[enemy_ani_db[x][0]] = self.load_ani(enemy_ani_db[x][0], enemy_ani_db[x][1], 1)
        elif lvl == 2:
            for x in range(4):
                db[enemy_ani_db[x][0]] = self.load_ani(enemy_ani_db[x][0], enemy_ani_db[x][1], 2)
        elif lvl == 3:
            for x in range(4):
                db[enemy_ani_db[x][0]] = self.load_ani(enemy_ani_db[x][0], enemy_ani_db[x][1], 3)
        return db
