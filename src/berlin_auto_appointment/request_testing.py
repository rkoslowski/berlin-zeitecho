import time
from tkinter import E
from urllib import request
from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import webbrowser as wb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")


browser.get('https://service.berlin.de/dienstleistung/120703/')


elem = browser.find_elements(By.PARTIAL_LINK_TEXT, 'berlinweit')
#elem.send_keys('seleniumhq' + Keys.RETURN)

for i in elem:
        i.click()



#browser.quit()