import urllib.request
import json
from datetime import datetime,timedelta
import pandas as pd

def covid19Json(*url):
    response = urllib.request.urlopen(*url)
    content = response.read()
    return(json.loads(content))

def subtractDays(date, days):
    subtracted_date = pd.to_datetime(date) - timedelta(days=days)
    subtracted_date = subtracted_date.strftime("%Y-%m-%d")

    return subtracted_date
