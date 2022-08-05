import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.base_class import BaseClass


class ProfilePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    EDUCATION = (By.XPATH, '//span[@data-url="/en/users/resume/update-education/56639"]/i')
    STUDY_CITY = (By.ID, 'educationform-location')
    SUBMIT_BTN = (By.XPATH, '//button[@type="submit"]')
    NOTIFICATION = (By.XPATH, '//h2[contains(text(),"Notification")]')

    def education_city_enter(self):
        self.driver.find_element(*self.EDUCATION).click()
        self.verify_visibility_of_element(self.STUDY_CITY, 10)
        self.driver.find_element(*self.STUDY_CITY).clear()
        self.driver.find_element(*self.STUDY_CITY).send_keys('Moscow')
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def notification_text(self):
        return self.driver.find_element(*self.NOTIFICATION).text
