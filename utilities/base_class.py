import random
import time

import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
#from PageObjects import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_visibility_of_element(self, locator, timeout):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def select_from_dropdown(self, elem, index):
        dropdown = Select(elem)
        dropdown.select_by_index(index)

    def open_vacancies_page_from_job_titles(self,  home_page_driver, index):
        elem = home_page_driver.click_on_job_titles()
        self.select_from_dropdown(elem, index)
        vacancyPageObject = home_page_driver.click_on_search_button()
        return vacancyPageObject

    def checking_mid_level_with_loop(self, elements_list, sample_size, driver):
        for i in random.sample(range(len(elements_list)), 2):
            time.sleep(2)
            elements_list[i].click()
            assert "Mid level" in driver.requirement_candidate_level_extract()
            self.driver.back()
            self.driver.refresh()
            elements_list = driver.extract_view_more_buttons_list()
