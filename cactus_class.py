class Cactus(pygame.sprite.Sprite):
     def __init__(self, speed=5, sx=-1, sy=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        #TODO : wstawic w miejsce "cactus-small.png" odpowiednie pliki
        self.imgs, self.rect = load_sprite_sheet('cactus-small.png', 3, 1, sx, sy, -1)
        self.rect.bottom = int(0.98 * height_screen)
        self.rect.left = width_screen + self.rect.width
        #losowanie typu kaktusa, który się pojawi
        self.image = self.imgs[random.randrange(0, 3)]
        self.movement = [-1*speed,0]
     
     #funkcja wyświetlająca kaktusy na ekranie
     def draw(self):
        screen_layout_display.blit(self.image, self.rect)

     #funkcja odświeżająca sytuacje na ekranie
     def update(self):
        self.rect = self.rect.move(self.movement)

     #jeśli kaktus wyjedzie poza obszar gry zostanie "zniszczony" w kodzie programu
     if self.rect.right &lt; 0:
        self.kill()
