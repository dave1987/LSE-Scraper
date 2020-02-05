# LSE-Scraper
Scrapes keywords from LSE RNS Feed

Needs bs4, re and urllib libraries installed

Running will print out a list of URL links to the news stories in the LSE RNS feed which contain the keyword entered at the top of the script.

Future plans for this script are to: 
  ~1) seperate results by market (AIM, FTSE100 etc) and save URLs to a file.~
  2) add multiple keywords
  3) Schedule to run regularly and pick up all stories as they come out
  5) possibly run some sort of machine learning algorithm on the results to gauge sentiment
  6) email the file out at say 6:30, 12:00 and 16:00 every weekday with the results
  
  
Note: I am a relativley basic Python user who mostly uses python as a Spatial ETL tool. My experience of web scraping is limited. Suggestions and feedback are welcome.


Edit 05/02/2020

I have added logging and sperate sections for different markets
