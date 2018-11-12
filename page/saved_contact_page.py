from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SavedContactPage(BaseAction):

    phone_name_text = By.ID, "com.android.contacts:id/large_title"

    def get_phone_name_text(self):
        return self.get_text(self.phone_name_text)

