import numpy

import pypathlib


class LineSegmentPath:
    def __init__(self, x0, x1):
        self.x0 = x0
        self.x1 = x1
        return

    def p(self, t):
        return numpy.multiply.outer(self.x0, 1 - t) + numpy.multiply.outer(self.x1, t)

    def dp_dt(self, t):
        ones = numpy.ones(t.shape)
        return numpy.multiply.outer(self.x0, -ones) + numpy.multiply.outer(
            self.x1, ones
        )


class Polygon:
    def __init__(self, points):
        points = numpy.array(points)
        self.bounding_box = [
            numpy.min(points[:, 0]),
            numpy.max(points[:, 0]),
            numpy.min(points[:, 1]),
            numpy.max(points[:, 1]),
        ]
        self.polygon = pypathlib.ClosedPath(points)
        self.feature_points = points

        self.paths = [
            LineSegmentPath(p0, p1)
            for p0, p1 in zip(points, numpy.roll(points, -1, axis=0))
        ]
        return

    def plot(self):
        self.polygon.plot(color="#1f77b4")
        return

    def dist(self, x):
        out = self.polygon.signed_distance(x.T)
        return out

    def boundary_step(self, x):
        # print("b")
        # print(x.T)
        # print("{:.16e}".format(x[0][0]))
        # print("{:.16e}".format(x[1][0]))
        # print("{:.16e}".format(self.dist(x)[0]))
        out = self.polygon.closest_points(x.T).T
        # print(out.T)
        # print(x.T - out.T)
        # print()
        return out
