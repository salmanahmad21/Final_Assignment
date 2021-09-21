from pages.locators_page import *


class Form6thPage(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def required_checks_empty_response_page6(self):
        obj = BaseMethods(self.driver)
        all_titles = obj.get_all_elements(all_input_title_selectors)
        obj.wait_for_ele_invisible(first_page_next_btn)
        page6_error_messages = obj.get_all_elements(all_error_msg)
        nxt = obj.get_all_elements(third_page_next_btn)
        for i in range(len(all_titles)):

            if all_titles[i].text == "Enter Current date *":
                obj.wait_for_ele_invisible(title_head)
                nxt[1].click()
                obj.wait_for_ele_invisible(title_head)
                if page6_error_messages[i].text == " This is a required question":
                    print("Error message : ", page6_error_messages[i].text, " Please select any option for >>> :",
                          all_titles[i].text)
                    assert "This is a required question" in page6_error_messages[i].text
                obj.wait_for_ele_invisible(title_head)
                dates = obj.dates()
                obj.send_values(page6_input_date_selector, dates)
                obj.wait_for_ele_invisible(title_head)
            elif all_titles[i].text == "Enter Current time *":
                obj.wait_for_ele_invisible(title_head)
                nxt[1].click()
                obj.wait_for_ele_invisible(title_head)
                if page6_error_messages[i].text == " This is a required question":
                    print("Error message : ", page6_error_messages[i].text, " Please select any option for >>> :",
                          all_titles[i].text)
                    assert "This is a required question" in page6_error_messages[i].text
                obj.send_values(page6_input_time_hour_selector, "09")
                obj.wait_for_ele_invisible(title_head)
                obj.send_values(page6_input_time_min_selector, "10")
                obj.wait_for_ele_invisible(title_head)
        nxt[1].click()
        obj.wait_for_ele_invisible(first_page_next_btn)