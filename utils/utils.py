import csv


def appendRowToBoughtCsv(inputId, name, day, price, amount, expiration):
    with open("./csv/bought.csv", "a", newline="") as inv:
        writer = csv.writer(inv, delimiter=",")
        writer.writerow([inputId, name, day, price, amount, expiration])


def appendRowToInventoryCsv(inputId, name, amount):
    with open("./csv/inventory.csv", "a", newline="") as inv:
        writer = csv.writer(inv, delimiter=",")
        writer.writerow([inputId, name, amount])


def adjustLineInInventoryCsv(inputId, amount):
    newLines = []
    with open("./csv/inventory.csv", "r+") as inv:
        lines = csv.DictReader(inv)
        for line in lines:
            if int(line["id"]) == inputId:
                newLines.append(
                    {
                        "id": line["id"],
                        "name": line["name"],
                        "amount": int(line["amount"]) - amount,
                    }
                )
            else:
                newLines.append(line)

    resetInventory()
    for line in newLines:
        appendRowToInventoryCsv(line["id"], line["name"], line["amount"])


def removeLineFromInventoryCsv(inputId):
    newLines = []
    with open("./csv/inventory.csv", "r+") as inv:
        lines = csv.DictReader(inv)
        for line in lines:
            if int(line["id"]) != inputId:
                newLines.append(line)

    resetInventory()
    for line in newLines:
        appendRowToInventoryCsv(line["id"], line["name"], line["amount"])


def writeLineToSoldCsv(inputId, name, amount, date, price):
    with open("./csv/sold.csv", "a", newline="") as s:
        writer = csv.writer(s, delimiter=",")
        writer.writerow([inputId, name, amount, date, price])


def resetInventory():
    with open("./csv/inventory.csv", "w") as inv:
        writer = csv.writer(inv)
        writer.writerow(["id", "name", "amount"])


def getAllItemsByNameFromInventoryCsv(name) -> list:
    inStock = []
    with open("./csv/inventory.csv") as inv:
        lines = csv.DictReader(inv)
        for line in lines:
            if line["name"] == name:
                inStock.append(
                    {
                        "id": int(line["id"]),
                        "name": line["name"],
                        "amount": int(line["amount"]),
                    }
                )
    return inStock
