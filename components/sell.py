import csv
import sys
from console import console, err_console
from utils.getDateFromFile import getDateFromFile

sys.path.insert(0, "../csv")


def handleSell(name, price, amount):
    # set boolean isInStock to false
    isInStock = False
    # set boolean isAbundant to true, later will be checked with
    isAbundant = True
    inStockAmount = 0

    # Get the current day from file to set the sell date
    day = getDateFromFile()

    # Check if the product is in Stock, if there is enough in stock to meet the sell.
    with open("./csv/inventory.csv") as inv:
        lines = csv.reader(inv)
        for line in lines:
            if line[1] == name:
                isInStock = True
                inStock = int(line[4])
                if inStock < int(amount):
                    isAbundant = False
                    inStockAmount = line[4]

    # Write down the sell into the sold.csv
    if isInStock:
        console.print("I was found and am in stock!")
        if not isAbundant:
            console.print(f"There are only {inStockAmount}, you asked for {amount}")
        console.print(name, price, amount)
    else:
        err_console.print("ERROR: Item not in stock")
    # with open("./csv/sold.csv", "a", newline="") as s:
