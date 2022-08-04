import pytaskpool as tp
from time import sleep

def my_func(x):
    sleep(1)
    return x ** x

mypool = tp.TaskPool(8)

for r in range(8):
    mypool.launch(my_func, r)

unsorted = [r for r in mypool.get_unsorted_results()]
sorted = [r for r in mypool.get_sorted_results()]

print ("unsorted :",unsorted)
print ("sorted   :",sorted)

