from pages.locators_page import *


class Form2ndPage(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def required_checks_empty_response_page2(self):
        obj = BaseMethods(self.driver)
        all_titles = obj.get_all_elements(all_input_title_selectors)
        page2_ans = obj.get_all_elements(page2_ans_opt_selector)
        obj.wait_for_ele_invisible(first_page_next_btn)
        for i in range(len(all_titles)):
            if all_titles[i].text == "Select the name which is NOT a type of the locater? *":
                all_ques.append(all_titles[i].text)
                obj.wait_for_ele_invisible(first_page_next_btn)
                obj.click(second_page_next_btn)
                obj.wait_for_ele_invisible(first_page_next_btn)
                page2_error_messages1 = obj.get_all_elements(all_error_msg)
                obj.wait_for_ele_invisible(first_page_next_btn)
                if page2_error_messages1[i] == " This is a required question":
                    print("Please Select any option for >>> ", all_titles[i].text)
                    assert "This is a required question" in page2_error_messages1[i].text
                for j in range(len(page2_ans)):
                    if page2_ans[j].text == "Name":
                        random_ans.append(page2_ans[j].text)
                        page2_ans[j].click()
                        obj.wait_for_ele_invisible(first_page_next_btn)
            elif all_titles[i].text == "Use of Firebug in Selenium? *":
                all_ques.append(all_titles[i].text)
                obj.wait_for_ele_invisible(first_page_next_btn)
                obj.click(second_page_next_btn)
                obj.wait_for_ele_invisible(first_page_next_btn)
                page2_error_messages2 = obj.get_all_elements(all_error_msg)
                if page2_error_messages2[i] == " This is a required question":
                    print("Please Select any option for >>> ", all_titles[i].text)
                    assert "This is a required question" in page2_error_messages2[i].text
                for j in range(len(page2_ans)):
                    if page2_ans[j].text == "Parallel Testing":
                        random_ans.append(page2_ans[j].text)
                        obj.wait_for_ele_invisible(first_page_next_btn)
                        page2_ans[j].click()
                        obj.wait_for_ele_invisible(first_page_next_btn)
        obj.click(second_page_next_btn)
