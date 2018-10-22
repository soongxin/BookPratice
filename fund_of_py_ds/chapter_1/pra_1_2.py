#! /usr/bin/env python
# -*- coding: utf-8 -*-


def week_salary(salary_per_hour, total_work_time, overtime_work_time):
    return salary_per_hour * total_work_time + salary_per_hour * overtime_work_time * 1.5


if __name__ == '__main__':
    print('total salary: ', week_salary(80, 40, 3))