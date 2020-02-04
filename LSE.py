# This script will print out URL links to news stories from the LSE RNS feed which contain a given keyword 

import urllib
import re
from bs4 import BeautifulSoup

#link to the LSE RNS and keyword. Main page needed to concatenate onto relative links. News page can be changed to filter specific types or markets.
mainPage = "https://www.londonstockexchange.com"
newsPage = urllib.urlopen("https://www.londonstockexchange.com/exchange/news/market-news/market-news-home.html?nameCodeText=&searchType=searchForNameCode&nameCode=&text=&rnsSubmitButton=Search&activatedFilters=true&newsSource=ALL&mostRead=&headlineCode=ONLY_EARNINGS_NEWS&headlineId=&ftseIndex=&sectorCode=&rbDate=released&preDate=Today&newsPerPage=500").read()
#Not sure yet if case sensituve so missing the E off Exceeding.
keyWord = "xceeding"

#Beautiful Soup scraper to find news links in the main news page (500 results)
soup = BeautifulSoup(newsPage)
for link in soup.findAll("a"):
    linkString = str(link.get("href"))
    if linkString.find("/exchange/news/market-news") > -1:
        #My crappy parser for getting the link out of the scripted href. It works....
        leftSlice = (len(linkString)-linkString.find("html"))-4
        linkString = linkString[:-leftSlice]
        rightSlice = linkString.find("/")
        linkString = linkString[rightSlice:]
        #Now we need to read each page and search for the keyword. If it finds it it'll return a number greater than -1. In that case print the URL to the news story
        pageSub = urllib.urlopen(mainPage+linkString).read()
        soupSub = BeautifulSoup(pageSub)
        soupSub = str(soupSub)
        if soupSub.find(keyWord) > -1:
            print mainPage+linkString



