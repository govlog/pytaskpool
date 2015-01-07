pytaskpool
==========

A simple multiprocess function pooler which create results generators

pytaskpool use the python multiprocessing module

pytaskpool provide an easy way to execute python functions in a pool of process (not threads) for using all your CPU
cores. Functions results can then be then obtained in order or not (via a generator method).

pytaskpool works on windows and linux.

Download and docs:
    http://pypi.python.org/pypi/pytaskpool
Source code & Development:
    https://github.com/govlog/pytaskpool
Issues:
    christopher.amiaud@gmail.com


Installation
============

pytaskpool is available in the python index package (pip),
It can be installed running the following command::

    $ pip install pytaskpool

or by git like this::

    $ git clone https://github.com/govlog/pytaskpool
    $ cd pytaskpool
    $ sudo python setup.py install

or even in a zip over http : https://github.com/govlog/pytaskpool/archive/master.zip

Usage
=====

This sample code will simultanously launch 8 functions with differents parameters using a pool of 8 processes.
The results returned by all launched functions will be get by the method get_sorted_results(), which is a generator
returning the functions results in order.

The excepted execution time should be around 1 second.

Sample code::

    import pytaskpool as tp
    from time import sleep

    def my_func(x):
        sleep(1)
        return [x ** x]

    mypool = tp.TaskPool([], 8)

    for r in range(8):
        mypool.launch(my_func, r)

    unsorted = [r for r in mypool.get_unsorted_results()]
    sorted = [r for r in mypool.get_sorted_results()]

    print "unsorted :",unsorted
    print "sorted   :",sorted

Terminal output should look like this::

    $ time python test.py
    unsorted : [[1], [4], [1], [3125], [823543], [256], [27], [46656]]
    sorted   : [[1], [1], [4], [27], [256], [3125], [46656], [823543]]

    real    0m1.031s
    user    0m0.858s
    sys     0m0.193s

