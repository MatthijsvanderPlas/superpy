# Imports
from components.inputParser import create_parser
from utils.advanceDate import advance
from components.buy import handleBuy
from components.sell import handleSell
import sys

sys.path.insert(0, "./components")


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    # Accept arguments from argparse
    parser = create_parser()
    parsed = parser.parse_args()
    # Buy command was given and now parsed
    if hasattr(parsed, "buy"):
        handleBuy(parsed)
        # displayInventory()

    if hasattr(parsed, "sell"):
        handleSell(parsed)

    if hasattr(parsed, "advance"):
        advance(parsed.d)

    if hasattr(parsed, "report"):
        if hasattr(parsed, "inventory"):
            print("Inventory")
        if hasattr(parsed, "revenue"):
            print("Revenue")
        if hasattr(parsed, "profit"):
            print("Profit")

    if hasattr(parsed, "reset"):
        print("Reset")

    if hasattr(parsed, "demo"):
        print("Load program with dummy data")


if __name__ == "__main__":
    main()
