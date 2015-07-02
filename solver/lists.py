'''
Created on Jun 30, 2015

I'm thinking evenutally we'll start reusing our lists,
and the functions we're using to create lists of things.

So, I figure, let's start sticking them all in a "lists" module.

@author: Leiran Biton, John O'Brien
'''

from solver.word import strip_accents
import requests
import re


def get_companies():
    page = requests.get('https://www.sec.gov/rules/other/4-460list.htm')
    content = strip_accents(str(page.text))
    companies = re.findall(r'<TD>(.*?)\n</TD>', content)
    for company in companies:
        yield company.lower()

def get_musicians():
    urls = ['https://en.wikipedia.org/wiki/Category:American_pop_singers',
            'https://en.wikipedia.org/w/index.php?title=Category:American_pop_singers&pagefrom=Edner%2C+Bobby%0ABobby+Edner#mw-pages',
            'https://en.wikipedia.org/w/index.php?title=Category:American_pop_singers&pagefrom=Lamond%2C+George%0AGeorge+Lamond#mw-pages',
            'https://en.wikipedia.org/w/index.php?title=Category:American_pop_singers&pagefrom=Ponce+Sisters%2C+The%0AThe+Ponce+Sisters#mw-pages',
            'https://en.wikipedia.org/w/index.php?title=Category:American_pop_singers&pagefrom=Wallace%2C+Chris%0AChris+Wallace+%28musician%29#mw-pages']

    for url in urls:
        page = requests.get(url)
        content = strip_accents(str(page.text))
        musicians = re.findall(r'">(.*?)</a>', content)
        for musician in musicians:
            yield musician.lower()
