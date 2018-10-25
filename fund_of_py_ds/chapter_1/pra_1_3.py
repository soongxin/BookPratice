#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 计算球下落的距离
import functools


BOUNCE_RATE = 0.6


def bounce_distance(initial_height, allow_bouncing_times):
	distance_list = []
	for i in range(0, allow_bouncing_times):
		distance_list.extend([initial_height, initial_height * BOUNCE_RATE])
		initial_height = initial_height * BOUNCE_RATE
	return functools.reduce(lambda x, y: x+y, distance_list)

if __name__ == '__main__':
	print(bounce_distance(10, 2))
