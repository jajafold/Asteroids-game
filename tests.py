import math
import unittest

import pygame

from src.asteroid import Asteroid
from src.ship import Ship
from src.ufo import Ufo
from src.utils.Vector2D import Vector2D
from src.bullet import Bullet
from game_objects import detect_collision
from src.utils.obj_type import ObjectType


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.ship = Ship()

    def testRect(self):
        rect = self.ship.offset_rect
        self.assertEqual(rect, self.ship.rect)

    def testRotating(self):
        rotated = self.ship.rot_center(30)
        rotated_image = pygame.transform.rotate(self.ship.ship_image, 30)
        image_center = self.ship.ship_image.get_rect(center=(self.ship.x, self.ship.y)).center
        new_rect = rotated_image.get_rect(center=image_center)
        self.assertEqual(rotated[1], new_rect)

    def testShipCollisions(self):
        bullet = Bullet(self.ship.x, self.ship.y, Vector2D(1, 1))
        asteroid = Asteroid(self.ship.x, self.ship.y, Vector2D(1, 1))
        collision = self.ship.detect_collision()
        self.assertIsNotNone(collision[0])
        self.assertIsNotNone(collision[1])
        self.assertEqual(type(bullet), type(collision[0]))
        self.assertEqual(type(asteroid), type(collision[1]))

    def testBulletAsteroidCollision(self):
        bullet = Bullet(self.ship.x, self.ship.y, Vector2D(1, 1))
        asteroid = Asteroid(self.ship.x, self.ship.y, Vector2D(1, 1))
        collision = asteroid.detect_collision()
        self.assertIsNotNone(collision)
        self.assertEqual(type(bullet), type(collision))

    def testUfoBullet(self):
        bullet = Bullet(self.ship.x + 5, self.ship.y + 5, Vector2D(1, 1))
        ufo = Ufo(self.ship.x, self.ship.y, self.ship)
        collision = ufo.detect_collision()
        self.assertIsNotNone(collision)
        self.assertEqual(type(bullet), type(collision))

    def checkInbounds(self):
        bullet_one = Bullet(self.ship.x, self.ship.y, Vector2D(1, 1))
        bullet_two = Bullet(-100, 300, Vector2D(1, 1))
        self.assertTrue(bullet_one.is_inbounds)
        self.assertFalse(bullet_two.is_inbounds)


class TestVector(unittest.TestCase):
    def testAdd(self):
        a = Vector2D(1, 1)
        b = Vector2D(5, 2)
        self.assertEqual(Vector2D(6, 3), a + b)
        a += b
        self.assertEqual(Vector2D(6, 3), a)

    def testSub(self):
        a = Vector2D(1, 1)
        b = Vector2D(5, 2)
        self.assertEqual(Vector2D(-4, -1), a - b)
        a -= b
        self.assertEqual(Vector2D(-4, -1), a)

    def testMulDiv(self):
        b = Vector2D(6, 3)
        size = 3
        self.assertEqual(Vector2D(18, 9), b * size)
        self.assertEqual(Vector2D(2, 1), b / size)
        b *= size
        self.assertEqual(Vector2D(18, 9), b)
        b /= size**2
        self.assertEqual(Vector2D(2, 1), b)

    def testLen(self):
        b = Vector2D(3, 4)
        self.assertEqual(5, b.length)

    def testRotate(self):
        a = Vector2D(1, 0)
        rotated_a = a.rotate(math.pi/2)
        self.assertAlmostEqual(0, rotated_a.x, delta=1e-10)
        self.assertAlmostEqual(1, rotated_a.y, delta=1e-10)

    def testAngle(self):
        a = Vector2D(1, 0)
        b = Vector2D(0, 1)
        c = Vector2D(1, 1)
        d = Vector2D(1, -1)
        self.assertEqual(0, a.angle)
        self.assertEqual(math.pi/2, b.angle)
        self.assertEqual(math.pi/4, c.angle)
        self.assertEqual(-math.pi/4, d.angle)

    def testStr(self):
        a = Vector2D(2, 5)
        self.assertEqual("2,5", a.__str__())
