import dmsh
from helpers import assert_norm_equality, save


def test_pacman(show=False):
    geo = dmsh.Difference(
        dmsh.Circle([0.0, 0.0], 1.0),
        dmsh.Polygon([[0.0, 0.0], [1.5, 0.4], [1.5, -0.4]]),
    )
    X, cells = dmsh.generate(geo, 0.1, show=show, tol=1.0e-10)

    ref_norms = [3.0385105041432689e02, 1.3644964912810719e01, 1.0]
    assert_norm_equality(X.flatten(), ref_norms, 1.0e-12)
    return X, cells


if __name__ == "__main__":
    X, cells = test_pacman(show=False)
    save("pacman.png", X, cells)
