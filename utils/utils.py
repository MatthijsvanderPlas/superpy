import csv
from datetime import datetime

from utils.getDateFromFile import getDateFromFile


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


def resetBought():
    with open("./csv/bought.csv", "w") as inv:
        writer = csv.writer(inv)
        writer.writerow(["id", "name", "buy_date", "price", "amount", "expiration"])


def resetSold():
    with open("./csv/sold.csv", "w") as inv:
        writer = csv.writer(inv)
        writer.writerow(["id", "name", "amount", "sell_date", "sell_price"])


def resetDay():
    with open(
        "./day/day.txt",
        "w",
    ) as day:
        writer = csv.writer(day, lineterminator="")
        writer.writerow(["01-01-2020"])


def resetAll():
    resetBought()
    resetInventory()
    resetSold()
    resetDay()


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


def getItemFromBoughtCsvById(inputId):
    with open("./csv/bought.csv") as inv:
        lines = csv.DictReader(inv)
        for line in lines:
            if int(line["id"]) == int(inputId):
                return line


def getAllItemsFromSoldCsvByDate(inputDate):
    sold = []
    with open("./csv/sold.csv") as s:
        lines = csv.DictReader(s)
        for line in lines:
            if line["sell_date"] == inputDate:
                sold.append(line)
    return sold


def checkForItemsExpired():
    newLines = []
    day = getDateFromFile("date")
    with open("./csv/inventory.csv") as inv:
        lines = csv.DictReader(inv)
        for line in lines:
            item = getItemFromBoughtCsvById(int(line["id"]))
            expirationDate = datetime.strptime(item["expiration"], "%d-%m-%Y").date()
            if day > expirationDate:
                # product expired (sell at price 0)
                removeLineFromInventoryCsv(int(line["id"]))
                writeLineToSoldCsv(
                    line["id"], line["name"], line["amount"], expirationDate, 0
                )
            else:
                newLines.append(line)

    resetInventory()
    for line in newLines:
        appendRowToInventoryCsv(line["id"], line["name"], line["amount"])


def getProfitFromSoldItemsList(soldList):
    totalSold = 0
    totalBought = 0

    for item in soldList:
        totalSold += float(item["amount"]) * float(item["sell_price"])
        buyPrice = getItemFromBoughtCsvById(item["id"])["price"]
        totalBought += round(float(item["amount"]) * float(buyPrice), 2)

    totalProfit = totalSold - totalBought
    return totalProfit


def getRevenueFromSoldItemsList(soldList):
    totalSold = 0

    for item in soldList:
        totalSold += float(item["amount"]) * float(item["sell_price"])

    return totalSold
