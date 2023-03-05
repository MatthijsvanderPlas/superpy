from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from utils.utils import (
    getAllItemsFromSoldCsvByDate,
    getProfitFromSoldItemsList,
)
from console import console


def handleProfitRequest(input, date=None):

    if input == "today":
        day = getDateFromFile("str")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalProfit = getProfitFromSoldItemsList(soldItems)
        console.print(f"Today's profit so far: \u20ac {totalProfit:.2f}")

    if input == "yesterday":
        day = getDateFromFile("date")
        day = day + timedelta(days=-1)
        day = day.strftime("%d-%m-%Y")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalProfit = getProfitFromSoldItemsList(soldItems)
        console.print(f"Yesterdays profit: \u20ac {totalProfit:.2f}")

    if input == "date":
        print(f"Entered date: {date}")
