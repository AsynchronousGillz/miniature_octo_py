#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
"""

import statistics
from typing import Union
from threading import RLock


class Metric:
    """ A simple metric class """

    def __init__(self, size: int = 100):
        """

        :param size:
        """
        self._size = size
        self._array = []
        self._index = 0
        self._lock = RLock()

    def add(self, metric: Union[int, float]) -> None:
        """

        :param metric:
        :return:
        """
        with self._lock:
            try:
                self._array[self._index] = metric
            except IndexError:
                self._array.append(metric)
            self._index = self._index + 1 if self._index < self._size else 0

    def stats(self, percentiles: list = None) -> dict:
        """ Get some stats

        :param percentiles: list of percentiles
        :return:
        """
        with self._lock:
            _perc = statistics.quantiles(self._array, n=100)
            stats = {f"p{perc}": _perc[perc] for perc in percentiles}
            stats.update({"min": min(self._array), "max": max(self._array)})
            return stats

