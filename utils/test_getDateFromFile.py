import datetime
from utils.getDateFromFile import getDateFromFile


def test_getDateFromFile():

    result = getDateFromFile()
    assert isinstance(result, datetime.date)
