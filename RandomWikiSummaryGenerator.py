import wikipediaapi
import requests
from datetime import date

# Asks for a number of random articles from Wikipedia and writes the summary to wikifile.txt

# ADD your EMAIL to wikipediaapi function.
#create a txt file or change name in wikiCall function

def wikiCall(page_name):
    wiki_wiki = wikipediaapi.Wikipedia('ForFun (YOUR_EMAIL_HERE)', 'en')

    page_py = wiki_wiki.page(page_name)

    # wikifile
    #make sure this text file exists in your directory
    wf = open('wikifile.txt', 'a')
    today = str(date.today())
    wf.write("Entry made "+today+ "\n")

    wf.write('Page - Title: %s' % page_py.title+ "\n")

    parameters = {'language': "en", 'exintro': 'True'}
    summ = wiki_wiki.extracts(page_py, params=parameters)
    # remove unencodable characters
    string_encode = summ.encode('ascii', 'ignore')
    summ_decode = string_encode.decode()

    wf.write('Page - Summary: %s' % summ_decode + '\n')

    wf.write('\n')
    wf.close()

def wikiRand():
    titlelist = []
    L = requests.Session()

    site = 'https://en.wikipedia.org/w/api.php'

    parameters = {'action': 'query', 'format': 'json', 'list': 'random', 'rnlimit': '2', 'rnnamespace': '0'}

    random = L.get(url=site, params=parameters)
    data = random.json()

    randomList = data['query']['random']

    for r in randomList:
        titlelist.append(r['title'])
    return titlelist


page_name = wikiRand()
for e in page_name:
    wikiCall(e)
