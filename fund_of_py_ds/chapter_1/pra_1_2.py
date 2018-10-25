#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
一个雇员一周的总薪水，等于其每小时的薪水乘以一周正常工作的小时数，再加上加班费
加班费等于总的加班时间乘以每小时薪水的1.5倍，编写一个程序，以每小时的薪水、总
的常规工作时间和总的加班时间作为参数， 并且显示一个雇员的总周薪
"""

def week_salary(salary_per_hour, total_work_time, overtime_work_time):
    return salary_per_hour * total_work_time + salary_per_hour * overtime_work_time * 1.5


if __name__ == '__main__':
    print('total salary: ', week_salary(80, 40, 3))
