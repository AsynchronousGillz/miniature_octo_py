#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

import os

_chunk_size = "MINIATURE_CHUNK_SIZE"

_server_port = "MINIATURE_PORT"

try:
    CHUNK_SIZE = int(os.getenv(_chunk_size, "10000"))
except ValueError:
    CHUNK_SIZE = 10000

try:
    PORT = int(os.getenv(_server_port, "443"))
except ValueError:
    PORT = 2900
