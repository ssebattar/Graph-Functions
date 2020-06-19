import math
import csv


def sin_func():
    pie = math.pi
    increment1 = pie / 64
    start = -2 * pie
    stop = 2 * pie

    while start < stop:
        print(f"X = {start}, Sin(x) = {math.sin(start)}")
        start += increment1


def cos_func():
    pie = math.pi
    increment1 = pie / 64
    start = -2 * pie
    stop = 2 * pie

    while start < stop:
        print(f"X = {start}, Cos(x) = {math.cos(start)}")
        start += increment1


def sqrt_func():
    increment2 = 0.5
    start = 0
    stop = 200

    while start < stop:
        print(f"X = {start}, Sqrt(x) = {math.sqrt(start)}")
        start += increment2


def log_func():
    increment2 = 0.5
    start = 0
    stop = 200

    while start < stop:
        if start == 0:
            print(f"Log10 of {start} is undefined and therefore skipped!")
        start += increment2
        print(f"X = {start}, log10(x) = {math.log10(start)}")


sin_func()
cos_func()
sqrt_func()
log_func()
