from datetime import datetime, timedelta
from utils.getDateFromFile import getDateFromFile
from console import console, err_console


def advance(days):
    day = getDateFromFile("date")
    try:
        with open("./day/day.txt", "w") as f:
            newDay = day + timedelta(days=days)
            euDay = newDay.strftime("%d-%m-%Y")
            console.print(f"[green]Current day set to: {euDay}")
            f.write(euDay)
        console.print("[blue bold]OK")
    except:
        err_console.print("Failure!")
