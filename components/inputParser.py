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
    instruction = parser.add_subparsers(
        metavar="Subcommands",
        title="SuperPy",
        help="Use [subcommand] -h to get extra info on usage of each subcommand",
    )
    # buy instruction
    buy = instruction.add_parser(
        "buy",
        help="Basic action type for buying an item.",
    )

    buy.add_argument("buy", nargs="?", default=True)

    buy.add_argument(
        "--name_product",
        "-n",
        help="supply product name for the product to buy",
        required=True,
    )

    buy.add_argument(
        "--price",
        "-p",
        help="supply the price of the product",
        required=True,
    )

    buy.add_argument(
        "--amount",
        "-a",
        default=1,
        help="supply the amount of products purchased (default=1)",
    )

    buy.add_argument(
        "--expiration",
        "-e",
        type=int,
        default=10,
        help="supply the amount in days of the shelf life of a product (default=10)",
    )

    sell = instruction.add_parser(
        "sell",
        help="Basic action type for selling an item.",
    )

    sell.add_argument("sell", nargs="?", default=True)

    sell.add_argument(
        "--name_product",
        "-n",
        help="supply product name for the product to sell",
        required=True,
    )

    sell.add_argument(
        "--price",
        "-p",
        help="supply the price of the product",
        required=True,
    )

    sell.add_argument(
        "--amount",
        "-a",
        default=1,
        help="supply the amount of products purchased (default=1)",
    )

    # advance day instruction
    parser.add_argument(
        "--advance-date",
        "-d",
        type=int,
        default=1,
        help="Advance day by X days (default=1)",
    )

    return parser
