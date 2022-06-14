# fucnkcja zajmująca się wczytywaniem obrazu

def load_image(
  
name,
sx=-1,
sy=-1,
colorkey=None,
):

#Wczytywanie danych modeli  

fullname = os.path.join('resources', name)
img = pygame.image.load(fullname)
img = img.convert()

if colorkey is not None:
  if colorkey == -1:
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey, RLEACCEL)

    if sx != -1 or sy != -1:
        img = pygame.transform.scale(img, (sx, sy))

return (img, img.get_rect())
