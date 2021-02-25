import pygame


def dr_p(screen):

    dr_p_ec(screen)
    dr_p_te(screen)
    dr_p_cn(screen)


def dr_p_cn(screen):

    pygame.draw.rect(screen, "orange", (895, 550, 201, 45), 0)
    screen.blit(pygame.font.Font(None, 69).render("ИГРАТЬ!", True, "blue"), (895, 550))

    pygame.draw.rect(screen, "orange", (5, 550, 158, 45), 0)
    screen.blit(pygame.font.Font(None, 69).render("МЕНЮ", True, "blue"), (5, 550))


def dr_p_te(screen):
    s0 = "Всего на поле 2 игрока."
    s1 = "Первый игрок управляется при помощиклавишь a, w, d и s,"
    s2 = "а второй при помощи стрелочек."
    s3 = "При соприкасновении мяча и игрока, мяч получает импульс"
    s4 = "с направлением движения игрока."
    s5 = "ПРИМЕЧАНИЯ:"
    s6 = "Мяч пролитает сквозь стоящего игрока."

    screen.blit(pygame.font.Font(None, 50).render(s0, True, (0, 0, 0)), (5, 100))
    screen.blit(pygame.font.Font(None, 50).render(s1, True, (0, 0, 0)), (5, 150))
    screen.blit(pygame.font.Font(None, 50).render(s2, True, (0, 0, 0)), (5, 200))
    screen.blit(pygame.font.Font(None, 50).render(s3, True, (0, 0, 0)), (5, 250))
    screen.blit(pygame.font.Font(None, 50).render(s4, True, (0, 0, 0)), (5, 300))
    screen.blit(pygame.font.Font(None, 50).render(s5, True, (0, 0, 0)), (5, 380))
    screen.blit(pygame.font.Font(None, 50).render(s6, True, (0, 0, 0)), (5, 430))


def dr_p_ec(screen):
    screen.fill((0, 255, 0))
    pygame.draw.rect(screen, (75, 255, 75), (50, 50, 166, 501), 0)
    pygame.draw.rect(screen, (75, 255, 75), (382, 50, 166, 501), 0)
    pygame.draw.rect(screen, (75, 255, 75), (719, 50, 166, 501), 0)

    pygame.draw.line(screen, (255, 255, 255), (551, 50), (551, 551), 5)
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(47, 47), (1054, 47), (1054, 554), (47, 554), (47, 47)], 5)

    pygame.draw.circle(screen, (255, 255, 255), (551, 301), 100)
    pygame.draw.circle(screen, (0, 255, 0), (551, 301), 95)
    pygame.draw.circle(screen, (255, 255, 255), (551, 301), 10)

    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(47, 225), (17, 225), (17, 376), (47, 376)], 5)
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(1054, 225), (1084, 225), (1084, 376), (1054, 376)], 5)


def dr_z_ec(screen):
    screen.fill((0, 255, 0))
    pygame.draw.rect(screen, (75, 255, 75), (50, 50, 166, 501), 0)
    pygame.draw.rect(screen, (75, 255, 75), (382, 50, 166, 501), 0)
    pygame.draw.rect(screen, (75, 255, 75), (719, 50, 166, 501), 0)

    pygame.draw.line(screen, (255, 255, 255), (551, 50), (551, 551), 5)
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(47, 47), (1054, 47), (1054, 554), (47, 554), (47, 47)], 5)

    pygame.draw.circle(screen, (255, 255, 255), (551, 301), 100)
    pygame.draw.circle(screen, (0, 255, 0), (551, 301), 95)
    pygame.draw.circle(screen, (255, 255, 255), (551, 301), 10)

    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(47, 225), (17, 225), (17, 376), (47, 376)], 5)
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(1054, 225), (1084, 225), (1084, 376), (1054, 376)], 5)


def dr_z(screen):

    dr_z_ec(screen)
    dr_z_na(screen)
    dr_z_cn(screen)


def dr_z_na(screen):

    screen.blit(pygame.font.Font(None, 100).render("ВЕСЁЛЫЙ ФУТБОЛ!!!", True, "blue"), (180, 100))


def dr_z_cn(screen):

    pl = 250

    pygame.draw.rect(screen, "orange", (450, pl, 201, 45), 0)
    screen.blit(pygame.font.Font(None, 69).render("ИГРАТЬ!", True, "blue"), (450, pl))

    pygame.draw.rect(screen, "orange", (432, pl + 65, 237, 45), 0)
    screen.blit(pygame.font.Font(None, 69).render("ПРАВИЛА", True, "blue"), (432, pl + 65))


def dr(screen):

    dr_pol(screen)
    dr_boll(screen)
    dr_plrs(screen)


def dr_plrs(screen):

    global n0
    global n1
    global fp00
    global fp01
    global fp02
    global fp03
    global fp10
    global fp11
    global fp12
    global fp13

    pygame.draw.rect(screen, (0, 0, 255), (n0[0] - 10, n0[1] - 40, 20, 25), 0)
    pygame.draw.rect(screen, (0, 0, 255), (n0[0] - 10, n0[1] + 15, 20, 25), 0)
    pygame.draw.circle(screen, (0, 0, 255), (n0[0], n0[1] - 40), 10)
    pygame.draw.circle(screen, (0, 0, 255), (n0[0], n0[1] + 40), 10)
    pygame.draw.circle(screen, "brown", (n0[0], n0[1]), 25)

    pygame.draw.rect(screen, (255, 0, 0), (n1[0] - 10, n1[1] - 40, 20, 25), 0)
    pygame.draw.rect(screen, (255, 0, 0), (n1[0] - 10, n1[1] + 15, 20, 25), 0)
    pygame.draw.circle(screen, (255, 0, 0), (n1[0], n1[1] - 40), 10)
    pygame.draw.circle(screen, (255, 0, 0), (n1[0], n1[1] + 40), 10)
    pygame.draw.circle(screen, "yellow", (n1[0], n1[1]), 25)


def dr_boll(screen):

    global n0
    global n1
    global n

    pygame.draw.circle(screen, "orange", (n[0], n[1]), 15)


def dr_pol(screen):

    global count0
    global count1

    screen.fill((0, 255, 0))
    pygame.draw.rect(screen, (75, 255, 75), (50, 50, 166, 501), 0)
    pygame.draw.rect(screen, (75, 255, 75), (382, 50, 166, 501), 0)
    pygame.draw.rect(screen, (75, 255, 75), (719, 50, 166, 501), 0)

    pygame.draw.line(screen, (255, 255, 255), (551, 50), (551, 551), 5)
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(47, 47), (1054, 47), (1054, 554), (47, 554), (47, 47)], 5)

    pygame.draw.circle(screen, (255, 255, 255), (551, 301), 100)
    pygame.draw.circle(screen, (0, 255, 0), (551, 301), 95)
    pygame.draw.circle(screen, (255, 255, 255), (551, 301), 10)

    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(47, 225), (17, 225), (17, 376), (47, 376)], 5)
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(1054, 225), (1084, 225), (1084, 376), (1054, 376)], 5)

    screen.blit(pygame.font.Font(None, 70).render(str(count1), True, (0, 0, 0)), (500, 0))
    screen.blit(pygame.font.Font(None, 70).render(str(count0), True, (0, 0, 0)), (580, 0))


def counter(screen):

    counter_go()
    counter_r()
    counter_st_pl()
    ceunter_boll()


def counter_st_pl():

    global n0
    global n1
    global n
    global m0
    global m1
    global m2
    global m3
    global fp00
    global fp01
    global fp02
    global fp03
    global fp10
    global fp11
    global fp12
    global fp13
    global s
    global c

    if n1[1] - 60 < n0[1] < n1[1] + 60:
        if 0 <= n0[0] - n1[0] < 60:
            n0[0] = n0[0] + 1
            n1[0] = n1[0] - 1
        if 0 < n1[0] - n0[0] < 60:
            n0[0] = n0[0] - 1
            n1[0] = n1[0] + 1


def counter_r():

    if n0[0] > 1027:
        n0[0] = n0[0] - 1
    if n0[0] < 75:
        n0[0] = n0[0] + 1
    if n1[0] > 1027:
        n1[0] = n1[0] - 1
    if n1[0] < 75:
        n1[0] = n1[0] + 1
    if n0[1] > 527:
        n0[1] = n0[1] - 1
    if n0[1] < 75:
        n0[1] = n0[1] + 1
    if n1[1] > 527:
        n1[1] = n1[1] - 1
    if n1[1] < 75:
        n1[1] = n1[1] + 1


def counter_go():

    global n0
    global n1
    global n
    global m0
    global m1
    global m2
    global m3
    global fp00
    global fp01
    global fp02
    global fp03
    global fp10
    global fp11
    global fp12
    global fp13
    global s
    global c

    if fp00 == 1:
        n0[1] = n0[1] - 1
    if fp01 == 1:
        n0[0] = n0[0] + 1
    if fp02 == 1:
        n0[1] = n0[1] + 1
    if fp03 == 1:
        n0[0] = n0[0] - 1

    if fp10 == 1:
        n1[1] = n1[1] - 1
    if fp11 == 1:
        n1[0] = n1[0] + 1
    if fp12 == 1:
        n1[1] = n1[1] + 1
    if fp13 == 1:
        n1[0] = n1[0] - 1


def ceunter_boll():

    global n0
    global n1
    global n
    global m0
    global m1
    global m2
    global m3
    global fp00
    global fp01
    global fp02
    global fp03
    global fp10
    global fp11
    global fp12
    global fp13
    global s
    global c
    global cp
    global count0
    global count1

    if c != -1:
        if m0 > 0:
            n[1] = n[1] - s[c]
        if m1 > 0:
            n[0] = n[0] + s[c]
        if m2 > 0:
            n[1] = n[1] + s[c]
        if m3 > 0:
            n[0] = n[0] - s[c]

        c = c + 1
        if c == len(s):
            m0 = 0
            m1 = 0
            m2 = 0
            m3 = 0
            c = -1

    if n0[0] - 50 < n[0] < n0[0] + 50 and \
            n0[1] - 50 < n[1] < n0[1] + 50:
        if fp00 == 1:
            c = 0
            m0 = 1
        if fp01 == 1:
            m1 = 1
            c = 0
        if fp02 == 1:
            m2 = 1
            c = 0
        if fp03 == 1:
            m3 = 1
            c = 0

    if n1[0] - 50 < n[0] < n1[0] + 50 and \
            n1[1] - 50 < n[1] < n1[1] + 50:
        if fp10 == 1:
            c = 0
            m0 = 1
        if fp11 == 1:
            m1 = 1
            c = 0
        if fp12 == 1:
            m2 = 1
            c = 0
        if fp13 == 1:
            m3 = 1
            c = 0

    if 225 <= n[1] <= 376 and 48 <= n[0] <= 51:
        count1 = count1 + 1
        n0, n1, n = [150, 301], [951, 301], [551, 301]
        c = -1
    if 225 <= n[1] <= 376 and 1050 <= n[0] <= 1053:
        count0 = count0 + 1
        n0, n1, n = [150, 301], [951, 301], [551, 301]
        c = -1

    if count0 == 9 or count1 == 9:
        n0, n1, n = [150, 301], [951, 301], [551, 301]
        count1 = count0 = 0
        c = -1
        cp = 0

    if 47 > n[0] or n[0] > 1054:
        m1, m3 = m3, m1
    if 47 > n[1] or n[1] > 554:
        m0, m2 = m2, m0


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('2')
    size = width, height = 1101, 601
    screen = pygame.display.set_mode(size)

    running = True
    c = -1
    s = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    m0, m1, m2, m3 = 0, 0, 0, 0
    n0, n1, n = [150, 301], [951, 301], [551, 301]
    fp00, fp01, fp02, fp03 = 0, 0, 0, 0
    fp10, fp11, fp12, fp13 = 0, 0, 0, 0
    count0, count1 = 0, 0
    cp = 0

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                p = [i for i in event.pos]

                if cp == 0:
                    if 450 <= p[0] <= 651 and 250 < p[1] < 295:
                        cp = 1

                    if 432 <= p[0] <= 669 and 315 < p[1] < 360:
                        cp = 2

                if cp == 2:
                    if 550 <= p[1] <= 595 and 895 < p[0] < 1096:
                        cp = 1

                    if 550 <= p[1] <= 595 and 5 < p[0] < 163:
                        cp = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    fp10 = 1
                if event.key == pygame.K_RIGHT:
                    fp11 = 1
                if event.key == pygame.K_DOWN:
                    fp12 = 1
                if event.key == pygame.K_LEFT:
                    fp13 = 1
                if event.key == pygame.K_w:
                    fp00 = 1
                if event.key == pygame.K_d:
                    fp01 = 1
                if event.key == pygame.K_s:
                    fp02 = 1
                if event.key == pygame.K_a:
                    fp03 = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    fp10 = 0
                if event.key == pygame.K_RIGHT:
                    fp11 = 0
                if event.key == pygame.K_DOWN:
                    fp12 = 0
                if event.key == pygame.K_LEFT:
                    fp13 = 0
                if event.key == pygame.K_w:
                    fp00 = 0
                if event.key == pygame.K_d:
                    fp01 = 0
                if event.key == pygame.K_s:
                    fp02 = 0
                if event.key == pygame.K_a:
                    fp03 = 0
        if cp == 0:
            dr_z(screen)
        if cp == 1:
            counter(screen)
            dr(screen)
        if cp == 2:
            dr_p(screen)
        pygame.display.flip()
    pygame.quit()
