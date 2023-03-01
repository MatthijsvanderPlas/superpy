import csv
import sys
from console import console, err_console
from utils.getDateFromFile import getDateFromFile

sys.path.insert(0, "../csv")


def handleSell(parserInfo):
    name = parserInfo.name_product
    price = parserInfo.price
    amount = parserInfo.amount
    # set boolean isInStock to false
    isInStock = False
    # set boolean amountInStock to 0
    amountInStock = 0

    # Get the current day from file to set the sell date
    day = getDateFromFile()

    # Check if the product is in Stock and if there is enough in stock to meet the sell.
    with open("./csv/inventory.csv") as inv:
        lines = csv.DictReader(inv)
        for line in lines:
            if line["name_product"] == name:
                isInStock = True
                amountInStock += int(line["amount"])

    # Write down the sell into the sold.csv
    if isInStock:
        # get info from the bought.csv and then note the sale in sold.csv plus adjust the inventory
        with open("./csv/sold.csv", "a", newline="") as s:
            writer = csv.writer(s, delimiter=",")
            writer.writerow([id, name, day, price, amount])

    else:
        err_console.print("ERROR: Product not in stock")
