#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:32:45 2018

@author: sadvani
adapted from https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
"""

import urllib2
from bs4 import BeautifulSoup

import pandas as pd

xgPage = "https://understat.com/league/EPL"
# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(xgPage)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, ‘html.parser’)

# Take out the <div> of name and get its value
name_box = soup.find(‘league-chemp’, attrs={‘class’: ‘name’})