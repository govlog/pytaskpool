# coding=utf-8
import pytaskpool as tp
import time

from time import sleep
from pytaskpool import TaskPool


def test_func(x, wait):
    """
    This  function return the square root of x in an array after waiting a number of seconds defined by wait param
    """
    sleep(wait)
    return [x ** x]


# how many time we execute the function
count = 32

# how many process we'll use
process = 32

# function execution duration in seconds
wait = 1

count_depth = range(count)
order_exec = []
order_launch = []

# creation of a pool of process
tp = tp.TaskPool([], process)

print "Launching", count, "functions that will wait", wait, "second(s), with", process, "process"

# launch
for y in count_depth:
    tp.launch(test_func, y, wait)

# get results in order of launch
for r in tp.get_sorted_results():
    order_launch += r

# get results in order of completion
for r in tp.get_unsorted_results():
    order_exec += r

print
print "results in end of execution order :", order_exec
print
print "results in launch order           :", order_launch
