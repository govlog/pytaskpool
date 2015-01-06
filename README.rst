pytaskpool
==========

Download and docs:
    http://pypi.python.org/pypi/pytaskpool
Source code & Development:
    https://github.com/govlog/pytaskpool
Issues:
    christopher.amiaud@gmail.com

Description
===========

A simple multiprocess function pooler which create results generators

pytaskpool use python multiprocessing module

pytaskpool provide an easy way to execute python functions in a pool of process (not threads) for using all your CPU
cores. Functions results can be then obtained in order or not (via a generator).

Installation
============

pytaskpool is available in the python index package (pip),
It can be installed running the following command:

``pip install pytaskpool``

Usage
=====

This sample code will launch 8 function simultanously using a pool of 8 process
The execution time should be 1 second.

Sample code::

    import pytaskpool as tp
    from time import sleep

    # this function wait 1 second before return
    def my_func(x):
        sleep(1)
        return [x ** x]

    # create a pool of 8 process
    mypool = tp.TaskPool([], 8)

    # launch my_func eight times
    for r in range(8):
        tp.launch(my_func, r)

    #display results
    for r in tp.get_sorted_results():
        print r


Result of execution::

    gov@dev:~$ time python example.py
    [1]
    [1]
    [4]
    [27]
    [256]
    [3125]
    [46656]
    [823543]

    real    0m1.036s
    user    0m0.845s
    sys     0m0.210s
    gov@dev:~$

