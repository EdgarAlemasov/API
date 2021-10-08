import datetime
import requests
from pprint import pprint


def get_questions():
    date = datetime.datetime.utcnow()
    today_date = date.replace(tzinfo=datetime.timezone.utc).timestamp()
    two_day_ago = date - datetime.timedelta(hours=1)
    two_day_ago_UTC = two_day_ago.replace(tzinfo=datetime.timezone.utc).timestamp()
    date = int(today_date)
    two_day_ago = int(two_day_ago_UTC)
    url = f'https://api.stackexchange.com/2.3/questions?fromdate={two_day_ago}&todate={date}&order=desc&sort=activity&tagged=Python&site=stackoverflow'
    response = requests.get(url=url, timeout=5)
    result = response.json()
    pprint(result)

get_questions()