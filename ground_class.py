class Ground():<br>
  def __init__(self,speed=-5):<br>
    self.image,self.rect = load_image('ground.png',-1,-1,-1)<br>
    
    self.image1,self.rect1 = load_image('ground.png',-1,-1,-1)<br>
    
    self.rect.bottom = height_screen<br>
    
    self.rect1.bottom = height_screen<br>
    
    self.rect1.left = self.rect.right<br>
    
    self.speed = speed<br><br>
  
  def draw(self):<br>
      screen_layout_display.blit(self.image, self.rect)<br>
      
      screen_layout_display.blit(self.image1, self.rect1)<br><br>
  
  def update(self):<br>
        self.rect.left += self.speed<br>
        
        self.rect1.left += self.speed<br><br>
        
        if self.rect.right &lt; 0:<br>
          self.rect.left = self.rect1.right<br><br>
          
          if self.rect1.right &lt; 0:<br>
            self.rect1.left = self.rect.right
