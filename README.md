# LSE-Scraper
Scrapes keywords from LSE RNS Feed


## Background

The story behind this is that I like to trade on good news. I'm not a fan of chartist theory. Although I know it works for a lot of people I find it tiresome. I like to see a company doing well and invest over short/medium term. That's always been the way I've picked stocks and so far so good! The trouble is that I spend a lot of time going through the RNS feed in the morning to find good news in trading updates and company results. Anyone who has done this knows it takes a lot of time, early in the morning. Wouldn't it be great if I autmatically knew which stories contained good news? Wouldn't it be great if I could make a quick assessment of the morning RNS feed leaving myself plenty of time to do some due dilligence and choose whether to jump on for a quick ride to profit town? I wrote this script to make that process as easy as possible. I'm going to paper trade it for the first week or so and see how it goes.

If you found this through one of my posts on a bulletin board or forum and you don't know how to use python get in touch. This is super easy to use. I'd be happy to help you get up and running with it.

## Information

Libraries required are bs4, urlib, re, datetime and logging. I can't remember which are installed as standard. 

Running will create a log file of the same name in the same directory with the date/time and keywords appended. It will contain a list of URL links by market (FTSE100, FTSE250 and FTSE AIM) to the news stories in the LSE RNS feed which contain the keyword entered at the top of the script. These are currently set to keyword = "xceed" for exceed or exeeding and keyword2 = "head of expect" for ahead of expectations.

Once run you can open the log file and click through the links to assess each nes story which contains the given keywords.

## Future plans 

  1) ~seperate results by market (AIM, FTSE100 etc) and save URLs to a file.~
  
  2) ~add multiple keywords~
  
  3) Schedule to run regularly and pick up all stories as they come out
  
  4) possibly run some sort of machine learning algorithm on the results to gauge sentiment
  
  5) email the file out at say 6:30, 12:00 and 16:00 every weekday with the results
  
# Final Note

I am a relativley basic Python user who mostly uses python as a Spatial ETL tool. My experience of web scraping is limited. If you feel I've done something wrong or you have ideas to improve the script suggestions and feedback are welcome.
