import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestContact:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()


    @pytest.mark.parametrize('args',analyze_file("contact_data.yaml","test_contact"))
    def test_contact(self,args):
        name = args["name"]
        tel = args["tel"]
        self.page.contactpage.click_add_contact()
        self.page.newcontactpage.input_name_text(name)
        self.page.newcontactpage.input_phone_text(tel)
        self.page.newcontactpage.click_back_button()

        assert name == self.page.savedcontactpage.get_phone_name_text()