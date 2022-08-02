#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
"""
from pyspark.sql import SparkSession


class Wind:

    def __init__(self, file_name: str):
        """TODO"""
        self.spark = SparkSession.builder.master("local[1]").appName("wind").getOrCreate()
        self.df = self.spark.read.option("multiline", "true").json(file_name)
