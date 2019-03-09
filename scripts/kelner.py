
# kelner object

# coordinates x y global

# dictionaries with

# movement procedures stolen from Elsa

import pygame, sys
class Kelner(pygame.sprite.Sprite):
    def __init__(self, x, y, window_width, window_height, walls):
        pygame.sprite.Sprite.__init__(self)

        self.window_width = window_width
        self.window_height = window_height

        # Set height, width
        self.image = pygame.image.load("images/elsa.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.step = 50

        self.walls = walls

        self.jump_sound = pygame.mixer.Sound('sounds/jump.wav')
        self.clang_sound = pygame.mixer.Sound('sounds/clang.wav')

    def move_right(self):
        if self.rect.x + self.rect.width + self.step <= self.window_width:
            self.rect.x += self.step
            collision = False
            for wall in self.walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.x -= self.step
                    collision = True
                    break
            if collision:
                self.clang_sound.play()
            else:
                self.jump_sound.play()


    def move_left(self):
        if self.rect.x >= self.step:
            self.rect.x -= self.step
            collision = False
            for wall in self.walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.x += self.step
                    collision = True
                    break
            if collision:
                self.clang_sound.play()
            else:
                self.jump_sound.play()

    def move_down(self):
        if self.rect.y + self.rect.height + self.step <= self.window_height:
            self.rect.y += self.step
            collision = False
            for wall in self.walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.y -= self.step
                    collision = True
                    break
            if collision:
                self.clang_sound.play()
            else:
                self.jump_sound.play()

    def move_up(self):
        if self.rect.y >= self.step:
            self.rect.y -= self.step
            collision = False
            for wall in self.walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.y += self.step
                    collision = True
                    break
            if collision:
                self.clang_sound.play()
            else:
                self.jump_sound.play()


    def reset(self):
        self.rect.x = 0
        self.rect.y = 0

