import math
import random
from math import *


def get_random_vector():
    random_angle = random.random() * 2 * pi
    return Vector2D(math.cos(random_angle), math.sin(random_angle))


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, size: int):
        return Vector2D(self.x * size, self.y * size)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, a):
        self.x *= a
        self.y *= a
        return self

    def __itruediv__(self, a):
        self.x /= a
        self.y /= a
        return self

    def __truediv__(self, a):
        return Vector2D(self.x / a, self.y / a)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return "{0},{1}".format(self.x, self.y)

    def rotate(self, angle):
        new_vec = Vector2D(self.x * cos(angle) - self.y * sin(angle),
                           self.x * sin(angle) + self.y * cos(angle))
        return new_vec

    @property
    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)

    @property
    def angle(self):
        if self.x == 0:
            if self.y > 0:
                return math.pi / 2
            else:
                return -math.pi / 2

        return atan(self.y / self.x)
