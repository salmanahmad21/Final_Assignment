from pages.locators_page import *


class Form3rdPage(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def required_checks_empty_response_page3(self):
        obj = BaseMethods(self.driver)
        obj.wait_for_ele_invisible(first_page_next_btn)
        all_titles_page_3 = obj.get_all_elements(all_input_title_selectors)
        page3_ans = obj.get_all_elements(page3_ans_opt_selector)
        obj.wait_for_ele_invisible(first_page_next_btn)
        nxt = obj.get_all_elements(third_page_next_btn)

        for i in range(len(all_titles_page_3)):
            if all_titles_page_3[i].text == "Select the correct answers *":
                all_ques.append(all_titles_page_3[i].text)
                obj.wait_for_ele_invisible(first_page_next_btn)
                nxt[1].click()
                obj.wait_for_ele_invisible(first_page_next_btn)
                page3_error_messages1 = obj.get_all_elements(all_error_msg)
                obj.wait_for_ele_invisible(first_page_next_btn)
                if page3_error_messages1[i].text == " This is a required question":
                    print("Please Select any option for >>> ", all_titles_page_3[i].text)
                    assert "This is a required question" in page3_error_messages1[i].text
                for j in range(len(page3_ans)):
                    if page3_ans[j].text == "63/7 = 54/6":
                        obj.wait_for_ele_invisible(first_page_next_btn)
                        a1 = page3_ans[j].text
                        page3_ans[j].click()
                    elif page3_ans[j].text == "4*10 = 5*8":
                        obj.wait_for_ele_invisible(first_page_next_btn)
                        a2 = page3_ans[j].text
                        page3_ans[j].click()
                    elif page3_ans[j].text == "72/9 = 64/8":
                        obj.wait_for_ele_invisible(first_page_next_btn)
                        a3 = page3_ans[j].text
                        page3_ans[j].click()
                if a1 and a2 and a3 != "":
                    random_ans.append([a1, a2, a3])
            elif all_titles_page_3[i].text == "Select the two numbers that are not prime. *":
                obj.wait_for_ele_invisible(first_page_next_btn)
                all_ques.append(all_titles_page_3[i].text)
                obj.wait_for_ele_invisible(first_page_next_btn)
                nxt[1].click()
                obj.wait_for_ele_invisible(first_page_next_btn)
                page3_error_messages2 = obj.get_all_elements(all_error_msg)
                obj.wait_for_ele_invisible(first_page_next_btn)
                if page3_error_messages2[i].text == " This is a required question":
                    print("Please Select any option for >>> ", all_titles_page_3[i].text)
                    assert "This is a required question" in page3_error_messages2[i].text
                for j in range(len(page3_ans)):
                    if page3_ans[j].text == "51":
                        page3_ans[j].click()
                        for k in range(len(page3_ans)):
                            if page3_ans[k].text == "21":
                                random_ans.append([page3_ans[j].text, page3_ans[k].text])
                                page3_ans[k].click()

        nxt[1].click()
        obj.wait_for_ele_invisible(first_page_next_btn)