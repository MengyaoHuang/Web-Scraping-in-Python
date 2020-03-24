# package use
import pandas as pd
import pickle
import glob
import numpy as np

import warnings
warnings.filterwarnings("ignore")
from collections import Counter

import requests
import urllib
import urllib.request
import time
import re
import string
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pandas as pd
import re
from datetime import datetime, timedelta

# login Amazon id and password
id = "111"
pw = "111"

# imdb extraction function
def imdblink_extraction(url_):
    filter_out_textList = np.nan
    try:
        response = requests.get(url_)
        soup = BeautifulSoup(response.text, "html.parser")
        filter_out = soup.select("a[href^='/search/title?genres=']")
        filter_out_textList = [filter_out[i].text for i in range(len(filter_out))]
    except:
        pass
    return filter_out_textList

# log-in needed link collection
def login_link_extraction(url_):
    result_link = np.nan
    try:
        response = requests.get(url_)
        soup = BeautifulSoup(response.text, "html.parser")
        filter_out = soup.find_all("a", href=re.compile("ref_=mojo_rl_summary&rf=mojo_rl_summary"))
        result_link = filter_out[0]['href']
    except:
        pass
    return result_link

def extract_movie_id(url_text):
    # in case there are nan values
    result_id = np.nan
    try:
        a, b = url_text.find('https://pro.imdb.com/title/'), url_text.find('?ref_=mojo_rl_summary')
        length_a = len("https://pro.imdb.com/title/")
        result_id = url_text[a+length_a:b]
    except:
        pass
    return result_id

# create dictionary for movie name and BoxOfficeMojo link
def movie_link_dictionary(url_, numberOfMovies=200):
  result_dic = {}
  response = requests.get(url_)
  soup = BeautifulSoup(response.text, "html.parser")
  # filter and extract
  # table_list = soup.select("a[href^='/?ref_=bo_yld_table_']")
  table_list = soup.find_all("a", href=re.compile("ref_=bo_yld_table_"))
  for i in range(numberOfMovies):
    movie_name = table_list[i].text
    # check if existing name
    if movie_name in result_dic:
      movie_name = movie_name + " other version"
    result_dic[movie_name] = "https://www.boxofficemojo.com" + table_list[i]['href']
  print("dictionary successfully generate!")
  return result_dic

# collection and dataframe formation
def dic_to_frame(url_, year):
  temp_dic = movie_link_dictionary(url_)
  temp_frame = pd.DataFrame(list(temp_dic.items()), columns=['bomtitle', 'bomlink'])
  temp_frame['year'] = year
  return temp_frame

# chrome driver setup
def launch_selenium(name="tt0170016"):
    from selenium.webdriver.common.by import By
    # mv chrome driver from Downloads to Applications
    # chromedriver = "D:/chromedriver"
    chromedriver = "chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    # Temp url address for login session
    url = 'https://pro.imdb.com/title/' + name + '?ref_=mojo_rl_summary&rf=mojo_rl_summary'
    opts = webdriver.ChromeOptions()
    opts.add_argument("user-agent=[user-agent string]")
    opts.add_argument("Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36")
    driver = webdriver.Chrome(chromedriver, chrome_options=opts)
    driver.get(url)
    # Login
    loginButton = driver.find_element_by_xpath('//a[@class="a-size- a-align- a-link- log_in"]')
    loginButton.click()
    time.sleep(.2)
    loginButton = driver.find_element_by_xpath(".//a[contains(@href,'https://pro.imdb.com/login/auth?')]")
    # loginButton = driver.find_element_by_xpath('//a[contains(@href,"https://pro.imdb.com/login/auth?")')
    # loginButton = driver.find_element(By.PARTIAL_LINK_TEXT, 'https://pro.imdb.com/login/auth?')
    loginButton.click()
    # fillin username and password to login and wait for seconds
    time.sleep(.2)
    username_form = driver.find_element_by_id("ap_email")
    username_form.send_keys(id)
    password_form = driver.find_element_by_id('ap_password')
    password_form.send_keys(pw)
    password_form.send_keys(Keys.RETURN)
    return driver

# use driver to get page source and genre info
def get_pageSource_genre(driver, dataset_, column_, id_column = 'imdb_idList'):
    for ii in range(len(dataset_)):
        filter_out_textList = np.nan
        try:
            movie_id = dataset_[id_column][ii]
            url = "https://www.imdb.com/title/" + movie_id + "/?ref_=pro_tt_visitcons"
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, features="html.parser")
            filter_out = soup.select("a[href^='/search/title?genres=']")
            filter_out_textList = [filter_out[i].text.strip() for i in range(len(filter_out))]
            # Get rid of duplicates
            filter_out_textList = sorted(list(set(filter_out_textList)))
        except:
            pass
        dataset_[column_][ii] = filter_out_textList
        # progress
        if ii % 20 == 0:
            print(ii)
    driver.quit()
    return dataset_