from math import *

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, size):
        return Vector2D(self.x * size, self.y * size)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

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
    
    def __str__(self) -> str:
        return "{0},{1}".format(self.x, self.y)

    def rotate(self, angle):
        self.x = self.x * cos(angle) - self.y * sin(angle)
        self.y = self.x * sin(angle) + self.y * cos(angle)
        self /= self.length
        return self

    @property
    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)

    @property
    def angle(self):
        if self.x == 0:
            if self.y > 0:
                return 90
            else:
                return -90

        return atan(self.y / self.x)
