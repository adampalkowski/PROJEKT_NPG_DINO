class Dino():
    def __init__(self, sx=-1, sy=-1):
        #wynik dino
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
      #musimy wiedziec czy dino jest w skoku
        self.jumping = False

      # musimy wiedziec czy dino żyje
        self.dead = False
    # musimy wiedziec czy dino kuca
        self.ducking = False
        self.blinking = False
        self.movement = [0,0]
        #tymczasowa prędkosc
        self.jumpSpeed = 11.5


 #funkcja pokazujaca dino na ekranie
    def draw(self):
        screen_layout_display.blit(self.image, self.rect)


#funkcja odpowiadajaca za nie wykroczenie dino poza wyznaczone pole
    def checkbounds(self):
        if self.rect.bottom > int(0.98 * height_screen):
            self.rect.bottom = int(0.98 * height_screen)
            self.jumping = False

    #funkcja ktora bedzie odswieżac pozycje dino oraz licznik
    def update(self):

        if self.jumping:
            self.movement[1] = self.movement[1] + gravity

        if self.jumping:
            self.index = 0
        elif self.blinking:
            if self.index == 0:
                if self.counter % 400 == 399:
                    self.index = (self.index + 1)%2
            else:
                if self.counter % 20 == 19:
                    self.index = (self.index + 1)%2



        if self.dead:
            self.index = 4




        self.checkbounds()
        self.counter = (self.counter + 1)