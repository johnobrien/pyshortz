'''
Created on Jul 13, 2015

@author: johno_000
'''
import requests
import json
import datetime
from time import sleep

NPR_key = "MDE5ODcyNTE2MDE0MzY4MzY2NTY1MDVjMQ001"

def get_puzzle(date):
    '''
    Get's the puzzle text for
    a given date via the NRP API.
    '''
    response = requests.get("http://api.npr.org/query?id=4473090&date={0}&dateType=story&output=JSON&apiKey=MDE5ODcyNTE2MDE0MzY4MzY2NTY1MDVjMQ001".format(date))
    d = json.loads(response.text)
    p = d["list"]["story"][0]["text"]["paragraph"]
    for text in p:
        if text["$text"].startswith("Last week's challenge:"):
            print(text["$text"])
        if text["$text"].startswith("Answer:"):
            print(text["$text"])

if __name__ == "__main__":
    date = datetime.date(2015, 6, 28)
    for _ in range(1, 100):
        date -= datetime.timedelta(7)
        try:
            get_puzzle(str(date))
        except Exception:
            pass