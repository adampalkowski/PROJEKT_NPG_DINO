# fucnkcja zajmująca się wczytywaniem obrazu

def load_image(
  
name,
sx=-1,
sy=-1,
colorkey=None,
):

fullname = os.path.join('resources', name)
img = pygame.image.load(fullname)
img = img.convert()
