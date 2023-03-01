import csv
import sys
from console import console, err_console
from utils.getDateFromFile import getDateFromFile

sys.path.insert(0, "../csv")


def handleSell(name, price, amount):
    # set boolean isInStock to false
    isInStock = False
    # set boolean isAbundant to true, later will be checked with
    amountInStock = 0

    # Get the current day from file to set the sell date
    day = getDateFromFile()

    # Check if the product is in Stock, if there is enough in stock to meet the sell.
    with open("./csv/inventory.csv") as inv:
        lines = csv.DictReader(inv)
        for line in lines:
            if line["name_product"] == name:
                isInStock = True
                amountInStock += int(line["amount"])

    # Write down the sell into the sold.csv
    if isInStock:
        console.print("I was found and am in stock!")
        if amountInStock < int(amount):
            console.print(f"There are only {amountInStock}, you asked for {amount}")
            console.print(name, price, amount)
        else:
            console.print(
                f"You got your {name} all {amount}. Left:  {amountInStock - int(amount)}"
            )
    else:
        err_console.print("ERROR: Product not in stock")
    # with open("./csv/sold.csv", "a", newline="") as s:
