import csv
import sys
import random
from datetime import datetime, timedelta

sys.path.insert(0, "../csv")


def handleBuy(name, price, amount, expiration):
    with open("./day/day.txt") as f:
        line = "".join(f.readline().split("-"))
        day = datetime.strptime(line, "%Y%m%d").date()
        expiration = day + timedelta(days=expiration)

    with open("./csv/inventory.csv", "a", newline="") as inv:
        writer = csv.writer(inv, delimiter=",")
        id = random.randint(1, 10000000)
        writer.writerow([id, name, day, price, amount, expiration])
    print("Succes!")
