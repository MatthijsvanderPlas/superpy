# Imports
from components.inputParser import create_parser
import csv
import sys
from datetime import date
from time import sleep
from console import console, err_console

sys.path.insert(0, "./components")


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    # Accept arguments from argparse
    parser = create_parser()
    parsed = parser.parse_args()
    console.print(f"[blue bold]{parsed}")


if __name__ == "__main__":
    main()
