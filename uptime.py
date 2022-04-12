import sys, cfscrape, subprocess,requests
from time import sleep
from os import system
logo = """
Host			      Response Code
--------------------------------------------
"""
host = input("Host: ")
scraper = cfscrape.create_scraper()
print(logo)
for i in range(999999999999999):
	h = scraper.get('http://'""+host+"")
	sleep(0.3)
	print(f'{i}. http://'""+host+"",h)
   

