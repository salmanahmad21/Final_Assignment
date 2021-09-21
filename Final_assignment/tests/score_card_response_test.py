from config.config import *
from pages.score_card_response_page import *
import unittest


class TestScoreCardResponse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=driver_path)

    def test_score_card_response(self):
        obj_score_card_response = ScoreCardResponseMethods(self.driver)
        self.driver.get(view_score_url)
        obj_score_card_response.score_card_csv()


