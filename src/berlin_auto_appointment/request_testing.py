import time
from tkinter import E
from urllib import request
from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import webbrowser as wb


import helper_functions as hf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




hf.browser_emulation()


exit()

browser = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")

browser.get('https://service.berlin.de/dienstleistung/120703/')

searchbtn = browser.find_element(By.PARTIAL_LINK_TEXT, 'berlinweit')
#elem.send_keys('seleniumhq' + Keys.RETURN)
elem.click()

url = hf.get_long_link()

response = requests.get(url)

link, day = hf.get_available_appointment_links_this_month(response)

daybtn = browser.find_element(By.PARTIAL_LINK_TEXT, day)

#browser.quit()