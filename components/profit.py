from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from utils.utils import (
    checkInputDate,
    getAllItemsFromSoldCsvByDate,
    getProfitFromSoldItemsList,
    returnDatesForWeekNumber,
    returnTableOfItems,
)
from rich.align import Align
from console import console


def handleProfitRequest(input, date=None):

    if input == "today":
        day = getDateFromFile("str")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalProfit = getProfitFromSoldItemsList(soldItems)
        revenueTable = returnTableOfItems(soldItems, "profit")
        date = day
        profitLine = f"Today's profit so far: \u20ac {totalProfit:.2f}"

    if input == "yesterday":
        day = getDateFromFile("date")
        day = day + timedelta(days=-1)
        day = day.strftime("%d-%m-%Y")
        soldItems = getAllItemsFromSoldCsvByDate(day)
        totalProfit = getProfitFromSoldItemsList(soldItems)
        revenueTable = returnTableOfItems(soldItems, "profit")
        date = day
        profitLine = f"Yesterdays profit: \u20ac {totalProfit:.2f}"

        if input == "date":
            status = checkInputDate(date)

            if status["status"]:
                if status["type"] == "week":
                    dates = returnDatesForWeekNumber(date)
                    soldItems = getAllItemsFromSoldCsvByDate(dates)
                    totalRevenue = getProfitFromSoldItemsList(soldItems)
                    revenueTable = returnTableOfItems(soldItems, "profit")
                    profitLine = (
                        f"[blue]{date}[/blue] profit: \u20ac {totalRevenue:.2f}"
                    )
                else:
                    soldItems = getAllItemsFromSoldCsvByDate(date)
                    totalRevenue = getProfitFromSoldItemsList(soldItems)
                    revenueTable = returnTableOfItems(soldItems, "revenue")
                    profitLine = (
                        f"[blue]{date}[/blue] profit: \u20ac {totalRevenue:.2f}"
                    )
    console.rule(f"[bold green]Profit: {date}", style="red")
    console.print(Align.center(revenueTable))
    console.print(Align.center(profitLine))
