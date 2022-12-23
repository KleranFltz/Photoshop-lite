# Kieran Fitzgerald 101276562

# negated inverted colour is the difference between the given rgb value, and it's maximum possibility
#example (200,100,55)
#becomes (55,155,200)
"""
• read about pygame's "image.load"1, "mouse.get_pressed", and "mouse.get_pos" functions2
• read about the pygame Surface methods "get_size", "blit", "get_at", and "set_at"3
• choose whether you would like to implement a simple "negation" effect (below left)...
- or if you would prefer something more impressive, like "blur", "sharpen", or "edge detect"4

• must be a source code file with filename 'comp1405_f22_#########_assignment_07.py'
• must initialize pygame, load image specified by the user, and use get_size to find its dimensions
• must create a window that is the correct size and then "blit" the loaded image
• must use the loop (below right) to repeatedly get input, apply the effect, and update the display
• must permit the user to use the mouse to specify a region of the image (i.e., by clicking)5
• must use nested loops, "get_at", and "set_at" to apply an effect to the region the user selected
"""

import pygame
import sys

pygame.init()

src = sys.argv[1]

img = pygame.image.load(src)

dimensions = pygame.Surface.get_size(img)

win = pygame.display.set_mode(dimensions) 

pygame.Surface.blit(win,img,(0,0))

pygame.display.update()

x1 = 0
y1 = 0
x2 = 0
y2 = 0
clicks = 2
exit_flag = False


while not exit_flag:
    # loop body goes here
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONDOWN:

        if pygame.mouse.get_pressed() == (1,0,0) and (clicks % 2) == 0:
            (x1,y1) = pygame.mouse.get_pos()
            print(x1,y1,"1")
        
        elif pygame.mouse.get_pressed() == (1,0,0) and (clicks % 2) == 1:
            (x2,y2) = pygame.mouse.get_pos()
            print(x2,y2,"2")


            if (x1 < x2) and (y1 < y2):
                height = y2 - y1
                width = x2 - x1
                for y in range(height):
                    for x in range(width):
                        (r,g,b,_) = pygame.Surface.get_at(win,(x+x1,y+y1))
                        r = 255 - r
                        g = 255 - g
                        b = 255 - b

                        pygame.Surface.set_at(win,(x+x1,y+y1),(r,g,b))

            elif (x1 > x2) and (y1 > y2):
                height = y1 - y2
                width = x1 - x2
                for y in range(height):
                    for x in range(width):
                        (r,g,b,_) = pygame.Surface.get_at(win,(x+x2,y+y2))
                        r = 255 - r
                        g = 255 - g
                        b = 255 - b

                        pygame.Surface.set_at(win,(x+x2,y+y2),(r,g,b))

            elif (x1 < x2) and (y1 > y2):
                height = y1 - y2
                width = x2 - x1
                for y in range(height):
                    for x in range(width):
                        (r,g,b,_) = pygame.Surface.get_at(win,(x+x1,y+y2))
                        r = 255 - r
                        g = 255 - g
                        b = 255 - b

                        pygame.Surface.set_at(win,(x+x1,y+y2),(r,g,b))
            
            else:
                height = y2 - y1
                width = x1 - x2
                for y in range(height):
                    for x in range(width):
                        (r,g,b,_) = pygame.Surface.get_at(win,(x+x2,y+y1))
                        r = 255 - r
                        g = 255 - g
                        b = 255 - b

                        pygame.Surface.set_at(win,(x+x2,y+y1),(r,g,b))

            pygame.display.update()
        
        clicks = clicks + 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit_flag = True