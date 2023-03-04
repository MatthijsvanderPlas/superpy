from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from utils.utils import (
    getAllItemsFromSoldCsvByDate,
    getRevenueFromSoldItemsList,
)
from console import console


def handleRevenueRequest(input, date=None):

    if input == "today":
        day = getDateFromFile("str")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalRevenue = getRevenueFromSoldItemsList(soldItems)
        console.print(f"Today's revenue so far: {totalRevenue}")

    if input == "yesterday":
        day = getDateFromFile("date")
        day = day + timedelta(days=-1)
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalRevenue = getRevenueFromSoldItemsList(soldItems)
        console.print(f"Yesterdays revenue: {totalRevenue}")

    if input == "date":
        print(f"Entered date: {date}")
