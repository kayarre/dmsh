import numpy


class LinePath:
    def __init__(self, v, tangent):
        self.v = v
        self.tangent = tangent
        return

    def p(self, t):
        """This parametrization of the line is (inf, inf) for t=0 and t=1.
        """
        # Don't warn on division by 0
        with numpy.errstate(divide="ignore"):
            out = (
                numpy.multiply.outer(self.tangent, (2 * t - 1) / t / (1 - t)).T + self.v
            ).T
        return out

    def dp_dt(self, t):
        with numpy.errstate(divide="ignore"):
            dt = 1 / t ** 2 + 1 / (1 - t) ** 2
        return numpy.multiply.outer(self.tangent, dt)


class HalfSpace:
    def __init__(self, normal, alpha):
        self.normal = normal
        self.alpha = alpha

        self.bounding_box = [-numpy.inf, +numpy.inf, -numpy.inf, +numpy.inf]
        self.feature_points = numpy.array([])

        # One point on the line:
        v = self.normal / numpy.dot(self.normal, self.normal) * self.alpha
        tangent = numpy.array([-self.normal[1], self.normal[0]])

        self.paths = [LinePath(v, tangent)]
        return

    def dist(self, x):
        assert x.shape[0] == 2
        return self.alpha - numpy.dot(self.normal, x)

    def boundary_step(self, x):
        beta = self.alpha - numpy.dot(self.normal, x) / numpy.dot(
            self.normal, self.normal
        )
        return x + numpy.multiply.outer(self.normal, beta)
