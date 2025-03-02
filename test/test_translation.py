import dmsh
from helpers import assert_norm_equality


def test(show=False):
    geo = dmsh.Translation(dmsh.Rectangle(-1.0, +2.0, -1.0, +1.0), [1.0, 1.0])
    X, cells = dmsh.generate(geo, 0.1, show=show)

    ref_norms = [1.7525e03, 5.5677441324948013e01, 3.0]
    assert_norm_equality(X.flatten(), ref_norms, 1.0e-12)
    return


if __name__ == "__main__":
    test(show=False)
