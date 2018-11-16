import selenium
import helper.driver
import page.search
import helper.http
import page.qealty
import pytest
import allure
import os
import time


class TestSearch(object):
    def setup(self):
        #sms gateway
        self.chrome_driver_for_sms = helper.driver.WinChrome().return_driver()
        self.page_sms = page.qealty.PageSMS(self.chrome_driver_for_sms)

        #taxi
        self.chrome_driver = helper.driver.WinChrome().return_driver()
        self.page_search = page.search.PageSearch(self.chrome_driver)

        #http request
        #self.http=helper.http.HttpRequest('https://qealty.ru/')

    def teardown(self):
        #time.sleep(120)
        self.chrome_driver.close()
        self.chrome_driver_for_sms.close()

    @allure.feature('search some taxi')
    @allure.story('demo order')
    @allure.issue('issue3')
    @allure.severity('critical')
    def test_search_negative(self):
        page = self.page_search
        page.open()
        page.clear_froom()
        page.click_call()
        assert True == page.error_title()

    @pytest.mark.parametrize('froom',['Профсоюзная улица, 105'])
    @pytest.mark.parametrize('to', ['Профсоюзная улица, 107'])
    @pytest.mark.parametrize('phone', ['+79776585121'])
    #testdata = ['from','to','+123']
    #@pytest.mark.parametrize("fromm,to,phone",testdata)
    @allure.feature('search some taxi')
    @allure.story('feel from, to, phone fields and set taxi')
    @allure.issue('issue1')
    @allure.severity('blocker')
    #def test_positive_search(self,fromm='123',to='456',phone='789'):
    def test_search_positive(self,froom,to,phone):
        #http=self.http
        page = self.page_search
        page.open()
        #assert True == page.demo()

        #self.chrome_driver.refresh()


        page.to(to)
        page.froom(froom)
        page.set_phone(phone)
        page.click_call()

        #http.get_code()

        qealty=self.page_sms
        qealty.open_qealty()
        code = qealty.get_code()

        page.set_code(code)
        page.submit_code()
        assert True == page.check_frame()

    @allure.feature('search some taxi')
    @allure.story('demo order')
    @allure.issue('issue3')
    @allure.severity('critical')
    def test_search_demo(self):
        page = self.page_search
        page.open()
        assert True == page.demo()