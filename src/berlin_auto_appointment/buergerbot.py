# import subprocess
import time
import requests
import helper_functions as hf

def searchavailableappointments():
    url = hf.get_appointment_link()
    while True:
        # verify url integrity and connection
        hf.check_url(url)

        # capture url request-response
        response = hf.get_response(url)

        # execute the main code to retrieve appointment-links
        hf.try_get_app(response)
        
        # prevent serverblocking by waiting a random period of time
        hf.sleep_til_next_request()

if __name__ == '__main__':
    searchavailableappointments()