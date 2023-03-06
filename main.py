# Imports
from components.inputParser import create_parser
from components.inventory import displayCurrentInventory
from components.profit import handleProfitRequest
from components.revenue import handleRevenueRequest
from utils.advanceDate import advance
from utils.utils import checkForItemsExpired, loadDemoData, resetAll
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
        # advance the date
        advance(parsed.d)
        # check for items that might have gone out of date and handle accordingly
        checkForItemsExpired()

    if hasattr(parsed, "report"):
        if hasattr(parsed, "inventory"):
            displayCurrentInventory()

        if hasattr(parsed, "revenue"):
            if parsed.today:
                handleRevenueRequest("today")
            elif parsed.yesterday:
                handleRevenueRequest("yesterday")
            elif parsed.date:
                handleRevenueRequest("date", parsed.date)
            else:
                handleRevenueRequest("today")

        if hasattr(parsed, "profit"):
            if parsed.today:
                handleProfitRequest("today")
            elif parsed.yesterday:
                handleProfitRequest("yesterday")
            elif parsed.date:
                handleProfitRequest("date", parsed.date)
            else:
                handleProfitRequest("today")

    if hasattr(parsed, "reset"):
        resetAll()

    if hasattr(parsed, "demo"):
        loadDemoData()


if __name__ == "__main__":
    main()
