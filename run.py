"""
	AUTHOR: Daniel Fitzpatrick
	HOW TO RUN: python scraper.py -f [path to .env]
			EG: python scraper.py -f /opt/test/.env
				python scraper.py -f /opt/test/
				python scraper.py -f /opt/test
"""

import urllib.request as req
from html.parser import HTMLParser
import pandas as pd
import sys
import os
import boto3
import logging
from bs4 import BeautifulSoup

MINOR_URL = "https://www.bunrattychess.com/dbase/entry_list_minor.php?tbl_name=entry_list"

"""
	Scrape the Ratty Minor List for ratings
"""
with req.urlopen(MINOR_URL) as response:
	html = response.read()
	soup = BeautifulSoup(html)

	table = soup.find("table", {"class": "TFtable"})
	print(table)
	rows = table.findAll(lambda tag: tag.name=='tr')

	for row in rows:
		print("____________________________________")
		print(row)
