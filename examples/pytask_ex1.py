# coding=utf-8
from time import sleep
from random import randint

import pytaskpool as tp


def test_func(x):
    """
    This  function return the square root of x in an array after randomly waiting between 0 to 2.56s
    """
    rand_time = randint(0, 256) / 100.
    sleep(rand_time)
    print ("function :", x, ": sleeping", rand_time, "before exit")
    return [x ** x]


# how many time we execute the function
count = 32

# how many process we'll use
process = 4

count_depth = range(count)
excepted = [[r ** r] for r in count_depth]

# creation of a pool of 8 process
tp = tp.TaskPool([], 8)

print ("Launching", count, "functions that will wait between 0 to 2.56s using", process, "processes")

# launch
for y in count_depth:
    tp.launch(test_func, y)

print ("All launched, waiting all to finish")

unres = [r for r in tp.get_unsorted_results()]
print ("All tasks done")

res = [r for r in tp.get_sorted_results()]

if res == excepted:
    print ("results match the excepted")
