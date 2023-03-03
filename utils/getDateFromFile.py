from datetime import datetime


def getDateFromFile(type):

    if type == "str":

        with open("./day/day.txt") as f:
            line = "".join(f.readline().split("-"))
            date = datetime.strptime(line, "%d%m%Y").date()
            day = datetime.strftime(date, "%d-%m-%Y")
        return day

    if type == "date":
        with open("./day/day.txt") as f:
            line = "".join(f.readline().split("-"))
            day = datetime.strptime(line, "%d%m%Y").date()
        return day
