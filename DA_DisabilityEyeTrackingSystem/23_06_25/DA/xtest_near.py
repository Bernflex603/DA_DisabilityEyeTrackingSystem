import unittest
from point import Point, Targets
import math
import dc_pickOption as po

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
        
    def test_pickOption(self):
        self.assertEqual(po.pickOption(1), "Option1")
        self.assertEqual(po.pickOption("2"), "Option2")
        self.assertEqual(po.pickOption("nix"), "defaultOption")
        

if __name__ == '__main__':
    unittest.main()