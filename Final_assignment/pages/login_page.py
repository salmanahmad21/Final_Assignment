from pages.form_page import *


class LoginPage(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def login(self):
        obj = BaseMethods(self.driver)
        obj.send_values(input_email, email_address)
        obj.click(next_btn)
        obj.send_values(input_password, password)
        obj.click(pass_next_btn)
        obj.wait_for_ele_visible(input_email)