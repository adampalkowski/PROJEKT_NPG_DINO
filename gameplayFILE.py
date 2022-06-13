def gameplay():

    global highest_scores
    gp = 4
    #stworz obiekt dino
    gamer_Dino = Dino(44,47)


    s_Menu = False
    g_Over = False
    g_exit = False
    new_grnd = Ground(-1 * gp)
    score_boards = Scoreboard()
    highScore = Scoreboard(width_screen * 0.78)
    counter = 0

    cactusan = pygame.sprite.Group()
    smallBird = pygame.sprite.Group()
    skyClouds = pygame.sprite.Group()
    last_end_obs = pygame.sprite.Group()

    Cactus.containers = cactusan
    birds.containers = smallBird
    Cloud.containers = skyClouds

    #załaduj obrazy
    rbtn_image,rbtn_rect = load_image('replay_button.png',35,31,-1)
    gmo_image,gmo_rect = load_image('game_over.png',190,11,-1)
    t_images,t_rect = load_sprite_sheet('numbers.png',12,1,11,int(11*6/5),-1)
    ado_image = pygame.Surface((22,int(11*6/5)))
    ado_rect = ado_image.get_rect()
    ado_image.fill(bg_color)
    ado_image.blit(t_images[10],t_rect)
    t_rect.left += t_rect.width
    ado_image.blit(t_images[11],t_rect)
    ado_rect.top = height_screen * 0.1
    ado_rect.left = width_screen * 0.73

    #głowna pętla
    while not g_exit:
        while s_Menu:
            pass
        while not g_Over:

            if pygame.display.get_surface() == None:
                print("Nie da rady załadować powieszchni")
                g_exit = True
                g_Over = True
            else:
                #kontrol przycisków
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        g_exit = True
                        g_Over = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if gamer_Dino.rect.bottom == int(0.98 * height_screen):
                                gamer_Dino.jumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                gamer_Dino.movement[1] = -1 * gamer_Dino.jumpSpeed

                        if event.key == pygame.K_DOWN:
                            if not (gamer_Dino.jumping and gamer_Dino.dead):
                                gamer_Dino.ducking = True

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            gamer_Dino.ducking = False
            #poruszanie się kaktusów
            for c in cactusan:
                c.movement[0] = -1 * gp
                if pygame.sprite.collide_mask(gamer_Dino, c):
                    gamer_Dino.dead = True
                    if pygame.mixer.get_init() != None:
                        die_sound.play()
            #poruszanie się ptaków
            for p in smallBird:
                p.movement[0] = -1 * gp
                if pygame.sprite.collide_mask(gamer_Dino, p):
                    gamer_Dino.dead = True
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            if len(cactusan) < 2:
                if len(cactusan) == 0:
                    last_end_obs.empty()
                    last_end_obs.add(Cactus(gp, 40, 40))
                else:
                    for l in last_end_obs:
                        if l.rect.right < width_screen * 0.7 and random.randrange(0, 50) == 10:
                            last_end_obs.empty()
                            last_end_obs.add(Cactus(gp, 40, 40))

            if len(smallBird) == 0 and random.randrange(0, 200) == 10 and counter > 500:
                for l in last_end_obs:
                    if l.rect.right < width_screen * 0.8:
                        last_end_obs.empty()
                        last_end_obs.add(birds(gp, 46, 40))

            if len(skyClouds) < 5 and random.randrange(0, 300) == 10:
                Cloud(width_screen, random.randrange(height_screen / 5, height_screen / 2))


            #odświerzenie elementów
            gamer_Dino.update()
            cactusan.update()
            smallBird.update()
            skyClouds.update()
            new_grnd.update()
            score_boards.update(gamer_Dino.score)
            highScore.update(highest_scores)

            if pygame.display.get_surface() != None:
                screen_layout_display.fill(bg_color)
                new_grnd.draw()
                skyClouds.draw(screen_layout_display)
                score_boards.draw()
                if highest_scores != 0:
                    highScore.draw()
                    screen_layout_display.blit(ado_image, ado_rect)
                cactusan.draw(screen_layout_display)
                smallBird.draw(screen_layout_display)
                gamer_Dino.draw()

                pygame.display.update()
            time_clock.tick(FPS)

            if gamer_Dino.dead:
                g_Over = True
                if gamer_Dino.score > highest_scores:
                    highest_scores = gamer_Dino.score

            if counter % 700 == 699:
                new_grnd.speed -= 1
                gp += 1

            counter = (counter + 1)

        if g_exit:
            break

    while g_Over:
        if pygame.display.get_surface() == None:
            print("Nie można załadować powieszchni")
            g_exit = True
            g_Over = False
        else:

            #kontrola naciśniętych przycisków
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g_exit = True
                    g_Over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        g_exit = True
                        g_Over = False

                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        g_Over = False
                        gameplay()

        #tutaj ważny update wyniku
        highScore.update(highest_scores)
        if pygame.display.get_surface() != None:
            gameover_display_message(rbtn_image, gmo_image)
            if highest_scores != 0:
                highScore.draw()
                screen_layout_display.blit(ado_image, ado_rect)
            pygame.display.update()
        time_clock.tick(FPS)

>>>>>>> 5906e47 (update)

    pygame.quit()
    quit()

def main():

    isGameQuit = introduction_screen()

    if not isGameQuit:
        gameplay()

main()
