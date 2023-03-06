from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from utils.utils import (
    checkInputDate,
    getAllItemsFromSoldCsvByDate,
    getAllItemsFromSoldCsvByDateArray,
    getRevenueFromSoldItemsList,
    returnDatesForWeekNumber,
    returnTableOfItems,
)
from rich.align import Align
from components.console import console, err_console


def handleRevenueRequest(input, date=None):

    if input == "today":
        day = getDateFromFile("str")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalRevenue = getRevenueFromSoldItemsList(soldItems)
        revenueTable = returnTableOfItems(soldItems, "revenue")
        date = day
        revenueLine = f"Today's revenue so far: \u20ac {totalRevenue:.2f}"

    if input == "yesterday":
        day = getDateFromFile("date")
        day = day + timedelta(days=-1)
        day = day.strftime("%d-%m-%Y")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalRevenue = getRevenueFromSoldItemsList(soldItems)
        revenueTable = returnTableOfItems(soldItems, "revenue")
        date = day
        revenueLine = f"Yesterdays revenue: \u20ac {totalRevenue:.2f}"

    if input == "date":
        status = checkInputDate(date)
        if status == None:
            err_console.print("Please enter a valid date")
            return

        if status["type"] == "week":
            dates = returnDatesForWeekNumber(int(date) - 1)
            soldItems = getAllItemsFromSoldCsvByDateArray(dates)
            totalRevenue = getRevenueFromSoldItemsList(soldItems)
            revenueTable = returnTableOfItems(soldItems, "revenue")
            revenueLine = f"[blue]{date}[/blue] revenue: \u20ac {totalRevenue:.2f}"
        else:
            soldItems = getAllItemsFromSoldCsvByDate(date)
            totalRevenue = getRevenueFromSoldItemsList(soldItems)
            revenueTable = returnTableOfItems(soldItems, "revenue")
            revenueLine = f"[blue]{date}[/blue] revenue: \u20ac {totalRevenue:.2f}"

    console.rule(f"[bold green]Revenue: {date}", style="red")
    console.print(Align.center(revenueTable))
    console.print(Align.center(revenueLine))
