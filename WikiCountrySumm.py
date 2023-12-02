import wikipediaapi
import csv
import random
from datetime import date

# Chooses a random country and writes the summary section of the corresponding wikipedia article to a txt file
#



def wikiCall(page_name):
    wiki_wiki = wikipediaapi.Wikipedia('ForFun (focuswaiver7@gmail.com)', 'en')

    page_py = wiki_wiki.page(page_name)

    # wikifile
    wf = open('countryfile.txt', 'a')
    today = str(date.today())
    wf.write("Entry made "+today+ "\n")

    wf.write('Page - Title: %s' % page_py.title+ "\n")

    parameters ={'language':"en", 'exintro':'True'}
    summ = wiki_wiki.extracts(page_py, params=parameters)
    #remove unencodable characters
    string_encode = summ.encode('ascii','ignore')
    summ_decode = string_encode.decode()

    wf.write('Page - Summary: %s' % summ_decode+'\n')

    wf.write('\n')
    wf.close()

def countryChoice():
    countries_obj = []
    with open('countries.csv', newline='') as f:
        reader = csv.reader(f)
        for i in reader:
            countries_obj.append(i)
        x = random.randint(0,249)
        choiceraw = countries_obj[x]
        choice = str(choiceraw[0])
        return choice
country = countryChoice()
wikiCall(country)
