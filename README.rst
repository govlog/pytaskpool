pytaskpool
==========
A simple multiprocess function pooler which create results generators

pytaskpool use python multiprocessing module

pytaskpool provide an easy way to execute python functions in a pool of process (not threads) for using all your CPU cores. Functions results can be then obtained in order or not (via a generator).

installation
============
you can install it using pip :

pip install pytaskpool

using it
========


sample code :
-------------
 import pytaskpool as tp

 def my_func(x):
   return [x ** x]

 # create a pool of 8 process
 mypool = tp.TaskPool([], 8)

 # launch 100 my_func
 for r in range(100):
   tp.launch(my_func, r)

 #display results
 for r in tp.get_sorted_results():
   print r

author
======
christopher __dot__ amiaud __at__ gmail.com