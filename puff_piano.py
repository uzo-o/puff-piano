"""
name: puff_piano.py
author: Uzo Ukekwe
version: python 3.8
purpose: creates a piano made of puff puff for the user to play
"""

import pygame

# initialize pygame and pygame mixer
pygame.init()
pygame.mixer.init(channels=8)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
channel5 = pygame.mixer.Channel(4)
channel6 = pygame.mixer.Channel(5)
channel7 = pygame.mixer.Channel(6)
channel8 = pygame.mixer.Channel(7)

# set up window
size = (1300, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Puff Piano")
background_image = pygame.image.load("images/bg.gif").convert()
screen.blit(background_image, [0, 0])


def sing(channel, note_file):
    """
    Play a note
    :param channel: audio channel for note sung by puff puff
    :param note_file: name of audio file that will play
    """
    channel.play(pygame.mixer.Sound(note_file), -1)


class Puff(pygame.sprite.Sprite):
    """
    Puff represents a single puff puff pastry/piano key.
    """
    def __init__(self, pos_x, pos_y):
        """
        Initialize sleeping puff puff.
        :param pos_x: starting x-coordinate of the puff puff
        :param pos_y: starting y-coordinate of the puff puff
        """
        super(Puff, self).__init__()
        self.is_singing = False

        # sleeping frames
        self.frames = []
        self.frames.append(pygame.image.load("images/puff0.gif"))
        self.frames.append(pygame.image.load("images/puff1.gif"))
        self.frames.append(pygame.image.load("images/puff2.gif"))
        self.current_frame = 0
        self.surf = self.frames[self.current_frame]

        self.rect = self.surf.get_rect()
        self.init_y = pos_y                                       # save value to return to original height
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        """
        Update puff puff by running sleep/sing animations
        """
        if not self.is_singing:
            # run through sleeping frames, staying in bounds
            self.rect.top = self.init_y
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            self.surf = self.frames[self.current_frame]
        else:
            # float while singing
            self.surf = pygame.image.load("images/puff3.gif")
            self.rect.top -= 1


# sprites
all_sprites_list = pygame.sprite.Group()
puff1 = Puff(25, 200)
all_sprites_list.add(puff1)
puff2 = Puff(165, 200)
all_sprites_list.add(puff2)
puff3 = Puff(305, 200)
all_sprites_list.add(puff3)
puff4 = Puff(445, 200)
all_sprites_list.add(puff4)
puff5 = Puff(585, 200)
all_sprites_list.add(puff5)
puff6 = Puff(725, 200)
all_sprites_list.add(puff6)
puff7 = Puff(865, 200)
all_sprites_list.add(puff7)
puff8 = Puff(1005, 200)
all_sprites_list.add(puff8)

# main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background_image, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                puff1.is_singing = True
                sing(channel1, "sounds/c4.ogg")
            elif event.key == pygame.K_s:
                puff2.is_singing = True
                sing(channel2, "sounds/d4.ogg")
            elif event.key == pygame.K_d:
                puff3.is_singing = True
                sing(channel3, "sounds/e4.ogg")
            elif event.key == pygame.K_f:
                puff4.is_singing = True
                sing(channel4, "sounds/f4.ogg")
            elif event.key == pygame.K_j:
                puff5.is_singing = True
                sing(channel5, "sounds/g4.ogg")
            elif event.key == pygame.K_k:
                puff6.is_singing = True
                sing(channel6, "sounds/a4.ogg")
            elif event.key == pygame.K_l:
                puff7.is_singing = True
                sing(channel7, "sounds/b4.ogg")
            elif event.key == pygame.K_SEMICOLON:
                puff8.is_singing = True
                sing(channel8, "sounds/c5.ogg")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                puff1.is_singing = False
                channel1.stop()
            elif event.key == pygame.K_s:
                puff2.is_singing = False
                channel2.stop()
            elif event.key == pygame.K_d:
                puff3.is_singing = False
                channel3.stop()
            elif event.key == pygame.K_f:
                puff4.is_singing = False
                channel4.stop()
            elif event.key == pygame.K_j:
                puff5.is_singing = False
                channel5.stop()
            elif event.key == pygame.K_k:
                puff6.is_singing = False
                channel6.stop()
            elif event.key == pygame.K_l:
                puff7.is_singing = False
                channel7.stop()
            elif event.key == pygame.K_SEMICOLON:
                puff8.is_singing = False
                channel8.stop()

    all_sprites_list.update()
    for sprite in all_sprites_list:
        screen.blit(sprite.surf, sprite.rect)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
