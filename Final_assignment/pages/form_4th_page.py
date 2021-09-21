from pages.locators_page import *


class Form4thPage(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def required_checks_empty_response_page4(self):
        obj = BaseMethods(self.driver)
        all_titles = obj.get_all_elements(all_input_title_selectors)
        options_btn = obj.get_all_elements(page4_drop_down_punjab)
        obj.wait_for_ele_invisible(first_page_next_btn)
        page4_error_messages = obj.get_all_elements(all_error_msg)
        nxt = obj.get_all_elements(third_page_next_btn)
        for i in range(len(all_titles)):
            if all_titles[i].text == "Capital of Punjab *":
                obj.wait_for_ele_invisible(first_page_next_btn)
                nxt[1].click()
                obj.wait_for_ele_invisible(first_page_next_btn)
                if page4_error_messages[i].text == " This is a required question":
                    print("Error message : ", page4_error_messages[i].text, " Please select any option for >>> :",
                          all_titles[i].text)
                    assert "This is a required question" in page4_error_messages[i].text
                all_ques.append(all_titles[i].text)
                options_btn[i].click()
                obj.wait_for_ele_invisible(first_page_next_btn)
                obj.click(page4_punjab_ans)
                random_ans.append(page4_punjab_ans_input_city)

            elif all_titles[i].text == "Capital of Pakistan *":
                all_ques.append(all_titles[i].text)
                obj.wait_for_ele_invisible(first_page_next_btn)
                nxt[1].click()
                obj.wait_for_ele_invisible(first_page_next_btn)
                if page4_error_messages[i].text == " This is a required question":
                    print("Error message : ", page4_error_messages[i].text, " Please select any option for >>> :",
                          all_titles[i].text)
                    assert "This is a required question" in page4_error_messages[i].text

                options_btn[i].click()
                obj.wait_for_ele_invisible(first_page_next_btn)
                obj.click(page4_pakistan_ans)
                random_ans.append(page4_pakistan_ans_input_city)
        obj.wait_for_ele_invisible(first_page_next_btn)
        nxt[1].click()