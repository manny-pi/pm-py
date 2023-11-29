#! /usr/local/bin/python3.8

"""
`pm-py` (v1): a Python-based predecessor of `pm`.
"""


import os, sys
import argparse
import logging
import datetime
import flask
from pathlib import Path


# Supported commands
# = = = = = = = = = = = = = = = = = = = = = = = 
# Identity and Access Management
def get_creation_time(file: [str, Path]):
    """Returns the creation time of a resource `file`.
    
    args:
        file: `str` or `pathlib.Path` object. Must be absolute path if 
        the file is not located in the working directory.
    returns:
        
    """

def get_modification_teim(file: [str, Path]):
    """Returns the time when a resource was last modified."""

def get_access_time(file: [str, Path]): 
    """Returns the access time of a resource."""

def setup():
    parser = argparse.ArgumentParser(
        prog="pm", 
        description="Lazy Process Manager.",
        usage="""
        """
    )
    subparser = parser.add_subparsers(help="sub-command help")



    print(get_access_time)

    # In Development
    # = = = = = = = = = = = = = = = = = = = = = = = 
    # 
    # memory
    mem_parser = subparser.add_parser('mem', help='memory module')
    mem_parser.add_argument('--dump', action='store_true', help='Print summary information about the running process')
    mem_parser.add_argument()


namespace = parser.parse_args()
if namespace.dump:
    print("memory dump")

    # Print the following information


if __name__ == "__main__":
    pass 


