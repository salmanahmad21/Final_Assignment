from pages.locators_page import *


class Form5thPage(BaseMethods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def required_checks_empty_response_page5(self):
        obj = BaseMethods(self.driver)
        all_titles = obj.get_all_elements(all_input_title_selectors)
        obj.wait_for_ele_invisible(first_page_next_btn)
        page5_error_messages = obj.get_all_elements(all_error_msg)
        nxt = obj.get_all_elements(third_page_next_btn)
        obj.wait_for_ele_invisible(first_page_next_btn)
        add_file_btn = obj.get_all_elements(page5_add_btn)

        for i in range(len(all_titles)):

            if all_titles[i].text == "Upload Image File *":
                nxt[3].click()
                obj.wait_for_ele_invisible(first_page_next_btn)
                print("In Images >>> ")
                if page5_error_messages[i].text == " This is a required question":
                    print("Error message : ", page5_error_messages[i].text, " Please select any option for >>> :",
                          all_titles[i].text)
                    assert "This is a required question" in page5_error_messages[i].text
                for k in range(1):
                    if all_titles[i].text == "Upload Image File *" and i == 0:
                        for s in range(5):
                            add_file_btn[i].click()
                            obj.wait_for_ele_invisible(first_page_next_btn)
                            frame_ele = obj.get_all_elements(page5_iframes)
                            frame_id1 = frame_ele[s].get_attribute("id")
                            obj.wait_for_frames(frame_id1)
                            obj.wait_for_ele_invisible(frame_id1)
                            obj.click(page5_img_title_btn)
                            time.sleep(1)
                            img = obj.get_element_property(page5_img)
                            time.sleep(1)
                            img.click()
                            time.sleep(1)
                            obj.click(page5_select_btn)
                            self.driver.switch_to.default_content()
                            time.sleep(1)
                    elif all_titles[i].text == "Upload Image File *" and i == 1:
                        for t in range(1, 6):
                            add_file_btn[i].click()
                            time.sleep(1)
                            frame_ele = obj.get_all_elements(page5_iframes)
                            frame_id1 = frame_ele[t].get_attribute("id")
                            obj.wait_for_frames(frame_id1)
                            time.sleep(1)
                            obj.click(page5_img_title_btn)
                            time.sleep(2)
                            img = obj.get_element_property(page5_img)
                            time.sleep(2)
                            img.click()
                            time.sleep(1)
                            obj.click(page5_select_btn)
                            self.driver.switch_to.default_content()
                            time.sleep(1)

            elif all_titles[i].text == "Upload pdf file *":
                nxt[3].click()
                obj.wait_for_ele_invisible(first_page_next_btn)
                print("In PDF >>> ")
                if page5_error_messages[i].text == " This is a required question":
                    print("Error message : ", page5_error_messages[i].text, " Please select any option for >>> :",
                          all_titles[i].text)
                    assert "This is a required question" in page5_error_messages[i].text
                for k in range(1):
                    if all_titles[i].text == "Upload pdf file *" and i == 0:
                        for x in range(1):
                            add_file_btn[i].click()
                            obj.wait_for_ele_invisible(first_page_next_btn)
                            frame_elements = obj.get_all_elements(page5_iframes)
                            frame_id2 = frame_elements[x].get_attribute("id")
                            obj.wait_for_frames(frame_id2)
                            obj.wait_for_ele_invisible(frame_id2)
                            obj.click(page5_titles_btn)
                            obj.wait_for_ele_invisible(frame_id2)
                            pdf = obj.get_element_property(page5_pdf_file)
                            obj.wait_for_ele_invisible(frame_id2)
                            pdf.click()
                            obj.wait_for_ele_invisible(frame_id2)
                            obj.click(page5_select_btn)
                            self.driver.switch_to.default_content()
                            obj.wait_for_ele_invisible(frame_id2)
                    elif all_titles[i].text == "Upload pdf file *" and i == 1:
                        for z in range(5, 6):
                            add_file_btn[i].click()
                            obj.wait_for_ele_invisible(first_page_next_btn)
                            frame_elements = obj.get_all_elements(page5_iframes)
                            frame_id2 = frame_elements[i].get_attribute("id")
                            obj.wait_for_frames(frame_id2)
                            obj.wait_for_ele_invisible(frame_id2)
                            obj.click(page5_titles_btn)
                            obj.wait_for_ele_invisible(frame_id2)
                            pdf = obj.get_element_property(page5_pdf_file)
                            obj.wait_for_ele_invisible(frame_id2)
                            obj.wait_for_ele_invisible(frame_id2)
                            pdf.click()
                            obj.wait_for_ele_invisible(frame_id2)
                            obj.click(page5_select_btn)
                            self.driver.switch_to.default_content()
                            obj.wait_for_ele_invisible(frame_id2)

        nxt[3].click()
        obj.wait_for_ele_invisible(first_page_next_btn)