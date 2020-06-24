"""Some simple skeleton code for a pygame game/animation

This skeleton sets up a basic 800x600 window, an event loop, and a
redraw timer to redraw at 30 frames per second.
"""
from __future__ import division
import math
import sys
import pygame


class MyGame(object):
    def __init__(self):
        """Initialize a new game"""
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        # set up a 640 x 480 window
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))

        # use a black background
        self.bg_color = 0, 0, 0
        self.img = pygame.image.load("globe.png")
        self.img_cpy = self.img
        self.img_x = 0
        self.img_y = 399
        self.delta_x = 12
        self.delta_y = 12
        # Setup a timer to refresh the display FPS times per second
        self.FPS = 30
        self.REFRESH = pygame.USEREVENT+1
        pygame.time.set_timer(self.REFRESH, 1000//self.FPS)

        self.angle = 0

    def run(self):
        """Loop forever processing events"""
        running = True
        while running:
            event = pygame.event.wait()

            # player is asking to quit
            if event.type == pygame.QUIT:
                running = False

            # time to draw a new frame
            elif event.type == self.REFRESH:
                self.draw()

            else:
                pass # an event type we don't handle

    def draw(self):
        """Update the display"""
        # everything we draw now is to a buffer that is not displayed
        self.screen.fill(self.bg_color)

        rect = self.img.get_rect()
        #self.img_y += self.delta_y

        """if self.img_x  >= self.width - rect.width or self.img_x < 0:
            self.delta_x = -self.delta_x"""

        if self.img_x  >= self.width - rect.width:
            self.img_x = self.width - rect.width
            self.img_y -= self.delta_y

        if self.img_y <= 0:
            self.img_y = 0
            self.img_x -= self.delta_x

        if self.img_x <= 0:
            self.img_x = 0
            self.img_y += self.delta_y

        if self.img_y >= self.height-rect.height:
            self.img_y = 0
            self.img_x += self.delta_x

        else:
            self.img_x += self.delta_x


        rect = rect.move(self.img_x, self.img_y)
        self.angle += 6
        self.angle %= 360

        self.img_cpy = pygame.transform.rotate(self.img, self.angle)
        self.screen.blit(self.img_cpy, rect)

            #rect = rect.move(self.width - rect.width, self.height-rect.height) #Bottom right
            #print(rect)
            #rect = rect.move(self.width - rect.width, 0) #Top right
            #rect = rect.move(0, 0) #Top left
            #rect = rect.move(0, self.height-rect.height) #Bottom left
        #self.screen.blit(self.img, rect)
            # flip buffers so that everything we have drawn gets displayed
        pygame.display.flip()


MyGame().run()
pygame.quit()
sys.exit()
