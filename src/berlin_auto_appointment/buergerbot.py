from msilib.schema import Error
import helper_functions as hf

def searchavailableappointments():
    # long link (including all days of a service)
    url = hf.get_long_link()
    while True:
        # verify url integrity and connection
        hf.check_url(url)

        # execute the main code to retrieve appointment-links
        try:
            day = hf.try_get_app(url)
            print(day)
            if (day < 0 or day > 31):
                raise ValueError
        except TypeError :
            print("variable day is of type ",type(day))
            print('expected int32')
            exit()
        except ValueError :
            print('variable not in boundry 1-31')
            exit()
        
        if(day != 0):
            print('emu start')
            hf.browser_emulation(day)
        elif(day == 0):
            print('gonna wait')
            # prevent serverblocking by waiting a random period of time
            hf.sleep_til_next_request()
        else:
            print("uncaught exception here")

if __name__ == '__main__':
    searchavailableappointments()