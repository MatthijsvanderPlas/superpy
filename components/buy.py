import csv
import sys
import random
from datetime import timedelta
from console import console
from utils.getDateFromFile import getDateFromFile
from utils.utils import appendRowToBoughtCsv, appendRowToInventoryCsv

sys.path.insert(0, "../csv")
sys.path.insert(0, "../utils")


def handleBuy(parserInfo):
    newId = random.randint(1, 10000000)
    name = parserInfo.name.lower()
    price = parserInfo.price
    amount = parserInfo.amount
    inputExpiration = parserInfo.expiration
    # Get the current day from file to set the expiration date
    day = getDateFromFile()
    expiration = day + timedelta(days=inputExpiration)

    try:
        # Write new product to the inventory
        # Append line to bought.csv
        appendRowToBoughtCsv(newId, name, day, price, amount, expiration)

        # Append line to inventory.csv
        appendRowToInventoryCsv(newId, name, amount)

        console.print("[blue bold]OK")
    except:
        print("An exception occurred")
