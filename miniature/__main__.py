#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

import argparse
import logging

from miniature.machinist import JoinMachinist, SplitMachinist
from miniature.monk import Monk
from miniature.sag import Sag
from miniature.wind import Wind
from miniature.xtce import Xtce

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=str, help="action value")
    parser.add_argument("action", choices=["split", "join", "monk", "sag", "xtce", "wind"])
    args = parser.parse_args()

    match args.action:
        case "split":
            SplitMachinist(args.target)
        case "join":
            JoinMachinist(args.target)
        case "monk":
            v = Monk.safe_eval(args.target)
            logging.info(f"({args.target}) = {v}")
        case "sag":
            Sag.main()
        case "xtce":
            with open(args.target, "r") as fp:
                source = fp.read()
            Xtce.from_string(source)
        case "wind":
            Wind(75000, 100).df.to_parquet("wind.parquet")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logging.exception(err)
