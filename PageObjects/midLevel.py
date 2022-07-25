from random import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MidLevelPage:

    def __init__(self, driver):
        self.driver = driver

    mid_level_click = (By.XPATH, '//div//div[@id="jobsfilter-job_candidate_level"]/label/input[@value="3"]')

    #driver.find_element(By.XPATH, '//div//div[@id="jobsfilter-job_candidate_level"]/label/input[@value="3"]').click()

    view_more_buttons = "//div[@class='job-inner-right text-right load-more-container pull-right']"
    view_more_buttons_list = driver.find_elements(By.XPATH, view_more_buttons)
    for i in random.sample(range(len(view_more_buttons_list)), 2):
        wait = WebDriverWait(driver, 15)
        wait.until(expected_conditions.element_to_be_clickable(view_more_buttons_list[i]))
        view_more_buttons_list[i].click()
        assert "Mid level" in driver.find_element(By.XPATH, '//h3/span').text
        driver.back()
        driver.refresh()
        view_more_buttons_list = driver.find_elements(By.XPATH, view_more_buttons)



