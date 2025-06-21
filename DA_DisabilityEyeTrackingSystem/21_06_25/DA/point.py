import math

class Point():
    def __init__(self, x:float, y:float):
        self._x = x
        self._y = y
    
    def distance(self, other) -> float:
        diff = Point(other._x - self._x, other._y - self._y)
        return math.sqrt(diff._x*diff._x + diff._y*diff._y)

class Targets():
    def __init__(self, targets: list[Point]):
        self._targets = targets
        
    def closestTarget(self, point:Point) -> Point:
        minDistance = 1e9
        minTarget = self._targets[0]
        for target in self._targets:
            distance = target.distance(point)
            if distance < minDistance:
                minTarget = target
                minDistance = distance
        return minTarget
                
            