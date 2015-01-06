Download and docs:
    http://pypi.python.org/pypi/pytaskpool
Source code & Development:
    https://github.com/govlog/pytaskpool
Issues:
    christopher __dot__ amiaud __at__ gmail.com


pytaskpool
==========
A simple multiprocess function pooler which create results generators

pytaskpool use python multiprocessing module

pytaskpool provide an easy way to execute python functions in a pool of process (not threads) for using all your CPU
cores. Functions results can be then obtained in order or not (via a generator).

installation
============
you can install it using pip :

pip install pytaskpool

using it
========


sample code :
-------------

This sample code will launch 8 function simultanously using a pool of 8 process
The execution time should be 1 second::

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

author
======
christopher __dot__ amiaud __at__ gmail.com