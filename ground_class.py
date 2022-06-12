class Ground():<br>
  def __init__(self,speed=-5):<br>
    #TODO : wstawic w miejsce "ground.png" odpowiednie pliki
    self.image,self.rect = load_image('ground.png',-1,-1,-1)<br>
    
    #TODO : wstawic w miejsce "ground.png" odpowiednie pliki
    self.image1,self.rect1 = load_image('ground.png',-1,-1,-1)<br>
    
    #wybór wysokości na której jest grunt (tzw. poziom zero po którym biegnie Dino)
    self.rect.bottom = height_screen<br>
    self.rect1.bottom = height_screen<br>
    
    self.rect1.left = self.rect.right<br>
    
    self.speed = speed<br><br>
  
  #funkcja wyświetlająca podłoże na ekranie
  def draw(self):<br>
      screen_layout_display.blit(self.image, self.rect)<br>
      
      screen_layout_display.blit(self.image1, self.rect1)<br><br>
  
  #funkcja odświeżająca sytuacje na ekranie
  def update(self):<br>
        self.rect.left += self.speed<br>
        
        self.rect1.left += self.speed<br><br>
        
        if self.rect.right &lt; 0:<br>
          self.rect.left = self.rect1.right<br><br>
          
        if self.rect1.right &lt; 0:<br>
          self.rect1.left = self.rect.right
