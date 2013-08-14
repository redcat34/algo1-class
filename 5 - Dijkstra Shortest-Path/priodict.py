#!/usr/bin/env python

from heapq import heapify, heappop, heappush

# Adapted from http://code.activestate.com/recipes/522995/
class PriorityDict(dict):

    def __init__(self, *args, **kwargs):
        super(PriorityDict, self).__init__(*args, **kwargs)
        self._heap = [ ]
        self._rebuild_heap()

    def __setitem__(self, key, val):
        super(PriorityDict, self).__setitem__(key, val)

        if len(self._heap) < 2 * len(self):
            heappush(self._heap, (val, key))
        else:
            self._rebuild_heap()

    def __iter__(self):
        while self:
            yield self.min()
            self.pop()

    def _rebuild_heap(self):
        self._heap = [(v, k) for k, v in self.items()]
        heapify(self._heap)

    def min(self):
        heap = self._heap
        v, k = heap[0]
        while k not in self or self[k] is not v:
            heappop(heap)
            v, k = heap[0]
        return k

    def pop(self):
        heap = self._heap
        v, k = heappop(heap)
        while k not in self or self[k] != v:
            v, k = heappop(heap)
        del self[k]
        return k

