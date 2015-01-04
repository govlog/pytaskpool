# coding=utf-8

"""
import the multiprocessing class
"""

import multiprocessing as mp


class TaskPool(object):
    """
    This class permit the asynchronous execution of functions
    with a way of getting the results in order or not
    """

    def __init__(self, var_type, max_process=0):

        self.out_q = mp.Queue()

        if not max_process:
            self.max_process = mp.cpu_count()
        else:
            self.max_process = max_process

        self.task_index = 0
        self.running = 0
        self.var_type = var_type
        self.results = []
        self.sorted_results = []
        self.finished = False

    # methodes privees
    def __task_do(self, funcname, *args):

        self.var_type += funcname(*args)
        self.out_q.put([(self.task_index, [self.var_type])])

    def __get_results(self):

        if not self.finished:
            while mp.active_children():
                if self.out_q.qsize():
                    self.results += self.out_q.get()

            self.finished = True

        return self.results

    def __get_sorted_results(self):

        if not self.sorted_results:
            self.sorted_results = sorted(self.__get_results())

        return self.sorted_results

    # methodes publiques
    def launch(self, *args):
        """
        Launch the function process in background

        :param args: function name, param1, param2, ...
        """
        if self.running == self.max_process:
            self.results += self.out_q.get()
            self.running -= 1

        p = mp.Process(target=self.__task_do, args=list(args))
        p.start()

        self.running += 1
        self.task_index += 1

    def get_sorted_results(self):
        """
        This generator return the sorted results
        """
        for r in self.__get_sorted_results():
            yield r[1][0]

    def get_unsorted_results(self):
        """
        This generator return the results in the order of completed tasks
        """
        for r in self.__get_results():
            yield r[1][0]