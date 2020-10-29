from bs4 import BeautifulSoup
import requests
a = 'https://www.cricbuzz.com/live-cricket-scores/20714/eng-vs-ire-only-test-ireland-tour-of-england-only-test-2019'
url=requests.get(a)
b=url.text
c=BeautifulSoup(b,'html.parser') #parse - take html functions
for i in c.find_all('div',{'class':"cb-col cb-col-67 cb-scrs-wrp"}):
   print(i.text)
