from .solvers import FixedGridODESolver
from . import rk_common


class Euler(FixedGridODESolver):

    def step_func(self, func, t, dt, y):
        return tuple(dt * f_ for f_ in func(t, y))

    @property
    def order(self):
        return 1


class Midpoint(FixedGridODESolver):

    def step_func(self, func, t, dt, y):
        y_mid = tuple(y_ + f_ * dt / 2 for y_, f_ in zip(y, func(t, y)))
        return tuple(dt * f_ for f_ in func(t + dt / 2, y_mid))

    @property
    def order(self):
        return 2


class RK4Alt(FixedGridODESolver):

    def step_func(self, func, t, dt, y):
        return rk_common.rk4_alt_step_func(func, t, dt, y, enforce_openset=self.enforce_openset)

    @property
    def order(self):
        return 4


# Alias for compatiblity
RK4 = RK4Alt


class RK4Classic(FixedGridODESolver):

    def step_func(self, func, t, dt, y):
        return rk_common.rk4_step_func(func, t, dt, y, enforce_openset=self.enforce_openset)

    @property
    def order(self):
        return 4
