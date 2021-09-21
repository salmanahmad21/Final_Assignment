from config.config import *
from pages.scoring_page import *
import unittest


class TestScoringValues(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=driver_path)

    def test_scoring(self):
        obj_scoring = ScoringMethods(self.driver)
        self.driver.get(view_score_url)
        score_values, web_score_value = obj_scoring.scoring()
        self.assertEqual(score_values, web_score_value, "Score not matching with website")

