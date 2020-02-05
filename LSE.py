# This script will print out URL links to news stories from the LSE RNS feed which contain a given keyword 

import urllib
import re
from bs4 import BeautifulSoup
import logging
from datetime import datetime

#START

#Add Keyword
keyWord = "xceed"
keyWord2 = "head of expect"
#link to the LSE RNS and keyword. Main page needed to concatenate onto relative links. News page can be changed to filter specific types or markets.
mainPage = "https://www.londonstockexchange.com"

#Logging Settings
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H%M")
logFileName = "LSE_"+dt_string+'_'+keyWord+'.log'
logging.basicConfig(level=logging.INFO, filename=logFileName, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

#define scraping function
def LSEScrape(newsPage):
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
            if soupSub.find(keyWord) or soupSub.find(keyWord2) > -1:
                logging.warning(mainPage+linkString)


logging.info("Scraping FTSE 100")
newsPage = urllib.urlopen("https://www.londonstockexchange.com/exchange/news/market-news/market-news-home.html?nameCodeText=&searchType=searchForNameCode&nameCode=&text=&rnsSubmitButton=Search&activatedFilters=true&newsSource=ALL&mostRead=&headlineCode=NONE&headlineId=&ftseIndex=UKX&sectorCode=&rbDate=released&preDate=Today&newsPerPage=500").read()
LSEScrape(newsPage=newsPage)

logging.info("Scraping FTSE 250")
newsPage = urllib.urlopen("https://www.londonstockexchange.com/exchange/news/market-news/market-news-home.html?nameCodeText=&searchType=searchForNameCode&nameCode=&text=&rnsSubmitButton=Search&activatedFilters=true&newsSource=ALL&mostRead=&headlineCode=NONE&headlineId=&ftseIndex=MCX&sectorCode=&rbDate=released&preDate=Today&newsPerPage=500").read()
LSEScrape(newsPage=newsPage)
 
logging.info("Scraping FTSE 350")
newsPage = urllib.urlopen("https://www.londonstockexchange.com/exchange/news/market-news/market-news-home.html?nameCodeText=&searchType=searchForNameCode&nameCode=&text=&rnsSubmitButton=Search&activatedFilters=true&newsSource=ALL&mostRead=&headlineCode=NONE&headlineId=&ftseIndex=NMX&sectorCode=&rbDate=released&preDate=Today&newsPerPage=500").read()
LSEScrape(newsPage=newsPage)

logging.info("Scraping FTSE AIM")
newsPage = urllib.urlopen("https://www.londonstockexchange.com/exchange/news/market-news/market-news-home.html?nameCodeText=&searchType=searchForNameCode&nameCode=&text=&rnsSubmitButton=Search&activatedFilters=true&newsSource=ALL&mostRead=&headlineCode=NONE&headlineId=&ftseIndex=AXX&sectorCode=&rbDate=released&preDate=Today&newsPerPage=500").read()
LSEScrape(newsPage=newsPage)

#END
