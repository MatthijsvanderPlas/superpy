import csv
from functools import reduce
import sys
from datetime import datetime
from console import console, err_console
from utils.getDateFromFile import getDateFromFile
from utils.utils import (
    adjustLineInInventoryCsv,
    getAllItemsByNameFromInventoryCsv,
    removeLineFromInventoryCsv,
    writeLineToSoldCsv,
)

sys.path.insert(0, "../csv")


def handleSell(inputObj):
    name = inputObj.name.lower()
    price = inputObj.price
    amount = int(inputObj.amount)
    sold = 0

    # Get the current day from file to set the sell date
    day = getDateFromFile()

    # Go through the inventory and get the lines that meet the product_name
    inStock = getAllItemsByNameFromInventoryCsv(name)
    # Check how much of the item is in stock.
    inStockAmount = reduce(lambda x, y: x + y, [d["amount"] for d in inStock], 0)

    # Loop that handles the selling of the products till either the order was fulfilled or the stock ran out.
    while amount > 0:
        if inStock:
            for stock in inStock:
                # the amount is higher than what is in stock
                if amount > stock["amount"] and inStockAmount != 0:
                    if amount == stock["amount"]:
                        console.print("[blue bold]OK")
                    amount -= stock["amount"]
                    inStockAmount -= stock["amount"]
                    sold += stock["amount"]
                    # remove the line from the inventory.csv and write the into sell.csv
                    writeLineToSoldCsv(stock["id"], name, stock["amount"], day, price)
                    removeLineFromInventoryCsv(int(stock["id"]))
                    continue
                elif inStockAmount == 0:
                    err_console.print(f"You were only able to buy {sold}")
                    amount = 0
                    break
                else:
                    writeLineToSoldCsv(stock["id"], name, amount, day, price)
                    if amount == stock["amount"]:
                        removeLineFromInventoryCsv(int(stock["id"]))
                    else:
                        adjustLineInInventoryCsv(int(stock["id"]), amount)
                    # Set amount to 0 to reset the loop as the purchase has been fulfilled
                    amount = 0
                    sold += amount
                    console.print("[blue bold]OK")
                    break
        else:
            err_console.print("ERROR: Product not in stock.")
            break
