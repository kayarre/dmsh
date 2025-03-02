import numpy

import dmsh
from helpers import assert_norm_equality, save


def test(show=False):
    r = dmsh.Rectangle(-1.0, +1.0, -1.0, +1.0)
    c = dmsh.Circle([0.0, 0.0], 0.3)
    geo = dmsh.Difference(r, c)

    numpy.random.seed(0)
    X, cells = dmsh.generate(
        geo, lambda pts: numpy.abs(c.dist(pts)) / 5 + 0.05, show=show, tol=1.0e-10
    )

    ref_norms = [2.4810107884562055e02, 1.2004528988116096e01, 1.0]
    assert_norm_equality(X.flatten(), ref_norms, 1.0e-12)
    return X, cells


if __name__ == "__main__":
    X, cells = test(show=False)
    save("square_hole_refined.png", X, cells)
