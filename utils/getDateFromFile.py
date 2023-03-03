from datetime import datetime


def getDateFromFile():
    with open("./day/day.txt") as f:
        line = "".join(f.readline().split("-"))
        day = datetime.strptime(line, "%d%m%Y").date()
    return day
