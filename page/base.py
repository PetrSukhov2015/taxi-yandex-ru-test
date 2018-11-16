import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class PageBase(object):
    def __init__(self,driver):
        self.driver=driver
        self.url="https://taxi.yandex.ru/"
    #open base url
    def open(self):
        self.driver.get(self.url)

    def open_by_url(self,the_url):
        self.driver.get(the_url)

    # input fild find by xpath
    def feel(self,type,locator,value):
        if 'x' == type:
            self.x_feel(locator,value)
        elif 'i' == type:
            try:
                self.driver.find_element_by_id(locator).clear()
                self.driver.find_element_by_id(locator).send_keys(value)
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body').send_keys(Keys.DOWN)
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body').send_keys(Keys.END)
                
                #from selenium.webdriver.common.action_chains import ActionChains
                #ActionChains(self.driver).key_down(Keys.DOWN).perform()
                #ActionChains(self.driver).key_down(Keys.ENTER).perform()

                #self.driver.find_element_by_id(locator).send_key(Keys.DOWN)
                #self.driver.find_element_by_id(locator).send_key(Keys.ENTER)
            except:
                print('cant find element '+locator)

    # feel field by xpath
    def x_feel(self,l,v):
        try:
            self.driver.find_element_by_xpath(l).clear()
            self.driver.find_element_by_xpath(l).send_keys(v)
        except:
            print('cant find element '+l)


    def click(self,type,element):
        if 'x' == type:
            self.x_click(element)

    def x_click(self,e):
        try:
            self.driver.find_element_by_xpath(e).click()
        except:
            print('cant find element '+e)

    def find(self,type,element):
        if 'x' == type:
            return self.x_find(element)

    def x_find(self,e):
        try:
            return self.driver.find_element_by_xpath(e)
        except:
            print('cant find element '+e)
            return None
    def is_exists(self,type,e):
        if 'x' == type:
            if None!=self.x_find(e):
                return True
            else:
                return False


    def e_wait_n_click(self,sec=None,
                       xpath=None,
                       id=None,
                       css=None,
                       el_path=None):
        if xpath:
            try:
                element = WebDriverWait(self.driver,sec).until(
                    EC.presence_of_element_located((By.XPATH,el_path ))
                )
                element.click()
                #return True
            except:
                print('error cant find '+element)
                #return False

    def e_wait(self,sec=None,
               xpath=None,
               el_path=None):
        try:
            element = WebDriverWait(self.driver,sec).until(
                EC.presence_of_element_located((By.XPATH,el_path ))
            )
            return True
        except:
            print('error cant find '+element)
            return False
