from argparse import Namespace
from components.inputParser import create_parser
import sys

sys.path.insert(0, "./components")


def test_input():
    parser = create_parser()
    parsing = parser.parse_args
    assert parsing(["buy", "-n", "Orange", "-p", "2"]) == Namespace(
        buy=True, name_product="Orange", price=2, amount=1, expiration=10
    )


def test_input2():
    parser = create_parser()
    parsing = parser.parse_args
    assert parsing(["sell", "-n", "Brocolli", "-p", "3"]) == Namespace(
        sell=True, name_product="Brocolli", price=3, amount=1
    )
