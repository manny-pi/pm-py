#! /Library/Frameworks/Python.framework/Versions/3.8

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("example", help="the name of the example you want to run.")
    parser.add_argument("--verbose", help="increase the output verbosity.", action="store_true")


    args = parser.parse_args()
    print(parser.parse_args())