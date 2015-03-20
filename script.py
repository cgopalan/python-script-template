"""
    Module documentation.
"""

import argparse


def run_task():
    """ Function documentation. """
    pass


def parse_cmd_line_args():
    """ Parses the arguments specified on the command line. """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true",
                  help=("Turn on verbose logging"))

    # Add more arguments

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_cmd_line_args()
    run_task()