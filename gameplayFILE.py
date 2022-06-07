import pygame
def gameplay():

    global highest_scores
    gp = 4

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




    while not g_exit:
        while s_Menu:
            pass
        while not g_Over:

            if pygame.display.get_surface() == None:
                print("Nie da rady załadować powieszchni")
                g_exit = True
                g_Over = True
            else:

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



            if pygame.display.get_surface() != None:
                pygame.display.update()



        if g_exit:

            break

    while g_Over:


        if pygame.display.get_surface() == None:
            g_exit = True
            g_Over = False
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g_exit = True
                    g_Over = False

                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_SPACE:
                          if gamer_Dino.rect.bottom == int(0.98 * height_screen):
                                gamer_Dino.jumping = True
                                if pygame.mixer.get_init() != None:
                                   #todo dodaj dzwiek skoku
                                #todo zmien predkosc dino

                    if event.type == pygame.KEYDOWN:
                        if not (gamer_Dino.jumping and gamer_Dino.dead):
                                gamer_Dino.ducking = True
                    if event.key == pygame.K_ESCAPE:
                        g_exit = True
                        g_Over = False

                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        g_Over = False
                        gameplay()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                          gamer_Dino.ducking = False



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