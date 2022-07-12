#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

import argparse
import logging

from miniature.split import split
from miniature.machinist.join import join
from miniature.xtce import Xtce

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help='file or directory to split or join')
    parser.add_argument('action', choices=['split', 'join', 'xtce'])
    args = parser.parse_args()

    match args.action:
        case 'split':
            split(args.target)
        case 'join':
            join(args.target)
        case 'xtce':
            Xtce(args.target)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logging.exception(err)
