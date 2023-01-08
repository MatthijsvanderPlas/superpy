# buy a product and add to inventory
# sell a product and remove from inventory
# advance the internal date and then check for expired goods add those to the sold.csv as a negative
# print out different reports

import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="SuperPy",
        usage="SuperPy [buy | sell | report]",
        description="Welcome to your favorite local grocery store",
        epilog="Please use the above help to work with our program",
    )

    # Get the basic instruction
    instruction = parser.add_mutually_exclusive_group()
    # buy instruction
    instruction.add_argument(
        "buy",
        nargs="?",
        action="store",
        help="Basic action type for buying an item.",
    )
    # sell instruction
    instruction.add_argument(
        "sell",
        nargs="?",
        action="store",
        help="Basic action type for selling an item.",
    )
    # report instruction
    instruction.add_argument(
        "report",
        nargs="?",
        action="store",
        help="Basic action type for getting a report.",
    )

    reports = parser.add_argument_group("reports")
    # get the report for today
    reports.add_argument(
        "--today",
        "-t",
        action="store_true",
        required=False,
        help="Get the requested report for today",
    )
    # get the report for yesterday
    reports.add_argument(
        "--yesterday",
        "-y",
        action="store_true",
        required=False,
        help="Get the requested report for yesterday",
    )

    # advance the date by x argument
    parser.add_argument(
        "--advance-time",
        "-adv",
        metavar="Advance day",
        type=int,
        action="store",
        help="To advance the current day by [int]",
    )

    # product name argument
    product = parser.add_argument_group("product")
    product.add_argument(
        "--product-name",
        "-prod",
        required=False,
        type=str,
        action="store",
        help="",
    )

    # product price argument
    product.add_argument(
        "--price",
        required=False,
        type=float,
        action="store",
        help="",
    )

    return parser
