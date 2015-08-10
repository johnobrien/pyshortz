'''
Created on Jul 14, 2015

@author: johno_000
'''
from time import sleep
import datetime
import requests
import json
import nltk
from nltk.tokenize import word_tokenize

NPR_key = "MDE5ODcyNTE2MDE0MzY4MzY2NTY1MDVjMQ001"

# Good source of lists: https://github.com/dariusk/corpora


def get_puzzle(date):
    '''
    Get's the puzzle text for
    a given date via the NRP API.

    date is string in the format 2015-07-12
    date has to be a Sunday

    One idea from Michelle from Python meetup, use named entity extraction
    (http://www.nltk.org/book/ch07.html#fig-locations) to get the source
    and target lists (provide some training data for that).
    http://mattshomepage.com/#/blog/feb2013/liftingthehood

    Another pass to get criteria to restrict the source and target lists.
    And then parse out the middle part get the transform part of the puzzle.

    Spacy is apparently good to depency parsing.

    '''

    response = requests.get("http://api.npr.org/query?id=4473090&date={0}&dateType=story&output=JSON&apiKey=MDE5ODcyNTE2MDE0MzY4MzY2NTY1MDVjMQ001".format(date))
    d = json.loads(response.text)
    p = d["list"]["story"][0]["text"]["paragraph"]
    for text in p:
        if text["$text"].startswith("Next week's challenge:"):
            print("Date:{0}".format(date))
            sentences = nltk.sent_tokenize(text["$text"])
            sentences[0] = sentences[0][23:]
            if ("comes" and "from" and "listener") in sentences[0]:
                del sentences[0]
            for i, s in enumerate(sentences):
                print("Sentence {0}: {1}".format(i, s))
                s = word_tokenize(s)
                # print(nltk.pos_tag(s))
                # http://www.monlp.com/2011/11/08/part-of-speech-tags/
            print("\n")

if __name__ == "__main__":
    date = datetime.date(2015, 6, 28)
    for _ in range(1, 100):
        date -= datetime.timedelta(7)
        sleep(1)
        try:
            get_puzzle(str(date))
        except Exception:
            pass