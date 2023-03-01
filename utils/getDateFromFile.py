from datetime import datetime


def getDateFromFile():

    # Get the current day from file to set the sell date
    with open("./day/day.txt") as f:
        line = "".join(f.readline().split("-"))
        day = datetime.strptime(line, "%Y%m%d").date()
    return day
