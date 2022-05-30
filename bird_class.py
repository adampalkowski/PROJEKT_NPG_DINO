class birds(pygame.sprite.Sprite):<br>    

def __init__(self, speed=5, sx=-1, sy=-1):<br>        
    pygame.sprite.Sprite.__init__(self,self.containers)<br>        
    self.imgs, self.rect = load_sprite_sheet('birds.png', 2, 1, sx, sy, -1)<br>        
    self.birds_height = [height_screen * 0.82, height_screen * 0.75, height_screen * 0.60]<br>        
    self.rect.centery = self.birds_height[random.randrange(0, 3)]<br>        
    self.rect.left = width_screen + self.rect.width<br>        
    self.image = self.imgs[0]<br>        
    self.movement = [-1*speed,0]<br>        
    self.index = 0<br>        
    self.counter = 0<br><br>    

def draw(self):<br>        
    screen_layout_display.blit(self.image, self.rect)<br><br>    

def update(self):<br>        
    if self.counter % 10 == 0:<br>            
      self.index = (self.index+1)%2<br>        
      self.image = self.imgs[self.index]<br>        
      self.rect = self.rect.move(self.movement)<br>        
      self.counter = (self.counter + 1)<br>        
    
    if self.rect.right &lt; 0:<br>            
      self.kill()<br>
