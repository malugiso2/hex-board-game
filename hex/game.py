from math import sqrt
from consts import *
import pygame as pg

from funcs import Point, drawHex


class Game:
    def __init__(self, size):
        # pg.init()
        self.size = size
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Tile size = top to button
        self.tile_width = ((WINDOW_WIDTH - 100) / (self.size + (self.size - 1) * 0.5))
        self.tile_height = 2 * self.tile_width / sqrt(3)
        self.state = [[0 for _ in range(self.size)] for __ in range(self.size)]
        self.origin = Point(50, 50)

        pg.display.set_caption("Hex Game")

    def coords(self, r, c):
        """translates grid coordinates to real coordinates"""
        x = self.origin.x + (c + r / 2) * self.tile_width
        y = self.origin.y + 0.75 * r * self.tile_height
        return int(x), int(y)

    def show_grid(self):
        """shows hexagonal grid as well as players moves and destination sides"""
        # draw bounds
        corner_a = (self.origin.x - 1 / 2 * self.tile_width, self.origin.y)
        corner_b = (self.origin.x + self.tile_width * self.size - 1 / 8 * self.tile_width, self.origin.y)
        corner_c = (self.origin.x + self.tile_width * (self.size + (self.size - 1) * 0.5 + 0.5),
                    self.origin.y + self.tile_height * (self.size + 1) * 3 / 4 - 1 / 2 * self.tile_height)
        corner_d = (self.origin.x + ((self.size - 1) * 0.5) * self.tile_width + self.tile_width * 0.2,
                    self.origin.y + self.tile_height * (self.size + 1) * 3 / 4 - 1 / 2 * self.tile_height)
        middle_x = (self.origin.x + self.tile_width * (self.size + (self.size - 1) * 0.5)) / 2
        middle_y = (self.origin.y + self.tile_height * (self.size + 1) * 3 / 4 - 1 / 2 * self.tile_height) / 2
        midpoint = (middle_x, middle_y)

        pg.draw.polygon(self.screen, GREEN, [corner_a, corner_b, midpoint])  # Color green top row
        pg.draw.polygon(self.screen, BLUE, [corner_b, corner_c, midpoint])  # Color Blue right
        pg.draw.polygon(self.screen, GREEN, [corner_c, corner_d, midpoint])  # Color green bottom row
        pg.draw.polygon(self.screen, BLUE, [corner_d, corner_a, midpoint])  # Color Blue left

        for r in range(self.size):
            for c in range(self.size):
                x, y = self.coords(r, c)
                # draw players
                if self.state[r][c] == 1:
                    drawHex(self.screen, GREEN, LIGHTYELLOW, (x, y), self.tile_width, self.tile_width)
                elif self.state[r][c] == 2:
                    drawHex(self.screen, BLUE, LIGHTYELLOW, (x, y), self.tile_width, self.tile_width)
                elif self.state[r][c] == 3:
                    drawHex(self.screen, LIGHTGREEN, LIGHTYELLOW, (x, y), self.tile_width, self.tile_width)
                elif self.state[r][c] == 4:
                    drawHex(self.screen, LIGHTBLUE, LIGHTYELLOW, (x, y), self.tile_width, self.tile_width)
                else:
                    drawHex(self.screen, DARKRED, LIGHTYELLOW, (x, y), self.tile_height, self.tile_width)



def main():
    game = Game(SIZE)
    game.screen.fill(WHITE)

    run = True

    while run:
        game.clock.tick(FPS)
        game.show_grid()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()

# Sources
# https://www.redblobgames.com/grids/hexagons/
