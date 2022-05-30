def load_sprite_sheet(
        s_name,
        namex,
        namey,
        scx = -1,
        scy = -1,
        c_key = None,
        ):
    fullname = os.path.join('resources', s_name)
    sh = pygame.image.load(fullname)
    sh = sh.convert()

    sh_rect = sh.get_rect()

    sprites = []

    sx = sh_rect.width/ namex
    sy = sh_rect.height/ namey

    for i in range(0, namey):
        for j in range(0, namex):
            rect = pygame.Rect((j*sx,i*sy,sx,sy))
            img = pygame.Surface(rect.size)
            img = img.convert()
            img.blit(sh,(0,0),rect)

            if c_key is not None:
                if c_key == -1:
                    c_key = img.get_at((0, 0))
                img.set_colorkey(c_key, RLEACCEL)

            if scx != -1 or scy != -1:
                img = pygame.transform.scale(img, (scx, scy))

            sprites.append(img)

    sprite_rect = sprites[0].get_rect()

    return sprites,sprite_rect