from utils.getDateFromFile import getDateFromFile
from utils.utils import getAllItemsFromSoldCsvByDate, getItemFromBoughtCsvById
from console import console


def handleProfitRequest(input):

    if input == "today":
        day = getDateFromFile("str")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalSold = 0
        totalBought = 0

        for item in soldItems:
            totalSold += float(item["amount"]) * float(item["sell_price"])
            buyPrice = getItemFromBoughtCsvById(item["id"])["price"]
            totalBought += round(float(item["amount"]) * float(buyPrice), 2)

        totalProfit = totalSold - totalBought
        console.print(f"Today's revenue so far: {totalProfit}")
