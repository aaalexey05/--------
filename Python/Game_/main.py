import pygame
from Config import *
from ClassLevel import Level

# Init
pygame.init()
clock = pygame.time.Clock()

# Open windiw
displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("MagicForest")



level = Level(displaySurface)


isGamingRunning = True
while isGamingRunning:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGamingRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isGamingRunning = False
                
            
    level.run()
    
    pygame.display.flip()
    clock.tick(60)
    
# Close pygame
pygame.quit()
