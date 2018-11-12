from page.contact_page import ContactPage
from page.new_contact_page import NewContactPage
from page.saved_contact_page import SavedContactPage


class Page:

    def __init__(self,driver):
        self.driver = driver
        self.page = Page

    @property
    def contactpage(self):
        return ContactPage(self.driver)

    @property
    def newcontactpage(self):
        return NewContactPage(self.driver)

    @property
    def savedcontactpage(self):
        return SavedContactPage(self.driver)


