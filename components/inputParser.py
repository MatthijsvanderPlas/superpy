# buy a product and add to inventory
# sell a product and remove from inventory
# advance the internal date and then check for expired goods add those to the sold.csv as sold at 0
# print out different reports

import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="SuperPy",
        usage="SuperPy [buy | sell | report | advance]",
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
        "--name",
        "-n",
        metavar="PRODUCT",
        help="supply product name for the product to buy",
        required=True,
    )

    buy.add_argument(
        "--price",
        "-p",
        metavar="PRICE",
        type=float,
        help="supply the price of the product",
        required=True,
    )

    buy.add_argument(
        "--amount",
        "-a",
        metavar="[AMOUNT]",
        default=1,
        help="supply the amount of products purchased (default=1)",
    )

    buy.add_argument(
        "--expiration",
        "-e",
        metavar="[EXPIRATION]",
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
        "--name",
        "-n",
        metavar="NAME",
        help="supply product name for the product to sell",
        required=True,
    )

    sell.add_argument(
        "--price",
        "-p",
        metavar="PRICE",
        type=float,
        help="supply the price of the product",
        required=True,
    )

    sell.add_argument(
        "--amount",
        "-a",
        metavar="[AMOUNT]",
        default=1,
        help="supply the amount of products purchased (default=1)",
    )

    # advance day instruction
    advance = instruction.add_parser(
        "advance",
        help="Advance day by X days (default=1)",
    )

    advance.add_argument("advance", nargs="?", default=True)

    advance.add_argument(
        "-d",
        metavar="DAYS",
        type=int,
        default=1,
        help="Advance day by X days (default=1)",
    )

    # report instruction
    report = instruction.add_parser(
        "report",
        help="Produce several reports",
    )

    report.add_argument("report", action="store_true", default=False)

    reportSubcommands = report.add_subparsers(
        metavar="Subcommands",
        title="Report",
        help="Use [subcommand] -h to get extra info on usage of each subcommand",
    )

    inventory = reportSubcommands.add_parser("inventory", help="Show current inventory")

    inventory.add_argument(
        "inventory", action="store_true", default=False, help="Shows current inventory"
    )

    revenue = reportSubcommands.add_parser(
        "revenue", help="Show revenue for different time periods"
    )

    revenue.add_argument("revenue", action="store_true", default=False)

    revenue.add_argument(
        "--today", action="store_true", default=False, help="Returns revenue for today."
    )
    revenue.add_argument(
        "--yesterday",
        action="store_true",
        default=False,
        help="Returns revenue for yesterday.",
    )
    revenue.add_argument(
        "--date",
        "-d",
        help="Specify a certain date or period. For example '03-2020' returns profit for the month March of 2020. Other options: 01-01-2020 (full date), 02 (week number), 02-2020 (month), 2020 (year) ",
    )

    profit = reportSubcommands.add_parser(
        "profit", help="Show profit for different time periods"
    )

    profit.add_argument("profit", action="store_true", default=False)

    profit.add_argument(
        "--today", action="store_true", default=False, help="Returns profit for today."
    )
    profit.add_argument(
        "--yesterday",
        action="store_true",
        default=False,
        help="Returns profit for yesterday.",
    )
    profit.add_argument(
        "--date",
        "-d",
        help="Specify a certain date or period. For example '03-2020' returns profit for the month March of 2020. Other options: 01-01-2020 (full date), 02 (week number), 02-2020 (month), 2020 (year)",
    )

    reset = instruction.add_parser("reset", help="Reset database")

    reset.add_argument("reset", nargs="?", default=True)

    demo = instruction.add_parser("demo", help="Load dummy data to experiment")

    demo.add_argument("demo", nargs="?", default=True)

    return parser
