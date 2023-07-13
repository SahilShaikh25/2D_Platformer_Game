import pygame
import Database
import Lvl_1
import Lvl_2
import Lvl_3

# initialize
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(64)

# Window
WINDOW_SIZE = (800, 500)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Lost in the Abyss")
display = pygame.Surface((300, 230))

clock = pygame.time.Clock()

# font
new_font = pygame.font.Font("myfont/Stacked pixel.ttf", 30)

# image
bg = pygame.image.load('img/map_img/abyss.jpg')
bg = pygame.transform.scale(bg, (300, 230))
play_bg = pygame.image.load('img/map_img/jap_catsle.jpg')
play_bg = pygame.transform.scale(play_bg, (300, 230))
hs_bg = pygame.image.load('img/map_img/hill_track.jpg')
hs_bg = pygame.transform.scale(hs_bg, (300, 230))

# sound
m = pygame.mixer.music.load('sound/Desert Theme.mp3')
pygame.mixer.music.play(-1)

click = pygame.mixer.Sound('sound/click_sound.wav')


def play():
    level_num = 1
    run = True
    while run:
        display.fill((0, 0, 0))
        display.blit(play_bg, (0, 0))

        if level_num == 0:
            pygame.draw.rect(display, (0, 0, 0), (5, 110, 70, 40))
        elif level_num == 1:
            pygame.draw.rect(display, (0, 0, 0), (90, 145, 30, 30))
        elif level_num == 2:
            pygame.draw.rect(display, (0, 0, 0), (140, 145, 30, 30))
        elif level_num == 3:
            pygame.draw.rect(display, (0, 0, 0), (190, 145, 30, 30))

        display.blit(new_font.render("Select Level", True, (255, 255, 255)), (display.get_width() / 2 - 90, 20))
        display.blit(new_font.render("Back", True, (255, 255, 255)), (10, 120))
        display.blit(new_font.render("1", True, (255, 255, 255)), (100, 150))
        display.blit(new_font.render("2", True, (255, 255, 255)), (150, 150))
        display.blit(new_font.render("3", True, (255, 255, 255)), (200, 150))
        note_font = pygame.font.Font("myfont/Stacked pixel.ttf", 15)
        display.blit(note_font.render("(Use Left and Right Arrow keys)", True, (255, 255, 255)), (35, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if level_num < 3:
                        click.play()
                        level_num += 1
                    else:
                        level_num = 0
                if event.key == pygame.K_LEFT:
                    if level_num > 0:
                        click.play()
                        level_num -= 1
                    else:
                        level_num = 3
                if event.key == pygame.K_RETURN:
                    click.play()
                    return level_num
        new_surface = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(new_surface, (0, 0))
        pygame.display.update()

def highscore():
    run = True
    while run:
        display.fill((0, 0, 0))
        display.blit(hs_bg, (0, 0))

        highscore = Database.get_highscore()
        pygame.draw.rect(display, (0, 0, 0), (15, 20, 70, 40))
        display.blit(new_font.render(f"Back", True, (255, 255, 255)), (20, 30))
        display.blit(new_font.render(f"Highscore", True, (255, 255, 255)), (80, 100))
        display.blit(new_font.render(f"{highscore}", True, (255, 255, 255)), (120, 130))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    click.play()
                    run = False

        new_surface = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(new_surface, (0, 0))
        pygame.display.update()


btn_num = 1
run = True
while run:
    display.fill((0, 0, 0))

    display.blit(bg, (0, 0))

    if btn_num == 1:
        pygame.draw.rect(display, (0, 0, 0), (20, 45, 65, 30))
    elif btn_num == 2:
        pygame.draw.rect(display, (0, 0, 0), (20, 95, 140, 30))
    elif btn_num == 3:
        pygame.draw.rect(display, (0, 0, 0), (20, 135, 60, 30))

    display.blit(new_font.render("play", True, (255, 255, 255)), (20, 50))
    display.blit(new_font.render("high score", True, (255, 255, 255)), (20, 100))
    display.blit(new_font.render("exit", True, (255, 255, 255)), (20, 140))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                click.play()
                if btn_num < 3:
                    btn_num += 1
                else:
                    btn_num = 1

            if event.key ==pygame.K_UP:
                click.play()
                if btn_num > 1:
                    btn_num -= 1
                else:
                    btn_num = 3

            if event.key == pygame.K_RETURN:
                click.play()
                if btn_num == 1:
                    level = play()
                    if level == 0:
                        pass
                    elif level == 1:
                        pygame.mixer.music.fadeout(1000)
                        pygame.time.wait(1000)
                        x = Lvl_1.Level_1()
                        x.level_1_loop()
                    elif level == 2:
                        pygame.mixer.music.fadeout(1000)
                        pygame.time.wait(1000)
                        x = Lvl_2.Level_2()
                        x.level_2_loop()
                    elif level == 3:
                        pygame.mixer.music.fadeout(1000)
                        pygame.time.wait(1000)
                        x = Lvl_3.Level_3()
                        x.level_3_loop()
                elif btn_num == 2:
                    highscore()
                elif btn_num == 3:
                    run = False

    new_surface = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(new_surface, (0, 0))
    pygame.display.update()
