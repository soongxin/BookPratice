#! /usr/bin/env python
# -*- coding: utf-8 -*-
PI = 3.1415926

class Ball(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def circumference(self):
        return 2 * PI * self.radius

    @property
    def surface_area(self):
        return 4 * PI * pow(self.radius, 2)

    @property
    def volume(self):
        return 4/3 * PI * pow(self.radius, 3)


if __name__ == '__main__':
    ball = Ball(1)
    print('diameter: ', ball.diameter)
    print('circumference: ', ball.circumference)
    print('surface_area: ', ball.surface_area)
    print('volume: ', ball.volume)