#!/usr/bin/python3
from argparse import ArgumentParser
import xml_parce as xml

def line_to_dictionaty():
    parser = ArgumentParser()
    parser.add_argument("--file", dest="filename",
                        help="write report to FILE", metavar="FILE")
    parser.add_argument("-q", "--quiet",
                        action="store_false", dest="verbose", default=True,
                        help="don't print status messages to stdout")

    return vars(parser.parse_args())

print(line_to_dictionaty())

