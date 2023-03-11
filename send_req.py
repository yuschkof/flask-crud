import json
import requests


def send_request(page, from_date, to_date, tagged):
    r = requests.get(
        f"https://api.stackexchange.com/2.3/search?page={page}&from_date={from_date}&to_date={to_date}&order=desc"
        f"&sort=activity&tagged={tagged}&site=stackoverflow")
    data = json.loads(r.text)
    user = data["items"]
    return user
