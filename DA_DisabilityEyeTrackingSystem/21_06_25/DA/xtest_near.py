import unittest
from point import Point, Targets
import math

class TestNear(unittest.TestCase):

    def test_distance(self):
        p1 = Point(2., 1.)
        p2 = Point(1., 2.)
        self.assertAlmostEqual(p1.distance(p2), math.sqrt(2.))

    def test_closest(self):
        p1 = Point(2., 1.)
        p2 = Point(1., 2.)
        targets = Targets([p1, p2])
        closest = targets.closestTarget(p1)
        self.assertAlmostEqual(closest.distance(p1), 0.)
        closest = targets.closestTarget(Point(1.5, 1.4))
        self.assertAlmostEqual(closest.distance(p1), 0.)
        

if __name__ == '__main__':
    unittest.main()