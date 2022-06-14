class Dino():
    def __init__(self, sx=-1, sy=-1):
        # wynik dino

        self.score = 0
        self.image = self.imgs[0]
        # todo : wstawic tutaj .png pliki
        self.imgs, self.rect = load_sprite_sheet()
        # todo : wstawic tutaj .png pliki
        self.imgs1, self.rect1 = load_sprite_sheet()
        self.rect.bottom = int(0.98 * height_screen)
        self.rect.left = width_screen / 15
        self.index = 0
        self.counter = 0
        # musimy wiedziec czy dino jest w skoku
        self.jumping = False

        # musimy wiedziec czy dino żyje
        self.dead = False
        # musimy wiedziec czy dino kuca
        self.ducking = False
        self.blinking = False
        self.movement = [0, 0]
        # tymczasowa prędkosc
        self.jumpSpeed = 11.5

        self.stand_position_width = self.rect.width
        self.duck_position_width = self.rect1.width
        self.imgs, self.rect = load_sprite_sheet('dino.png', 5, 1, sx, sy, -1)
        self.imgs1, self.rect1 = load_sprite_sheet('dino_ducking.png', 2, 1, 59, sy, -1)
        self.rect.bottom = int(0.98 * height_screen)
        self.rect.left = width_screen / 15

    # funkcja pokazujaca dino na ekranie
    def draw(self):
        screen_layout_display.blit(self.image, self.rect)

    # funkcja odpowiadajaca za nie wykroczenie dino poza wyznaczone pole
    def checkbounds(self):
        if self.rect.bottom > int(0.98 * height_screen):
            self.rect.bottom = int(0.98 * height_screen)
            self.jumping = False

    # funkcja ktora bedzie odswieżac pozycje dino oraz licznik
    def update(self):

        if self.jumping:
            self.movement[1] = self.movement[1] + gravity

        if self.jumping:
            self.index = 0
        elif self.blinking:
            if self.index == 0:
                if self.counter % 400 == 399:
                    self.index = (self.index + 1) % 2
            else:
                if self.counter % 20 == 19:
                    self.index = (self.index + 1) % 2
        elif self.ducking:
            if self.counter % 5 == 0:
                self.index = (self.index + 1) % 2
        else:
            if self.counter % 5 == 0:
                self.index = (self.index + 1) % 2 + 2

        if self.dead:
            self.index = 4

        if not self.ducking:
            self.image = self.imgs[self.index]
            self.rect.width = self.stand_position_width
        else:
            self.image = self.imgs1[(self.index) % 2]
            self.rect.width = self.duck_position_width

        self.rect = self.rect.move(self.movement)
        self.checkbounds()

        if not self.dead and self.counter % 7 == 6 and self.blinking == False:
            self.score += 1
            if self.score % 100 == 0 and self.score != 0:
                if pygame.mixer.get_init() != None:
                    checkPoint_sound.play()

        self.counter = (self.counter + 1)
