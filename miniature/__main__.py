#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""
import logging

from miniature.server import Server

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)


def main():
    Server.main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logging.exception(err)
