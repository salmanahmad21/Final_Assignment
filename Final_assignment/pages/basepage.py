from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd
import csv
from datetime import datetime
from os import write



class BaseMethods:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator)).click()
        except:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(locator)).click()
        # finally:
        #     self.driver.find_element_by_css_selector(locator).click()

    def send_values(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)).text
        except (ValueError, TimeoutError, Exception):
            return None

    def wait_for_ele_invisible(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element(locator))
        except (ValueError, TimeoutError, Exception):
            return None

    def get_all_elements(self, locator):
        try:
            return self.driver.find_elements_by_class_name(locator)
        except:
            return self.driver.find_elements_by_css_selector(locator)

    def get_element_property(self, locator):
        ele = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator))
        return ele

    def clean_text(self, original, expected):
        result = original.replace(original, expected)
        return result

    def wait_for_ele_visible(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator))
        except (ValueError, TimeoutError, Exception):
            return None

    def send_form_values(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator))).send_keys(text)

    def check_the_check_box(self, locator):
        ele = self.driver.find_element_by_css_selector(locator).is_selected()
        return ele

    def page_next_btn(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located(locator))[1].click()
        except:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(locator))[1].click()
        finally:
            print("Locator is not working")

    def drop_down_punjab(self, locator):
        # try:
        #     WebDriverWait(self.driver, 5).until(
        #         EC.visibility_of_all_elements_located(locator))[0].click()
        # except:
        #     WebDriverWait(self.driver, 5).until(
        #         EC.presence_of_all_elements_located(locator))[0].click()
        # finally:
        self.driver.find_elements(locator)[0].click()

    def drop_down_pakistan(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located(locator))[1].click()
        except:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(locator))[1].click()

    def frames(self, locator):
        ids = self.driver.find_elements_by_css_selector(locator)[0]
        return ids

    # def wait_for_frames(self, frame):
    #     WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it(frame.get_attribute('id')))

    def wait_for_frames(self, frame):
        WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.ID, frame)))

    def wait(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element((By.CSS_SELECTOR, ".freebirdFormviewerViewHeaderTitle")))
        except (ValueError, TimeoutError, Exception):
            return None

    def dates(self):
        mm = str(datetime.now().month)
        dd = str(datetime.now().day)
        yy = str(datetime.now().year)
        dates = [mm, dd, yy]
        listToStr = ' '.join([str(elem) for elem in dates])
        acutal_date = listToStr.replace(" ", "")
        return acutal_date

    def clean_questions(self, raw_text):
        head, sep, tail = raw_text.partition('\n')
        q = head.strip()
        return q

    def clean_correct_ans(self, raw_text):
        head, sep, tail = raw_text.partition('\n')
        return tail

    def clean_head(self, raw_text):
        head, sep, tail = raw_text.partition('/')
        obtain = head.strip()
        return obtain

    def clean_tail(self, raw_text):
        head, sep, tail = raw_text.partition('/')
        total = tail.strip()
        return total

    def clean_questions_tail(self, raw_text):
        head, sep, tail = raw_text.partition('\n')
        q = tail.strip()
        return q