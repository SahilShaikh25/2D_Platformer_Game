import pygame, level_1

level_1_bg = []
forest_back = pygame.image.load('img/parallax-forest-back-trees.png')
level_1_bg.append(pygame.transform.scale(forest_back, (600, 300)))
mid_tree = pygame.image.load('img/parallax-forest-middle-trees.png')
level_1_bg.append(pygame.transform.scale(mid_tree, (600, 300)))

def load_map(lvl):
    if lvl == 1:
        return level_1, level_1_bg
    elif lvl == 2:
        return level_2, level_2_bg
    elif lvl == 3:
        return level_3, level_3_bg

level_1 = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,42,43,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,10,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,2,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,11,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,20,21,21,21,21,21,21,21,22,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,10,11,11,11,11,11,11,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,-1,42,43,43,43,43,43,43,43,43,43,43,43,43,43,43,44,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,1,1,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,20,21,21,21,21,21,21,21,22,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,52,53,53,53,53,53,53,53,53,53,53,53,53,53,53,54,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,11,11,11,11,11,11,11,11,11,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [42,43,43,44,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,-1,-1,-1,-1,-1,52,53,53,53,53,53,53,53,53,53,53,53,53,53,53,54,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,-1,10,11,11,11,11,11,11,11,11,11,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [52,53,53,54,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,52,53,53,53,53,53,53,53,53,53,53,53,53,53,-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,31,-1,-1,31,-1,-1,-1,-1,-1,-1,20,21,21,21,22,21,21,21,22,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,-1,-1,-1,-1,-1,-1,10,11,11,11,11,11,11,11,11,11,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [52,53,53,54,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,52,53,53,53,53,53,53,53,53,53,53,53,-1,9,-1,-1,-1,-1,-1,31,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,11,11,11,11,11,11,11,11,11,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [52,53,53,54,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,52,53,53,53,53,53,53,53,53,53,53,53,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,31,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,11,11,11,11,11,11,11,11,11,11,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [52,53,53,53,43,43,43,43,43,43,43,43,43,43,43,44,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,52,53,53,53,53,53,53,53,53,53,53,53,43,43,43,44,-1,31,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,11,11,11,11,11,11,11,11,11,11,12,-1,-1,-1,-1,-1,-1,42,43,43,43,43,43,43,43,43,43,43,44],
            [52,53,53,53,53,53,53,53,53,53,53,53,53,53,53,54,55,55,55,55,55,55,55,55,55,55,55,55,55,55,52,53,53,53,53,53,53,53,53,53,53,53,53,53,53,54,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,42,43,43,43,55,55,55,43,43,43,43,43,43,43,43,43,43,43,43,43,55,55,55,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,11,11,11,11,11,11,11,11,11,11,12,-1,-1,-1,-1,-1,-1,52,53,53,53,53,53,53,53,53,53,53,54],
            [52,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,54,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,52,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,11,11,11,11,11,11,11,11,11,11,12,-1,-1,-1,-1,-1,-1,52,53,53,53,53,53,53,53,53,53,53,54]]

level_2_bg = []
bg_1 = pygame.image.load('level_2/img/background/plx-1.png')
level_2_bg.append(pygame.transform.scale(bg_1, (600, 300)))
bg_2 = pygame.image.load('level_2/img/background/plx-2.png')
level_2_bg.append(pygame.transform.scale(bg_2, (600, 300)))
bg_3 = pygame.image.load('level_2/img/background/plx-3.png')
level_2_bg.append(pygame.transform.scale(bg_3, (600, 300)))
bg_4 = pygame.image.load('level_2/img/background/plx-4.png')
level_2_bg.append(pygame.transform.scale(bg_4, (600, 300)))
bg_5 = pygame.image.load('level_2/img/background/plx-5.png')
level_2_bg.append(pygame.transform.scale(bg_5, (600, 300)))

level_2 = [[151,199,152,-1,-1,-1,-1,694,696,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,100,101,102,103,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,100,102,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,196,149,150,150,150,150,150,151,292,293,294,295,296,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,100,101,102,103,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [199,247,248,-1,-1,-1,-1,694,696,-1,-1,-1,-1,-1,-1,100,102,104,-1,-1,-1,-1,148,149,150,151,152,-1,-1,-1,-1,-1,-1,-1,-1,-1,292,294,296,647,647,647,647,647,647,647,647,647,648,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,196,197,198,198,198,198,198,198,200,9,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,148,149,150,151,152,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [247,151,152,646,647,647,647,695,696,-1,-1,-1,-1,-1,-1,196,246,200,-1,-1,-1,-1,196,197,198,199,200,-1,646,647,648,-1,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,452,453,456,457,457,458,-1,-1,100,101,101,102,103,101,102,103,101,102,103,101,102,103,103,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,196,197,198,198,198,198,198,198,248,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,196,197,198,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [151,199,200,695,695,695,695,695,696,-1,-1,-1,-1,-1,-1,292,294,296,-1,-1,-1,-1,196,197,198,199,200,-1,694,695,696,-1,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,696,-1,-1,-1,148,149,150,150,150,150,150,150,150,150,150,150,150,150,150,152,-1,-1,-1,-1,-1,-1,646,647,647,647,647,647,647,647,647,647,647,647,647,647,648,196,197,198,198,198,198,198,198,101,102,102,103,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,196,197,198,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [199,247,248,742,100,101,103,104,696,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,196,197,198,199,200,647,648,743,744,100,101,102,103,104,-1,-1,694,695,695,695,695,695,695,695,695,695,696,-1,-1,-1,196,197,198,198,198,198,198,198,198,198,198,198,198,198,199,200,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,695,695,695,695,696,196,197,198,198,198,198,198,198,198,198,198,151,200,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,196,197,198,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [247,151,152,-1,148,149,151,152,696,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,196,197,198,199,200,695,696,-1,-1,148,149,150,151,152,-1,-1,452,458,695,695,695,695,695,695,695,695,696,-1,-1,-1,196,197,198,198,198,198,198,198,198,198,198,198,198,198,199,248,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,695,695,695,695,696,196,197,198,198,198,198,198,198,198,198,198,199,200,-1,-1,-1,100,101,102,102,102,102,103,104,-1,-1,244,245,246,247,248,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [151,199,200,-1,292,293,295,296,696,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,196,197,198,199,200,743,744,-1,-1,292,293,294,295,296,-1,-1,694,695,695,695,695,695,695,695,695,695,696,-1,-1,-1,196,197,198,198,198,198,198,198,198,198,198,198,198,198,199,152,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,695,695,695,695,696,196,197,198,198,198,198,198,198,198,198,198,199,200,-1,-1,-1,196,149,150,150,150,150,151,152,-1,-1,292,293,294,295,296,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [199,247,248,-1,-1,-1,694,695,696,-1,452,458,-1,-1,-1,-1,-1,-1,-1,-1,-1,646,244,245,246,247,248,457,458,-1,-1,-1,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,696,-1,-1,-1,196,197,198,198,198,198,198,198,198,198,198,198,198,198,199,200,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,695,695,695,695,696,196,197,198,198,198,198,198,198,198,198,198,199,200,-1,-1,-1,196,197,198,198,198,198,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [247,151,152,-1,-1,-1,742,743,744,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,694,292,293,294,295,296,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,696,-1,-1,-1,196,197,198,198,198,198,198,198,198,198,198,198,198,198,199,248,101,101,101,101,104,-1,694,695,695,695,695,695,695,695,695,695,695,100,101,102,102,196,197,198,198,198,198,198,198,198,198,198,199,200,-1,-1,-1,196,197,198,198,198,198,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [151,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,452,458,-1,-1,-1,-1,742,695,695,695,695,696,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,696,-1,-1,-1,196,197,198,198,198,198,198,198,198,198,198,198,198,198,247,248,647,648,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,695,148,246,246,246,246,246,246,246,246,246,246,246,246,246,246,247,248,-1,-1,-1,196,197,198,198,198,198,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [199,247,248,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,452,453,454,455,456,457,458,-1,-1,452,458,-1,-1,-1,-1,-1,-1,694,695,695,695,695,-1,-1,-1,695,695,696,-1,-1,-1,196,197,198,198,198,198,-1,694,695,695,695,695,695,695,695,695,695,696,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,695,292,293,294,295,294,294,294,294,294,294,294,294,294,294,294,295,296,-1,-1,-1,196,197,198,198,198,198,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [247,151,152,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,694,695,695,695,695,-1,-1,-1,695,695,696,-1,-1,-1,196,197,198,198,198,198,-1,694,695,695,695,695,695,695,695,743,744,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,695,695,695,695,696,-1,-1,-1,694,695,695,695,695,695,695,695,695,-1,-1,-1,-1,244,197,198,198,198,198,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [151,199,200,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,694,695,695,695,695,-1,3,-1,695,695,744,-1,-1,-1,196,197,198,198,198,198,-1,694,695,695,3,695,695,695,695,-1,-1,-1,-1,-1,-1,-1,694,695,695,695,695,695,695,695,695,695,695,695,695,695,696,-1,-1,-1,-1,695,695,695,695,695,695,695,695,-1,-1,-1,7,244,245,246,246,246,246,247,248,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [199,247,248,673,674,675,676,677,678,679,680,681,682,673,674,675,676,677,678,679,680,681,682,673,674,675,676,677,-1,-1,680,681,682,673,674,675,676,677,678,679,680,681,682,673,674,675,676,677,678,679,680,681,244,245,246,246,246,246,673,674,675,676,677,678,679,680,681,677,678,679,680,681,682,673,674,675,676,677,678,679,680,681,682,673,674,675,676,677,678,679,680,681,673,674,675,676,677,678,679,680,681,682,673,674,675,292,293,294,294,294,294,295,296,674,675,676,677,678,679,680,681,682,673,674,675,676,677,678,679,680,681,682,673,674,675,676,677,678,679,680,681,682,673,674,675,676,677,678,679,680],
            [247,724,725,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,-1,-1,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728,729,730,721,722,723,724,725,726,727,728]]


level_3_bg = []
bg_1 = pygame.image.load('level_3/img/background/background.png')
level_3_bg.append(pygame.transform.scale(bg_1, (600, 300)))
bg_2 = pygame.image.load('level_3/img/background/middleground.png')
level_3_bg.append(pygame.transform.scale(bg_2, (600, 300)))

level_3 = [[206,206,206,206,206,206,206,206,230,206,206,206,206,206,206,80,82,80,82,80,82,82,82,82,82,82,82,206,230,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206],
            [206,206,206,254,254,255,254,255,254,82,82,82,82,82,86,104,106,104,106,104,106,106,106,106,106,106,106,84,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,82,82,82,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206],
            [206,207,208,209,278,279,278,279,278,106,106,106,106,106,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,88,89,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,230,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,82,82,82,80,80,80,80,86,106,106,106,84,82,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206],
            [206,207,208,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,36,37,35,35,41,42,-1,-1,-1,-1,-1,112,113,82,254,255,255,255,254,254,254,255,254,82,88,89,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,230,230,206,206,206,206,206,91,92,254,254,255,255,255,255,255,254,254,254,254,254,254,255,255,255,255,255,254,254,255,86,106,106,106,104,104,104,104,-1,-1,-1,-1,-1,106,84,82,82,82,82,80,80,80,82,82,82,82,82,82,206,206,206,206,206,206,206,206,206,206,206,206,82,82,82,80,82,80,82,82,82,82,82,206,206,206,206],
            [206,207,208,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,106,278,279,279,279,278,278,278,279,278,106,112,113,88,89,206,206,206,206,206,206,206,206,206,206,206,230,206,206,206,206,206,206,206,206,206,206,206,206,206,91,92,115,116,278,278,279,279,279,279,279,278,278,278,278,278,278,279,279,279,279,279,278,278,279,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,106,106,106,106,104,104,104,106,106,106,106,106,106,84,82,82,82,80,82,82,80,82,82,82,86,106,106,106,104,106,104,106,106,106,106,106,84,206,206,206],
            [206,207,208,154,155,158,158,159,159,3,159,158,158,158,158,158,158,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,112,113,88,89,206,230,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,115,116,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,106,106,106,104,106,106,104,106,106,106,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,84,206,206],
            [206,206,101,178,179,182,182,183,183,183,183,182,182,182,182,182,182,-1,-1,-1,-1,-1,-1,-1,213,214,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,112,113,88,89,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,91,92,86,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,204,205],
            [206,207,91,92,92,82,82,82,82,82,82,82,254,255,82,82,256,-1,-1,-1,-1,-1,-1,-1,237,238,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,112,113,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,91,92,115,116,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,157,158,150,150,3,154,155,159,159,159,152,160,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,157,158,158,154,155,159,159,159,150,150,154,155,158,150,-1,-1,-1,-1,-1,-1,-1,74,75],
            [206,207,208,209,116,106,106,106,106,106,106,106,278,279,106,106,280,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,84,206,206,230,206,206,206,206,206,230,206,206,206,206,206,206,115,116,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,181,182,174,174,182,178,179,183,183,183,176,184,-1,-1,36,37,37,35,37,37,42,-1,36,37,37,35,41,41,42,-1,-1,181,182,182,178,179,183,183,183,174,174,178,179,182,174,-1,-1,-1,-1,-1,-1,-1,98,99],
            [206,207,77,78,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,157,158,152,3,154,155,159,152,158,160,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,84,82,206,206,206,206,82,82,206,206,206,206,206,82,86,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,36,37,35,41,42,-1,-1,36,37,35,41,42,-1,-1,36,37,35,41,42,-1,74,75,206,206,206,206,206,206,206,206,206,230,77,78,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,74,75,206,82,82,206,230,206,206,206,206,206,206,206,232,147,148,150,152,152,152,145,159,229],
            [206,207,101,102,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,186,187,-1,-1,-1,130,181,182,176,183,178,179,183,176,182,184,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,106,11,11,11,106,106,106,106,11,11,11,11,106,-1,-1,-1,-1,-1,157,158,158,159,160,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,98,99,206,206,230,206,206,206,206,206,206,206,101,102,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,98,99,86,106,106,84,206,206,206,206,206,206,206,206,232,171,172,174,176,176,176,169,183,183],
            [230,207,208,209,36,37,37,37,41,42,-1,-1,154,155,158,159,154,3,158,150,152,152,152,152,210,211,158,154,155,159,229,206,206,206,206,206,206,206,206,208,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,157,158,158,160,181,182,182,183,184,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,204,205,206,206,206,206,206,206,206,206,206,206,208,209,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,-1,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,193,206,206],
            [206,207,232,-1,-1,-1,-1,-1,-1,-1,-1,-1,178,179,182,183,178,179,182,174,176,176,176,176,234,235,182,178,179,183,229,206,206,206,206,206,206,206,206,232,158,152,152,158,158,158,159,159,159,159,159,159,159,159,154,155,-1,-1,159,159,152,159,152,159,160,181,182,182,184,206,206,206,206,232,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,229,230,206,206,206,206,206,230,206,206,206,208,158,152,3,159,154,155,159,159,152,159,158,158,158,158,158,159,150,150,159,159,150,154,155,158,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206],
            [206,206,206,94,94,94,94,94,94,94,94,94,206,206,206,206,206,206,206,206,206,206,206,230,206,206,206,206,206,206,206,206,230,206,206,206,206,206,206,232,182,176,176,182,182,182,183,183,183,183,183,183,183,183,178,179,12,12,183,183,176,183,176,183,184,206,206,206,206,206,206,230,206,232,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,229,206,206,206,206,206,206,206,206,206,206,232,182,176,176,183,178,179,183,183,176,183,182,182,182,182,182,183,174,174,183,183,174,178,179,182,206,230,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206],
            [206,207,206,118,118,118,118,118,118,118,118,118,206,206,206,206,206,206,206,230,206,206,206,206,206,206,206,206,230,206,206,206,206,206,206,206,206,230,206,232,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,230,206,206,206,206,206,206,206,206,206,206,230,206,206,206,206,206,206,232,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,229,206,206,206,206,206,206,206,206,206,230,206,206,206,206,206,230,206,206,206,206,206,206,230,206,206,206,206,206,206,206,230,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206,206]]


