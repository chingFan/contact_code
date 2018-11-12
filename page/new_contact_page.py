from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewContactPage(BaseAction):

    name_text = By.XPATH, "//*[@text='姓名']"

    phone_text = By.XPATH, "//*[@text='电话']"

    back_button = By.XPATH, "//*[@content-desc='向上导航']"

    def input_name_text(self,text):
        self.input(self.name_text,text)

    def input_phone_text(self,text):
        self.input(self.phone_text,text)

    def click_back_button(self):
        self.click(self.back_button)