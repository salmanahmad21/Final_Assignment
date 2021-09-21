import time
from config.config import *
from pages.form_page import *
from pages.score_card_response_page import *
from pages.login_page import *
from pages.form_1st_page import *
from pages.form_2nd_page import *
from pages.form_3rd_page import *
from pages.form_4th_page import *
from pages.form_5th_page import *
from pages.form_6th_page import *

from pages.locators_page import *

import unittest


class TestAssignment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=driver_path)

    def test_assignment(self):
        obj_login = LoginPage(self.driver)
        obj_page1 = Form1stPage(self.driver)
        obj_page2 = Form2ndPage(self.driver)
        obj_page3 = Form3rdPage(self.driver)
        obj_page4 = Form4thPage(self.driver)
        obj_page5 = Form5thPage(self.driver)
        obj_page6 = Form6thPage(self.driver)
        obj_csv = Csv(self.driver)
        self.driver.get(target_url)
        obj_login.login()
        # obj_page1.page1_empty_positive_check()
        # obj_page2.required_checks_empty_response_page2()
        # obj_page3.required_checks_empty_response_page3()
        # obj_page4.required_checks_empty_response_page4()
        # obj_page5.required_checks_empty_response_page5()
        # obj_page6.required_checks_empty_response_page6()
        # obj_csv.write_data()




if __name__ == "__main__":
    unittest.main()
