from pages.locators_page import *


class Form1stPage(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def page1_empty_positive_check(self):
        obj = BaseMethods(self.driver)
        obj.wait_for_ele_invisible(first_page_next_btn)
        all_titles = obj.get_all_elements(all_input_title_selectors)
        all_values = obj.get_all_elements(all_input_values_selectors)
        error_messages = obj.get_all_elements(all_error_msg)

        for i in range(len(all_titles)):
            if all_titles[i].text == "Name *":
                all_ques.append(all_titles[i].text)
                all_values[i].clear()
                obj.click(first_page_next_btn)
                obj.wait_for_ele_invisible(first_page_next_btn)
                if error_messages[i].text == " This is a required question":
                    error_of = all_titles[i].text
                    print("Error in >>> ", error_of, "Error Message >>> ", error_messages[i].text)
                    assert "This is a required question" in error_messages[i].text
                all_values[i].send_keys(form_input_name)
                random_ans.append(form_input_name)
                obj.click(first_page_next_btn)

            elif all_titles[i].text == "Phone Number *":
                all_ques.append(all_titles[i].text)
                all_values[i].clear()
                obj.click(first_page_next_btn)
                obj.wait_for_ele_invisible(first_page_next_btn)
                if error_messages[i].text == " This is a required question":
                    error_of = all_titles[i].text
                    print("Error in >>> ", error_of, "Error Message >>> ", error_messages[i].text)
                    assert "This is a required question" in error_messages[i].text
                all_values[i].send_keys(form_input_phone_number)

                random_ans.append(form_input_phone_number)
                obj.click(first_page_next_btn)
                obj.wait_for_ele_invisible(first_page_next_btn)

            elif all_titles[i].text == "Email *":
                all_ques.append(all_titles[i].text)
                all_values[i].clear()
                obj.click(first_page_next_btn)
                obj.wait_for_ele_invisible(first_page_next_btn)

                if error_messages[i].text == " This is a required question":
                    error_of = all_titles[i].text
                    print("Error in >>> ", error_of, "Error Message >>> ", error_messages[i].text)
                    assert "This is a required question" in error_messages[i].text
                all_values[i].send_keys(form_input_email)
                obj.wait_for_ele_invisible(first_page_next_btn)
                random_ans.append(form_input_email)
                obj.click(first_page_next_btn)

            elif all_titles[i].text == "CNIC *":
                all_ques.append(all_titles[i].text)
                all_values[i].clear()
                obj.click(first_page_next_btn)
                if error_messages[i].text == " This is a required question":
                    error_of = all_titles[i].text
                    print("Error in >>> ", error_of, "Error Message >>> ", error_messages[i].text)
                    assert "This is a required question" in error_messages[i].text

                obj.wait_for_ele_invisible(first_page_next_btn)
                all_values[i].send_keys(form_input_cnic)
                random_ans.append(form_input_cnic)
                obj.click(first_page_next_btn)

    def page1_invalid_check(self):
        obj = BaseMethods(self.driver)
        obj.wait_for_ele_invisible(first_page_next_btn)
        all_titles = obj.get_all_elements(all_input_title_selectors)
        all_values = obj.get_all_elements(all_input_values_selectors)
        for i in range(len(all_titles)):
            if all_titles[i].text == "Name *":
                all_values[i].send_keys(form_input_name)

            elif all_titles[i].text == "Phone Number *":
                all_values[i].send_keys(form_input_phone_number)

            elif all_titles[i].text == "Email *":
                all_values[i].send_keys(form_input_email)

            elif all_titles[i].text == "CNIC *":
                all_values[i].clear()
                all_values[i].send_keys(form_input_cnic)

        obj.click(first_page_next_btn)
        obj.wait_for_ele_invisible(first_page_next_btn)
        error_messages = obj.get_all_elements(all_error_msg)
        for i in range(len(all_titles)):
            if all_titles[i].text == "Name *":
                pass
            elif all_titles[i].text == "Phone Number *":
                if error_messages[i].text == " Must match pattern":
                    print("Validation Error in >>> :", all_titles[i].text, "Error message is >>>: ",
                          error_messages[i].text)
                    assert "Must match pattern" in error_messages[i].text
            elif all_titles[i].text == "Email *":
                if error_messages[i].text == " Must be a valid email":
                    print("Validation Error in >>> :", all_titles[i].text, "Error message is >>>: ",
                          error_messages[i].text)
                    assert "Must be a valid email" in error_messages[i].text
            elif all_titles[i].text == "CNIC *":
                if error_messages[i].text == " Must match pattern":
                    print("Validation Error in >>> :", all_titles[i].text, "Error message is >>>: ",
                          error_messages[i].text)
                    assert "Must match pattern" in error_messages[i].text
