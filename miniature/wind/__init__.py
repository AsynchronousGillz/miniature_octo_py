#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
"""
import pandas


class Wind:

    def __init__(self, file_name: str):
        """TODO"""
        self.df = pandas.read_json(path_or_buf=file_name, lines=True)
