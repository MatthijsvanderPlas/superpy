import csv
import sys
import random
from datetime import timedelta
from utils.getDateFromFile import getDateFromFile

sys.path.insert(0, "../csv")
sys.path.insert(0, "../utils")


def handleBuy(name, price, amount, expiration):
    # Get the current day from file to set the expiration date
    day = getDateFromFile()
    expiration = day + timedelta(days=expiration)

    # Write new product to the inventory
    with open("./csv/inventory.csv", "a", newline="") as inv:
        writer = csv.writer(inv, delimiter=",")
        id = random.randint(1, 10000000)
        writer.writerow([id, name, day, price, amount, expiration])
    print("Succes!")
