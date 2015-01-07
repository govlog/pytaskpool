# coding=utf-8

import multiprocessing as mp


class TaskPool(object):

    def __init__(self, var_type, max_process=0):
        """
        TaskPool initiator : creates the shared Queue between process.

        Arguments:
        var_type    : the type of var excepted from the launched functions
        max_process : pool number of process, if not set, it'll use number of detected CPUs.
        """

        # create the shared queue between process
        self.out_q = mp.Queue()

        # use the detected number of cpu if max_process arg isn't used
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

    def task_do(self, funcname, *args):
        """Execute the function and put indexed results in the shared queue"""
        self.var_type += funcname(*args)
        self.out_q.put([(self.task_index, [self.var_type])])

    def __get_results(self):
        """Wait the completion of remaining tasks (if any) and return the indexed results list"""
        if not self.finished:

            # getting the lasts queue datas from remaining process
            while mp.active_children():
                if self.out_q.qsize():
                    self.results += self.out_q.get()

            self.finished = True

        return self.results

    def __get_sorted_results(self):
        """Sort and return the indexed results list in order of tasks launch"""
        if not self.sorted_results:
            self.sorted_results = sorted(self.__get_results())

        return self.sorted_results

    # publics methods
    def launch(self, *args):
        """
        Launch the function with it args in a process if there is a free slot, otherwise it will wait until a slot is
        freed

        Arguments:
        *args : function_name , param1 , param2 , ...
        """
        if self.running == self.max_process:
            self.results += self.out_q.get()
            self.running -= 1

        p = mp.Process(target=self.task_do, args=list(args))
        p.start()

        self.running += 1
        self.task_index += 1

    def get_sorted_results(self):
        """Generator returning the results in tasks launch order"""
        for r in self.__get_sorted_results():
            yield r[1][0]

    def get_unsorted_results(self):
        """Generator returning the results in tasks completion order"""
        for r in self.__get_results():
            yield r[1][0]