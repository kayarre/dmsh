import dmsh
from helpers import assert_norm_equality


def test(show=False):
    geo = dmsh.Difference(
        dmsh.Rectangle(0.0, 5.0, 0.0, 5.0),
        dmsh.Polygon([[1, 1], [4, 1], [4, 4], [1, 4]]),
    )
    X, cells = dmsh.generate(geo, 1.0, show=show, tol=1.0e-3)

    assert_norm_equality(
        X.flatten(), [1.2599887992309357e02, 2.2109217065599051e01, 5.0], 1.0e-12
    )
    return


if __name__ == "__main__":
    test(show=False)
