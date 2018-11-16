import page.base
import locator.l

class PageSearch(page.base.PageBase):

    def froom(self,addr):
        self.clear_froom()
        self.feel('i',
                  'addressFrom',
                  addr)
        #self.feel('x',
        #          '/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[1]/span/span[2]',#locator.l.l['xp.from'],
        #          addr)

    def to(self,addr):
        self.feel('i',
                  'addressTo',
                  addr)
        #self.feel('x',
        #          '/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[3]/span/span[2]/span[1]',#locator.l.l['xp.to'],
        #          addr)


    def set_phone(self,phone):
        self.feel('x',
                  locator.l.l['xp.phone'],
                  phone)

    def click_call(self):
        #self.driver.f
        #self.driver.find_elements_by_class_name('button button_size_xl button_theme_action js-order-button i-bem button_js_inited').click()
        self.click('x',
                   locator.l.l['xp.call'])
        #self.click('x',
        #           locator.l.l['xp.call'])

    def set_code(self,code):
        self.feel('x',
                  '/html/body/div[1]/div[5]/div/div/div/div[3]/div[1]/span/span/input',#'*//div[3]/div[1]/span/span/input',
                  code)

    def submit_code(self):
        self.click('x',
                  '/html/body/div[1]/div[5]/div/div/div/div[3]/div[1]/div/button')

    def check_frame(self):
        try:
            self.e_wait(sec=10,
                        xpath=True,
                        el_path=locator.l.l['xp.order'])
            return True
        except:
            return False

        #if None!=self.find('x',
        #          '/html/body/div[1]/div[6]/div[1]/div'):
        #    return True
        #return False


    def demo(self):
        #self.driver.find('body > div.b-page__main.b-page__main_indent_menu.js-placeholder.js-placeholder_view_main > div.layout.layout_type_body.layout_wrap_normal.layout_view-name_index.clearfix > div:nth-child(1) > div.island.island_padding_normal.order.i-bem > div.grid-taxi > div:nth-child(6) > div:nth-child(2) > button')

        try:
            self.e_wait_n_click(sec=20,
                                xpath=True,
                                el_path=locator.l.l['xp.demo'])
            self.e_wait(sec=20,
                        xpath=True,
                        el_path=locator.l.l['xp.order'])
            #element = WebDriverWait(self.driver,10).until(
            #    EC.presence_of_element_located((By.XPATH, ))
            #)
            #element.click()
            #element2 = WebDriverWait(self.driver, 10).until(
            #    EC.presence_of_element_located((By.XPATH, ))
            #)
            #element2.click()
            return True
        except:
            return False



        #self.driver.find_element_by_xpath('*//div[1]/div[2]/div[6]/div[2]/button').click()
        #self.click('x',
        #           '/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[6]/div[2]/button')
        #return self.check_frame()

    def check_error_from(self):
        return self.is_exists('/html/body/div[6]/div[2]')

    def clear_froom(self):
        self.e_wait_n_click(sec=10,
                            xpath=True,
                            el_path='/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[1]/span/span[1]/span[2]')
    def error_title(self):
        return self.e_wait(sec=10,
                    xpath=True,
                    el_path='/html/body/div[6]/div[2]')