import pygame
pygame.init()
font = pygame.font.SysFont("arial", 40)
pencere = pygame.display.set_mode((800, 600))
cubuk = pygame.Rect(375, 550, 80, 5)
renk = (255, 255, 255)
tuglalar = []
tugla_genislik = 75
tugla_yukseklik = 20
for satir in range(4):
    for sutun in range(10):
        x = sutun * (tugla_genislik + 5) + 15
        y = satir * (tugla_yukseklik + 5) + 50
        tuglalar.append(pygame.Rect(x, y, tugla_genislik, tugla_yukseklik))
saat = pygame.time.Clock()
oyun_bitti = False
kazandi = False

top_yaricap = 5
top_x = cubuk.centerx
top_y = cubuk.y - top_yaricap - 1
top_dx = 3
top_dy = -3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            oyun_bitti = False
            kazandi = False
            top_x = cubuk.centerx
            top_y = cubuk.y - top_yaricap - 1
            top_dx = 3
            top_dy = -3
            cubuk.x = 375
            tuglalar = []
            for satir in range(4):
                for sutun in range(10):
                    x = sutun * (tugla_genislik + 5) + 15
                    y = satir * (tugla_yukseklik + 5) + 50
                    tuglalar.append(pygame.Rect(x, y, tugla_genislik, tugla_yukseklik))

    kontroller = pygame.key.get_pressed()
    if kontroller[pygame.K_LEFT] or kontroller[pygame.K_a]:
        cubuk.x -= 5
    if kontroller[pygame.K_RIGHT] or kontroller[pygame.K_d]:
        cubuk.x += 5

    if cubuk.x < 0:
        cubuk.x = 0
    if cubuk.x > 800 - cubuk.width:
        cubuk.x = 800 - cubuk.width

    if not oyun_bitti:
        top_x += top_dx
        top_y += top_dy

        if top_x < top_yaricap or top_x > 800 - top_yaricap:
            top_dx *= -1
        if top_y < 50 + top_yaricap:
            top_dy *= -1
        top_rect = pygame.Rect(top_x - top_yaricap, top_y - top_yaricap, top_yaricap * 2, top_yaricap * 2)
        if cubuk.colliderect(top_rect):
            top_dy *= -1

        for tugla in tuglalar:
            if tugla.colliderect(top_rect):
                tuglalar.remove(tugla)
                top_dy *= -1
                break

        if len(tuglalar) == 0:
            oyun_bitti = True
            kazandi = True

        if top_y > 600:
            oyun_bitti = True
            kazandi = False

    pencere.fill((0, 0, 0))
    baslik = font.render("MY BREAKOUT CLONE ATTEMPT", True, (255, 255, 255))
    pencere.blit(baslik, baslik.get_rect(center=(400, 25)))
    pygame.draw.rect(pencere, renk, cubuk)
    for tugla in tuglalar:
        pygame.draw.rect(pencere, renk, tugla)
    pygame.draw.circle(pencere, renk, (top_x, top_y), top_yaricap)

    if oyun_bitti:
        if kazandi:
            yazi = font.render("Kazandın!", True, (255, 255, 255))
        else:
            yazi = font.render("Kaybettin!", True, (255, 255, 255))
        pencere.blit(yazi, yazi.get_rect(center=(400, 300)))

    bilgi = pygame.font.SysFont("arial", 15).render("R: Yeniden Başlat", True, (150, 150, 150))
    pencere.blit(bilgi, bilgi.get_rect(bottomright=(790, 590)))

    pygame.display.update()
    saat.tick(60)