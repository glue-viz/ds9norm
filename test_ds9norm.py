import numpy as np
import pytest

from ds9norm import *


def test_log_warp():
    x = np.array([0, 1, 10, 100, 101])
    y = log_warp(x, 1, 100, .5, 1)
    yexp = np.array([0, 0, .654, 1, 1])
    np.testing.assert_array_almost_equal(y, yexp, 3)


def test_sqrt_warp():
    x = np.array([0, 1, 10, 100, 101])
    y = sqrt_warp(x, 1, 100, .5, 1)
    yexp = np.array([0, 0, .3015, 1, 1])
    np.testing.assert_array_almost_equal(y, yexp, 3)


def test_pow_warp():
    x = np.array([0, 1, 10, 100, 101])
    y = pow_warp(x, 1, 100, .5, 1)
    yexp = np.array([0, 0, .00087, 1, 1])
    np.testing.assert_array_almost_equal(y, yexp, 3)


def test_squared_warp():
    x = np.array([0, 1, 10, 100, 101])
    y = squared_warp(x, 1, 100, .5, 1)
    yexp = np.array([0, 0, .008264, 1, 1])
    np.testing.assert_array_almost_equal(y, yexp, 3)


def test_asinh_warp():
    x = np.array([0, 1, 10, 100, 101])
    y = asinh_warp(x, 1, 100, .5, 1)
    yexp = np.array([0, 0, .27187, 1, 1])
    np.testing.assert_array_almost_equal(y, yexp, 3)


def test_linear_warp():
    x = np.array([0, 1, 10, 100, 101])
    y = linear_warp(x, 1, 100, .5, 1)
    yexp = np.array([0, 0, 9. / 99., 1, 1])
    np.testing.assert_array_almost_equal(y, yexp, 3)


def test_bias():
    x = np.array([0, .4, .5, .6, 1])

    y = cscale(x.copy(), .5, 1)
    np.testing.assert_array_almost_equal(x, y)

    y = cscale(x.copy(), .5, 2)
    yexp = np.array([0, .3, .5, .7, 1])
    np.testing.assert_array_almost_equal(y, yexp)

    y = cscale(x.copy(), .5, 0)
    yexp = np.array([.5, .5, .5, .5, .5])
    np.testing.assert_array_almost_equal(y, yexp)

    y = cscale(x.copy(), .5, 0)
    yexp = np.array([.5, .5, .5, .5, .5])
    np.testing.assert_array_almost_equal(y, yexp)

    y = cscale(x.copy(), .4, 1)
    yexp = np.array([.1, .5, .6, .7, 1])
    np.testing.assert_array_almost_equal(y, yexp)

    y = cscale(x.copy(), .6, 1)
    yexp = np.array([0, .3, .4, .5, .9])
    np.testing.assert_array_almost_equal(y, yexp)


class TestDS9Normalize(object):

    def setup_method(self, method):
        self.norm = DS9Normalize()

    def test_input_unmodified(self):
        x = np.array([1, 2, 3])
        self.norm.contrast = 100
        y = self.norm(x)
        assert np.abs(x - y).max() > .1
        np.testing.assert_array_almost_equal(x, [1, 2, 3])

    def test_call_default(self):
        x = np.array([1, 2, 3])
        np.testing.assert_array_almost_equal(self.norm(x), [0, .5, 1])

    def test_call_invert(self):
        x = np.array([1, 2, 3])
        self.norm.vmin = 3
        self.norm.vmax = 1
        np.testing.assert_array_almost_equal(self.norm(x), [1, .5, 0])

    def test_invalid_stretch(self):
        with pytest.raises(ValueError) as exc:
            self.norm.stretch = 'invalid'
        assert exc.value.args[0].startswith("Invalid stretch")

    def test_update_clip(self):
        x = np.arange(101)
        self.norm.update_clip(x)
        assert self.norm.vmin == 0
        assert self.norm.vmax == 100

    def test_autoscale_on_call(self):
        x = np.arange(101)
        self.norm.clip_lo = 7
        self.norm.clip_hi = 16
        self.norm(x)
        np.testing.assert_array_almost_equal([self.norm.vmin, self.norm.vmax],
                                             [7, 16])

    def test_update_clip_nans(self):
        x = np.zeros(5) * np.nan
        self.norm.update_clip(x)
        assert self.norm.vmin == 0
        assert self.norm.vmax == 1
