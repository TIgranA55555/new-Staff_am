from random import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MidLevelPage:

    def __init__(self, driver):
        self.driver = driver

    VIEW_MORE_BTNS = (By.XPATH, "//div[@class='job-inner-right text-right load-more-container pull-right']")
    REQUIREMENT_LEVEL = (By.XPATH, '//h3/span')

    def extract_view_more_buttons_list(self):
        return self.driver.find_elements(*self.VIEW_MORE_BTNS)

    def requirement_candidate_level_extract(self):
        return self.driver.find_element(*self.REQUIREMENT_LEVEL).text


