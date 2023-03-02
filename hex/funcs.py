import pygame as pg
from math import hypot


class Point:
    def __init__(self, *pos):
        if len(pos) == 1:
            self.x, self.y = pos[0]
            self.X, self.Y = list(map(int, pos[0]))
        else:
            self.x, self.y = pos
            self.X, self.Y = list(map(int, pos))

    def dist(self, other):
        return hypot(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return '[x:{x}, y:{y}]'.format(x=self.x, y=self.y)

    def __iter__(self):
        """for unpacking"""
        return (x for x in (self.x, self.y))


def drawHex(surface, colIn, colOut, pos, height, width):
    x, y = pos
    points = [
        (x + width / 2, y),
        (x + width, y + height / 4),
        (x + width, y + 3 * height / 4),
        (x + width / 2, y + height),
        (x, y + 3 * height / 4),
        (x, y + height / 4)
    ]

    pg.draw.polygon(surface, colIn, points)
    pg.draw.polygon(surface, colOut, points, 2)
