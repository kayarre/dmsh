import dmsh
from helpers import assert_norm_equality, save


def test_union(show=False):
    geo = dmsh.Union([dmsh.Circle([-0.5, 0.0], 1.0), dmsh.Circle([+0.5, 0.0], 1.0)])
    X, cells = dmsh.generate(geo, 0.15, show=show, tol=1.0e-10)

    geo.plot()

    ref_norms = [3.0088043884612756e02, 1.5785099320497183e01, 1.5]
    assert_norm_equality(X.flatten(), ref_norms, 1.0e-12)
    return X, cells


if __name__ == "__main__":
    X, cells = test_union(show=False)
    save("union.png", X, cells)
