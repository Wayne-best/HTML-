import random
import pygame


class Button():
    def __int __(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos
        
        def clicked(self, pos):
            if self.pos = pygame.mouse.get_pos()
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
            return False
        
        
        
        class RpsGame():
            self.pos = pygame.mouse.get_pos()
            def __init __(self):
                pygame.init()
                
                self.screen = pygame.display.set_mode((960,640))
                pygame.display.set_caption
                