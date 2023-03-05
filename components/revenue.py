from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from utils.utils import (
    checkInputDate,
    getAllItemsFromSoldCsvByDate,
    getRevenueFromSoldItemsList,
)
from console import console


def handleRevenueRequest(input, date=None):

    if input == "today":
        day = getDateFromFile("str")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalRevenue = getRevenueFromSoldItemsList(soldItems)
        console.print(f"Today's revenue so far: \u20ac {totalRevenue:.2f}")

    if input == "yesterday":
        day = getDateFromFile("date")
        day = day + timedelta(days=-1)
        day = day.strftime("%d-%m-%Y")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalRevenue = getRevenueFromSoldItemsList(soldItems)
        console.print(f"Yesterdays revenue: \u20ac {totalRevenue:.2f}")

    if input == "date":
        checkInputDate(date)
