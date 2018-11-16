import page.base
import locator.l
import time
import re
class PageSMS(page.base.PageBase):


    def open_qealty(self):
        url = 'https://qealty.ru/'
        self.open_by_url(url)

    def get_code(self):
        driver = self.driver
        phone_number='123'
        time.sleep(10)
        element = self.find('x',
                         locator.l.l['xp.th.frame'])
        #re.match()#.print (element.text)
        match = re.search(r': (\d+)', element.text)
        if match:
            print ('found', match.group(1)) ## 'found word:cat)
            return match.group(1)
        else:
            print ('didnt match')
        #print (result)
        return None

    def get_sms(self):
        driver = self.driver
        driver.get(self.url)

        sms_text='1243214'
        return sms_text
