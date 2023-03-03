from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from console import console, err_console


def advance(days):
    day = getDateFromFile()
    try:
        with open("./day/day.txt", "w") as f:
            newDay = day + timedelta(days=days)
            console.print(f"[red]Current day set to: {newDay}")
            f.write(newDay.strftime("%d-%m-%Y"))
        console.print("[blue bold]OK")
    except:
        err_console.print("Failure!")
