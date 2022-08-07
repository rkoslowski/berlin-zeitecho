import time
import bs4
import requests
from urllib import request
from requests.exceptions import HTTPError
import webbrowser as wb
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def check_url(url):
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            print(f'Other error occurred: {err}')  
        else:
            a = 0

def randomize_time():
    return random.randint(90, 120)

def get_available_appointment_links_this_month(response):
    body = bs4.BeautifulSoup(response.content, features="html.parser")
    links = body.select('.calendar-month-table')[0].select('td.buchbar a')
    print('found:', len(links), 'this month')
    if links:
        for link in links[:10]:
            if 'href' in link.attrs:
                day = int(link.text.strip()) 
                found = True
                print('{}: http://service.berlin.de{} '.format(day, link.attrs['href']))
                ext_link = "http://service.berlin.de" + link.attrs['href']
                print(ext_link)
                if found:
                    return day
                    #open_in_browser(ext_link)
                else:
                    return 0
    else:
        return 0

def get_available_appointment_links_next_month(response):
    body = bs4.BeautifulSoup(response.content, features="html.parser")
    links = body.select('.calendar-month-table')[1].select('td.buchbar a')
    print('found:', len(links), 'next month')
    if links:
        for link in links[:10]:
            day = int(link.text.strip())
            found = True
            #print('{}: http://service.berlin.de{} '.format(day, link.attrs['href']))
            ext_link = "http://service.berlin.de" + link.attrs['href']
            print(ext_link)
            if found:
                return day
                #open_in_browser(ext_link)
            else:
                return 0
    else:
        return 0

# opens the target link in the browser
def open_in_browser(link):
    wb.open_new_tab(link)

# defines the type of service to check for available appointments
# the booleans are to be set as the only input parameter
# i really didnt want to make an gui...
def get_servic_type():
    anmeldung_einer_wohnung     = True
    personal_id_beantragen      = False
    reisepass_beantragen        = False
    if(anmeldung_einer_wohnung):
        return 'https://service.berlin.de/dienstleistung/120686/'
    elif (personal_id_beantragen):
        return 'https://service.berlin.de/dienstleistung/120703/'
    else:
        return 'https://service.berlin.de/dienstleistung/121151/'

def get_long_link():
    # servicelink : https://service.berlin.de/dienstleistung/xxxxxx/
    servicelink = get_servic_type()
    try:
        response = requests.get(servicelink)
        response.raise_for_status()
    except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6

    body = bs4.BeautifulSoup(response.content, 'html.parser')

    if(body.find('div', class_='zmstermin-multi inner')):

        bodyclass = body.find('a', class_='btn')
        link = bodyclass.attrs['href']
        return link
    else:
        print('required element not found')
        exit()

# wait a random time between 90 to 120 sec to prevent the webserver to refuse connection (for ddos)
def sleep_til_next_request():
    time.sleep(randomize_time())


def get_response(url):
    return requests.get(url)


def try_get_app(longurl):
    # capture url request-response
    response = get_response(longurl)
    day_this = get_available_appointment_links_this_month(response)
    day_next = get_available_appointment_links_next_month(response)
    if (day_this != 0):
        return day_this
    elif(day_next != 0):
        return day_next
    else:
        return 0

def browser_emulation():

    browser = webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")
    type = get_servic_type()

    browser.get('https://duckduckgo.com')

    searchbar = browser.find_element(By.ID, 'search_form_input_homepage')

    searchbar.send_keys('www.service.berlin.de' + Keys.RETURN)

    #mainwebpage = browser.find_element(By.XPATH("//a[@href='service.berlin.de']"))
    
    browser.get("https://service.berlin.de/")

    browser.get(type)

    searchbtn = browser.find_element(By.PARTIAL_LINK_TEXT, 'berlinweit').click()

    #browser.get(type)