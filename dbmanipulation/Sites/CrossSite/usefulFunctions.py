import datetime
from time import strftime

def string_from_date(thisdate = datetime.datetime.now()):
    return thisdate.strftime("%Y%m%d%H%M%S")

def sqldate_format(thisdate  = datetime.datetime.now()):
    return thisdate.strftime('%Y-%m-%d %H:%M:%S')