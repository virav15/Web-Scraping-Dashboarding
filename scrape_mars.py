#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver

def init_browser():
    executable_path = {"executable_path":"c:\drivers\chromedriver"}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    browser = init_browser()
    mars_facts_data = {}

    nasa = "https://mars.nasa.gov/news/"
    browser.visit(nasa)
    time.sleep(2)

    html = browser.html
    soup = bs(html,"html.parser")

    #scrapping latest news about mars from nasa
    news_title = soup.find("div",class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text
    mars_facts_data['news_title'] = news_title
    mars_facts_data['news_p'] = news_p
