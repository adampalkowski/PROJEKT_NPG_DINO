import pygame
def gameplay():

    global highest_scores
    gp = 4
    s_Menu = False
    g_Over = False
    g_exit = False
    while not g_exit:
        while s_Menu:
            pass
        while not g_Over:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                g_exit = True
                g_Over = True
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        g_exit = True
                        g_Over = True
        if g_exit:
            break
    while g_Over:
        if pygame.display.get_surface() == None:
            print("Couldn't load display surface")
            g_exit = True
            g_Over = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g_exit = True
                    g_Over = False

    pygame.quit()
    quit()

def main():
    isGameQuit = introduction_screen()
    if not isGameQuit:
        gameplay()