import pygame, random
from pygame import mixer
def check_vacham():
    if heli_rect.colliderect(build1_rect):
        return True
    if heli_rect.colliderect(build2_rect):
         return True
    if heli_rect.colliderect(build3_rect):
         return True
    if heli_rect.colliderect(build4_rect):
         return True
    if heli_rect.colliderect(plane1_rect):
        return True
    if heli_rect.colliderect(plane2_rect):
        return True
    if heli_rect.colliderect(plane3_rect):
        return True
    if heli_rect.colliderect(plane4_rect):
        return True
    if heli_rect.top == 0:
        return True
    if heli_rect.colliderect(floor1) or heli_rect.colliderect(floor2):
        return True
    
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.init()
# set up khung , tên game và fps cho game
screen = pygame.display.set_mode((1500,600))
pygame.display.set_caption('CITY WAR')
clock = pygame.time.Clock()
# TẠO CÁC ĐÔI TƯỢNG CỦA GAME:

# tạo background
bg = pygame.image.load('game\images\\background.jpg').convert()
#tạo ảnh welcome game
welcome_image = pygame.image.load('game\images\welcome.png').convert_alpha()
welcome_image = pygame.transform.scale2x(welcome_image)
#tạo sàn
floor = pygame.image.load('game\images\\floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x = 0
floor_y = 480
#tạo các tòa nhà
build = pygame.image.load('game\images\\building.png').convert()
build = pygame.transform.scale2x(build)
build_height = [300, 200, 250, 180, 350]
build1_x = 0+1500
build2_x = 500+1500
build3_x = 1000+1500
build4_x = 1500+1500
build1_y = 300
build2_y = 250
build3_y = 300
build4_y = 200
build1_pass = False
build2_pass = False
build3_pass = False
build4_pass = False
#tạo các trực thăng địch
plane = pygame.image.load('game\images\heli_enemy.png').convert_alpha()
plane_height = [20, 60, 150]
plane1_x = build1_x + 250 +20
plane2_x = build2_x +250 +20
plane3_x = build3_x + 250 +20
plane4_x = build4_x + 250 +20
plane1_y = 60
plane2_y = 150
plane3_y = 20
plane4_y = 150
enemy1_pass = False
enemy2_pass = False
enemy3_pass = False
enemy4_pass = False
#tạo trực thăng player điều khiển
heli = pygame.image.load('game\images\heli_main.png').convert_alpha()
heli_x = 100
heli_y = 200
heli_move = 0
#tạo âm thanh cho game
bg_sound = mixer.music.load('game\sound\\background_music.wav')
building_score = pygame.mixer.Sound('game\sound\\building_pass_sound.wav')
enemy_score = pygame.mixer.Sound('game\sound\enemy_pass_sound.wav')
high_score_sound = pygame.mixer.Sound('game\sound\highscore_sound.wav')
crash_sound = pygame.mixer.Sound('game\sound\explosion_sound.wav')
bg_sound = mixer.music.set_volume(0.5)
#tạo font và cỡ chữ
font_attempt = pygame.font.SysFont('san', 25)
font = pygame.font.SysFont('san', 25)
font_high = pygame.font.SysFont('san', 25)
font_ketthuc = pygame.font.SysFont('san', 60)
font_kyluc = pygame.font.SysFont('san', 40)
#các thông số
WHITE = (255, 255, 255)
RED = (255, 0, 0)
repeat = 0
x_vantoc = 2
gravity = 0.1
running = True
pausing = False
gaming = False
coming = False
new_high_score = False
attempt = 1
score = 0
high_score = 0
building_width = 78
heli_enemy_width = 64

#----------------------------------------------------------------------------------------------------------------------------#

bg_sound = mixer.music.play(-1)
while running:
    screen.blit(bg,(0, 0))
    build1_rect = screen.blit(build,(build1_x, build1_y))
    build2_rect = screen.blit(build,(build2_x, build2_y))
    build3_rect = screen.blit(build,(build3_x, build3_y))
    build4_rect = screen.blit(build,(build4_x, build4_y))
    floor1 = screen.blit(floor,(floor_x, floor_y))
    floor2 = screen.blit(floor,(floor_x + 1008, floor_y))
    plane1_rect = screen.blit(plane,(plane1_x, plane1_y))
    plane2_rect = screen.blit(plane,(plane2_x, plane2_y))
    plane3_rect = screen.blit(plane,(plane3_x, plane3_y))
    plane4_rect = screen.blit(plane,(plane4_x, plane4_y))
    # sàn di chuyển
    if floor_x <= -1008:
        floor_x = 0
    floor_x -= x_vantoc
    if gaming== False:
        screen.blit(welcome_image,(590, 60))
    if gaming:
        coming = True
        # tòa nhà di chuyển
        build1_x -= x_vantoc
        if build1_x <= -80:
            build1_x = 2000
            build1_y = random.choice(build_height)
            build1_pass = False
        build2_x -= x_vantoc  
        if build2_x <= -80:
            build2_x = 2000
            build2_y = random.choice(build_height)
            build2_pass = False
        build3_x -= x_vantoc  
        if build3_x <= -80:
            build3_x = 2000
            build3_y = random.choice(build_height)
            build3_pass = False
        build4_x -= x_vantoc  
        if build4_x <= -80:
            build4_x = 2000
            build4_y = random.choice(build_height)
            build4_pass = False
        heli_rect = screen.blit(heli,(heli_x, heli_y))
        # trực thăng địch di chuyển
        plane1_x -= x_vantoc
        if plane1_x <= -80:
            plane1_x = 2000
            plane1_y = random.choice(plane_height)
            enemy1_pass = False
        plane2_x -= x_vantoc
        if plane2_x <= -80:
            plane2_x = 2000
            plane2_y = random.choice(plane_height)
            enemy2_pass = False
        plane3_x -= x_vantoc
        if plane3_x <= -80:
            plane3_x = 2000
            plane3_y = random.choice(plane_height)
            enemy3_pass = False
        plane4_x -= x_vantoc
        if plane4_x <= -80:
            plane4_x = 2000
            plane4_y = random.choice(plane_height)
            enemy4_pass = False
        
        # Tăng tốc độ - độ khó của trò chơi
        if score == 24 : #Sau 3 round, vận tốc tăng
            x_vantoc = 3
        if score == 56: #Sau 4 round tiếp theo, vận tốc tăng
            x_vantoc = 4
        if score == 96: #Sau 5 round tiếp theo,vận tốc tăng
            x_vantoc = 5
        if score == 144: #Sau 6 round tiếp theo,vận tốc tăng - mức khó nhất
            x_vantoc = 6

        if check_vacham():
            bg_sound = mixer.music.fadeout(1500)
            repeat += 1
            if repeat == 1:
                crash_sound.play()
            pausing = True
            x_vantoc = 0
            heli_move = 0
            gravity = 0
            ketthuc_txt = font_ketthuc.render("GAME OVER", True, RED)
            screen.blit(ketthuc_txt, (620, 200))
            if score == high_score and score != 0 and new_high_score == True:
                repeat += 1
                if repeat == 2 :
                    high_score_sound.play()
                kyluc = font_kyluc.render("new high score!", True, RED)
                screen.blit(kyluc, (640, 300))
        
        # ghi điểm
        attempt_txt = font.render("Attempt "+str(attempt), True, WHITE)
        screen.blit(attempt_txt, (1320, 10))
        score_txt = font.render("Score: "+str(score), True, WHITE)
        screen.blit(score_txt, (1320, 35))
        high_score_txt = font.render("High Score: "+str(high_score), True, WHITE)
        screen.blit(high_score_txt, (1320, 60))
        if score > high_score:
            new_high_score = True
            high_score = score
        # cộng điểm
        if build1_x + building_width <= heli_x and build1_pass == False:
            building_score.play()
            score += 1
            build1_pass = True
            
        if build2_x + building_width <= heli_x and build2_pass == False:
            building_score.play()
            score += 1
            build2_pass = True
            
        if build3_x + building_width <= heli_x and build3_pass == False:
            building_score.play()
            score += 1
            build3_pass = True
            
        if build4_x + building_width <= heli_x and build4_pass == False:
            building_score.play()
            score += 1
            build4_pass = True
            
        if plane1_x + heli_enemy_width <= heli_x and enemy1_pass == False:
            enemy_score.play()
            score += 1
            enemy1_pass = True

        if plane2_x + heli_enemy_width <= heli_x and enemy2_pass == False:
            enemy_score.play()
            score += 1
            enemy2_pass = True

        if plane3_x + heli_enemy_width <= heli_x and enemy3_pass == False:
            enemy_score.play()
            score += 1
            enemy3_pass = True

        if plane4_x + heli_enemy_width <= heli_x and enemy4_pass == False:
            enemy_score.play()
            score += 1
            enemy4_pass = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if  event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gaming = True         
        if event.type == pygame.KEYDOWN and pausing == False and coming == True:
            if event.key == pygame.K_SPACE:
                heli_move = 0
                heli_move -= 3
        if event.type == pygame.KEYDOWN and pausing == True and coming == True:
            if event.key == pygame.K_SPACE:
                bg_sound = mixer.music.play(-1)
                pausing = False
                build1_x = 0+1500
                build2_x = 500+1500
                build3_x = 1000+1500
                build4_x = 1500+1500
                plane1_x = build1_x + 250
                plane2_x = build2_x +250
                plane3_x = build3_x + 250
                plane4_x = build4_x + 250
                heli_y = 200
                heli_move = 0
                x_vantoc = 2
                gravity = 0.1
                score = 0
                repeat = 0
                attempt += 1
                new_high_score = False
    if coming == True:
        heli_move += gravity
        heli_y += heli_move
        screen.blit(heli,(heli_x,heli_y))
    pygame.display.flip()
    clock.tick(80)
pygame.quit()