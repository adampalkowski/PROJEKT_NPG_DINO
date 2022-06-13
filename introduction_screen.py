def introduction_screen():
    #stwórz dino
    ado_dino = Dino(44,47)
    ado_dino.blinking = True
    starting_game = False

    #załadowanie ekranu i ustawienie tła
    t_ground,t_ground_rect = load_sprite_sheet('ground.png',15,1,-1,-1,-1)
    t_ground_rect.left = width_screen / 20
    t_ground_rect.bottom = height_screen

    logo,l_rect = load_image('logo.png',300,140,-1)
    l_rect.centerx = width_screen * 0.6
    l_rect.centery = height_screen * 0.6

    #pętla czekająca na rozpoczęcie gry
    while not starting_game:

        #przypadek gdy nie można załadować surface
        if pygame.display.get_surface() == None:
            print("Couldn't load display surface")
            return True
        else:
            #w przypadku naciśnięcia klawiszy
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        ado_dino.jumping = True
                        ado_dino.blinking = False
                        ado_dino.movement[1] = -1*ado_dino.jumpSpeed

        ado_dino.update()

        if pygame.display.get_surface() != None:
            #ustaw tło
            screen_layout_display.fill(bg_color)
            screen_layout_display.blit(t_ground[0], t_ground_rect)
            if ado_dino.blinking:
                screen_layout_display.blit(logo, l_rect)

            ado_dino.draw()

            pygame.display.update()

        time_clock.tick(FPS)
        if ado_dino.jumping == False and ado_dino.blinking == False:
            starting_game = True
