import csv
import json
from datetime import datetime, timedelta
from rich.table import Table
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


def appendRowToSoldCsv(inputId, name, amount, date, price):
    with open("./csv/sold.csv", "a", newline="") as s:
        writer = csv.writer(s, delimiter=",")
        writer.writerow([inputId, name, amount, date, price])


def resetInventory():
    with open("./csv/inventory.csv", "w") as inv:
        writer = csv.writer(inv, lineterminator="")
        writer.writerow(["id", "name", "amount"])


def resetBought():
    with open("./csv/bought.csv", "w") as inv:
        writer = csv.writer(inv, lineterminator="")
        writer.writerow(["id", "name", "buy_date", "price", "amount", "expiration"])


def resetSold():
    with open("./csv/sold.csv", "w") as inv:
        writer = csv.writer(inv, lineterminator="")
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
            if inputDate in line["sell_date"]:
                sold.append(line)
                continue
    return sold


def getAllItemsFromSoldCsvByDateArray(inputDate):
    sold = []
    with open("./csv/sold.csv") as s:
        lines = csv.DictReader(s)
        for line in lines:
            if line["sell_date"] in inputDate:
                sold.append(line)
                continue
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
                appendRowToSoldCsv(
                    line["id"],
                    line["name"],
                    line["amount"],
                    expirationDate.strftime("%d-%m-%Y"),
                    0,
                )
            else:
                newLines.append(line)

    # "Update" the inventory
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


def checkInputDate(inputDate):

    if len(inputDate) == 2:
        if int(inputDate) in range(0, 52):
            return {"status": True, "type": "week"}

    if len(inputDate) == 4:
        if int(inputDate) in range(2020, 2050):
            return {"status": True, "type": "year"}

    if len(inputDate) == 7:
        correctDate = None
        arrayDate = inputDate.split("-")

        try:
            newDate = (arrayDate[1], arrayDate[0])
            correctDate = True
        except ValueError:
            correctDate = False

        return {"status": correctDate, "type": "month"}

    if len(inputDate) == 10:
        correctDate = None
        arrayDate = inputDate.split("-")

        try:
            newDate = (arrayDate[2], arrayDate[1], arrayDate[0])
            correctDate = True
        except ValueError:
            correctDate = False

        return {"status": correctDate, "type": "date"}


def returnDatesForWeekNumber(week):
    day = getDateFromFile("str").split("-")
    startdate = datetime.strptime(f"1-{week}-{day[2]}", "%w-%W-%Y")
    dates = [startdate.strftime("%d-%m-%Y")]
    for i in range(1, 7):
        day = startdate + timedelta(days=i)
        dates.append(day.strftime("%d-%m-%Y"))
    return dates


def loadDemoData():
    # Set the date
    with open("./day/day.txt", "w") as day:
        day.write("22-01-2020")

    f = open("./demo/demodata.json")
    data = json.load(f)
    # Fill Bought.csv
    for item in data["bought"]:
        appendRowToBoughtCsv(
            item["id"],
            item["name"],
            item["buy_date"],
            item["price"],
            item["amount"],
            item["expiration"],
        )
    # Fill Sold.csv
    for item in data["sold"]:
        appendRowToSoldCsv(
            item["id"],
            item["name"],
            item["amount"],
            item["sell_date"],
            item["sell_price"],
        )
    # Fill Inventory.csv
    for item in data["inventory"]:
        appendRowToInventoryCsv(item["id"], item["name"], item["amount"])


def returnTableOfItems(data, type):
    table = Table(min_width=100)

    table.add_column("Product Name", style="magenta", no_wrap=True)
    table.add_column("Amount", justify="center", style="blue", no_wrap=True)
    if type != "revenue":
        table.add_column("Buy Price", justify="right", style="green", no_wrap=True)
    table.add_column("Sell Price", justify="right", style="green", no_wrap=True)
    table.add_column(
        "Date of Purchase/Expired", justify="center", style="yellow", no_wrap=True
    )
    for item in data:
        boughtItem = getItemFromBoughtCsvById(int(item["id"]))
        if type != "revenue":
            table.add_row(
                item["name"],
                item["amount"],
                "\u20ac " + boughtItem["price"],
                "\u20ac " + item["sell_price"],
                item["sell_date"],
            )
        else:
            table.add_row(
                item["name"],
                item["amount"],
                "\u20ac " + item["sell_price"],
                item["sell_date"],
            )

    return table
