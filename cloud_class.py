class Cloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
       pygame.sprite.Sprite.__init__(self,self.containers)

       #TODO : wstawic w miejsce "cloud.png" odpowiednie pliki
       self.image,self.rect = load_image('cloud.png',int(90*30/42),30,-1)
       self.speed = 1
       self.rect.left = x
       self.rect.top = y

       #dobór prędkości "ruchu" chmur względem ruchu dinozaura
       self.movement = [-1*self.speed,0]

    #funkcja wyświetlająca chmury na ekranie
    def draw(self):
       screen_layout_display.blit(self.image, self.rect)

    #funkcja odświeżająca sytuacje na ekranie
    def update(self):
       self.rect = self.rect.move(self.movement)
       
       #jeśli chmura wyleci poza obszar gry zostanie "zniszczona" w kodzie programu 
       if self.rect.right &lt; 0:
           self.kill()
