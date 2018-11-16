import selenium.webdriver
import os
class WinChrome(object):
        def __init__(self):
                options = selenium.webdriver.ChromeOptions()
                #options.add_argument('--use-fake-ui-for-media-stream')
                #options.add_argument('--use-fake-device-for-media-stream')
                #options.add_argument('disable-gpu')
                options.add_argument('--disable-search-geolocation-disclosure')
                options.add_argument('--disable-notifications')
                options.add_argument('--log-level=3')
                #a_path = os.path.abspath('drivers/chromedriver.exe')
                #print (a_path)
                a_path = 'C:/Users/sukhov/Desktop/taxi-yandex-ru/drivers/chromedriver.exe'
                self.chrome_driver = selenium.webdriver.Chrome(a_path)#, options=options)
                self.chrome_driver.implicitly_wait(30)


        def return_driver(self):
                return self.chrome_driver